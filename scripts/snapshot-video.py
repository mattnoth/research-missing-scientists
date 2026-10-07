#!/usr/bin/env python3
"""
snapshot-video — Phase 3 video leg of the primary-source snapshot pipeline.

Archives a TikTok / YouTube / archive.org / other yt-dlp-supported video as a
research artifact: metadata, captions (when the platform has them), a local
Whisper transcript (when it does not), a thumbnail, the audio track, and a
manifest with content hashes. Also provides programmatic discovery (YouTube
search, creator enumeration) so a research session can find candidates before
spending Whisper compute on them.

Usage
-----
  # Ingest one or more known URLs for a case (keeps the <=720p VIDEO by default)
  python3 scripts/snapshot-video.py ingest --case eskridge URL [URL ...]
        [--model base.en] [--no-transcribe] [--audio-only] [--max-height 720] [--force]
        [--refetch-media] [--cookies-from-browser brave|chrome|safari] [--note "why this matters"]

  # Discover candidates (YouTube search; any language; no API key)
  python3 scripts/snapshot-video.py search "Amy Eskridge scientist" --n 15 [--json]

  # Enumerate a creator's catalogue (YouTube channel, TikTok @user, playlist)
  python3 scripts/snapshot-video.py channel https://www.youtube.com/@PopCrimeTV --n 50 [--json]

Layout
------
  appendices/primary-sources/<case>/snapshots/video/<upload-date>-<platform>-<id>/
      manifest.json             provenance + hashes (always)
      info.json                 trimmed yt-dlp info dict (always)
      thumbnail.<ext>           (when available)
      captions.<lang>.vtt       platform captions (when available)
      transcript.txt            plain text — from captions, else Whisper
      transcript.segments.json  timestamped segments (Whisper path only)
      media.mp4 | media.m4a     the footage (<=720p video by default; audio with --audio-only); gitignored
  appendices/primary-sources/<case>/snapshots/video/INDEX.md   one row per snapshot

Media files are kept LOCALLY (gitignored — a few dozen videos would bloat the repo)
and are the link-rot insurance: the transcript, captions and manifest (with the
media SHA-256) are committed, the footage lives on the maintainer's disk until a
durable off-repo store is chosen (see TODO-research.md "Durable video storage").

Dependencies (user site-packages): yt-dlp (nightly recommended), curl_cffi,
faster-whisper; ffmpeg on PATH. See RUNBOOK.md "Video snapshots".
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PRIMARY = REPO / "appendices" / "primary-sources"

EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")

INFO_DROP_KEYS = {
    "formats", "requested_formats", "thumbnails", "url", "manifest_url",
    "fragments", "http_headers", "automatic_captions", "subtitles",
    "requested_downloads", "requested_subtitles", "heatmap", "_format_sort_fields",
    "downloader_options", "__postprocessors", "_filename", "filename",
}


def log(msg: str) -> None:
    print(f"[snapshot-video] {msg}", file=sys.stderr)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def platform_of(info: dict) -> str:
    ext = (info.get("extractor_key") or info.get("extractor") or "unknown").lower()
    for name in ("tiktok", "youtube", "archive", "reddit", "vimeo", "instagram",
                 "facebook", "twitter", "bilibili", "rumble", "odysee", "bitchute"):
        if name in ext:
            return "archive.org" if name == "archive" else name
    return re.sub(r"[^a-z0-9]+", "-", ext).strip("-") or "unknown"


def safe_id(s: str) -> str:
    return re.sub(r"[^A-Za-z0-9_-]+", "-", s)[:64].strip("-") or "id"


def vtt_to_text(vtt: str) -> str:
    """Flatten WebVTT to plain prose, collapsing the rolling duplicates that
    YouTube auto-captions emit."""
    lines: list[str] = []
    last = ""
    for raw in vtt.splitlines():
        line = raw.strip()
        if not line or line.startswith(("WEBVTT", "NOTE", "Kind:", "Language:", "STYLE", "REGION")):
            continue
        if "-->" in line or re.fullmatch(r"\d+", line):
            continue
        line = re.sub(r"<[^>]+>", "", line)  # strip <c> / timing tags
        line = re.sub(r"\s+", " ", line).strip()
        if not line or line == last:
            continue
        # rolling-window dedupe: skip if this line is a prefix of the previous or vice versa
        if last and (last.endswith(line) or line.startswith(last)):
            lines[-1] = line if len(line) >= len(last) else last
            last = lines[-1]
            continue
        lines.append(line)
        last = line
    return "\n".join(lines).strip() + "\n"


def build_ydl_opts(args, outdir: Path | None, flat: bool = False) -> dict:
    opts: dict = {
        "quiet": True,
        "no_warnings": False,
        "noprogress": True,
        "socket_timeout": 30,
        "retries": 3,
        "ignoreerrors": False,
    }
    try:
        from yt_dlp.networking.impersonate import ImpersonateTarget
        opts["impersonate"] = ImpersonateTarget.from_str(getattr(args, "impersonate", "chrome") or "chrome")
    except Exception:  # curl_cffi not installed; proceed without impersonation
        pass
    cfb = getattr(args, "cookies_from_browser", None)
    if cfb:
        opts["cookiesfrombrowser"] = (cfb,)
    if getattr(args, "extractor_args", None):
        # e.g. "youtubepot-bgutilscript:script_path=/path/generate_once.js"
        from yt_dlp.utils import parse_options  # noqa: F401  (ensures yt_dlp import)
        ea: dict = {}
        for item in args.extractor_args:
            key, _, val = item.partition(":")
            sub: dict = ea.setdefault(key, {})
            for kv in val.split(";"):
                if kv:
                    k, _, v = kv.partition("=")
                    sub[k] = v.split(",")
        opts["extractor_args"] = ea
    if flat:
        opts["extract_flat"] = "in_playlist"
        opts["skip_download"] = True
        return opts
    assert outdir is not None
    # Default is to KEEP THE VIDEO (≤720p mp4): links die, and the footage itself is the
    # evidence. --audio-only is the lightweight alternative for long audio-centric items.
    audio_only = getattr(args, "audio_only", False)
    max_h = getattr(args, "max_height", 720) or 720
    opts.update({
        "outtmpl": {"default": str(outdir / "media.%(ext)s"),
                    "thumbnail": str(outdir / "thumbnail.%(ext)s"),
                    "subtitle": str(outdir / "captions.%(ext)s"),
                    "infojson": str(outdir / "raw-info.%(ext)s")},
        "format": "bestaudio[ext=m4a]/bestaudio/best" if audio_only else
                  (f"bestvideo[height<={max_h}][ext=mp4]+bestaudio[ext=m4a]/"
                   f"bestvideo[height<={max_h}]+bestaudio/best[height<={max_h}]/best"),
        "merge_output_format": None if audio_only else "mp4",
        "writesubtitles": True,
        "writeautomaticsub": True,
        "subtitleslangs": ["en", "en-orig", "en-US", "en-GB", ".*orig"],
        "subtitlesformat": "vtt/best",
        "writethumbnail": True,
        "writeinfojson": True,
        "keepvideo": not audio_only,
        "postprocessors": [
            {"key": "FFmpegExtractAudio", "preferredcodec": "m4a", "preferredquality": "5"},
        ] if audio_only else [],
    })
    return opts


def refetch_media(args, dest: Path, url: str) -> bool:
    """Re-download only the media file into an existing snapshot (e.g. upgrade an
    audio-only capture to video). Transcript, captions and info are left untouched;
    the manifest's media fields are refreshed."""
    import yt_dlp
    tmp = dest.parent / f".tmp-refetch-{dest.name}"
    if tmp.exists():
        shutil.rmtree(tmp)
    tmp.mkdir()
    opts = build_ydl_opts(args, tmp)
    opts.update({"writesubtitles": False, "writeautomaticsub": False,
                 "writethumbnail": False, "writeinfojson": False})
    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            ydl.extract_info(url, download=True)
    except Exception as e:  # noqa: BLE001
        log(f"  refetch FAILED: {e}")
        shutil.rmtree(tmp, ignore_errors=True)
        return False
    new_media = next((p for p in tmp.iterdir() if p.name.startswith("media.")), None)
    if not new_media:
        log("  refetch produced no media file")
        shutil.rmtree(tmp, ignore_errors=True)
        return False
    for old in dest.glob("media.*"):
        old.unlink()
    final = dest / new_media.name
    new_media.rename(final)
    shutil.rmtree(tmp, ignore_errors=True)
    mpath = dest / "manifest.json"
    manifest = json.loads(mpath.read_text()) if mpath.exists() else {}
    manifest.update({
        "media_file": final.name,
        "media_sha256": sha256(final),
        "media_bytes": final.stat().st_size,
        "media_refetched_utc": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "media_kind": "audio" if getattr(args, "audio_only", False) else f"video<={getattr(args, 'max_height', 720)}p",
    })
    mpath.write_text(json.dumps(manifest, indent=1, ensure_ascii=False))
    log(f"  media refetched → {final.relative_to(REPO)} ({final.stat().st_size // 1024} KiB)")
    return True


def transcribe(media: Path, model_name: str, language: str | None = None) -> tuple[str, list[dict], dict]:
    from faster_whisper import WhisperModel
    if language and language != "en" and model_name.endswith(".en"):
        # English-only models cannot transcribe other languages; swap to the multilingual sibling.
        model_name = model_name[:-3]
        log(f"whisper: --language {language} → switching to multilingual model {model_name}")
    log(f"whisper: loading {model_name} (cpu/int8)")
    model = WhisperModel(model_name, device="cpu", compute_type="int8")
    segments_iter, info = model.transcribe(str(media), beam_size=5, vad_filter=True, language=language)
    segs: list[dict] = []
    text_parts: list[str] = []
    for s in segments_iter:
        segs.append({"start": round(s.start, 2), "end": round(s.end, 2), "text": s.text.strip()})
        text_parts.append(s.text.strip())
    meta = {"language": info.language, "language_probability": round(info.language_probability, 3),
            "duration_s": round(info.duration, 1)}
    return " ".join(text_parts).strip() + "\n", segs, meta


def append_index(case_dir: Path, row: dict) -> None:
    idx = case_dir / "INDEX.md"
    header = ("# Video snapshots\n\n"
              "Captured with `scripts/snapshot-video.py`. Media files are local-only (gitignored); "
              "transcripts, captions and manifests are committed. Tier/confidence for any claim made in a "
              "video is assigned where the video is cited, not here.\n\n"
              "| Captured | Uploaded | Platform | Uploader | Title | Length | Transcript | Dir |\n"
              "|---|---|---|---|---|---|---|---|\n")
    if not idx.exists():
        idx.write_text(header)
    line = ("| {capture_date} | {upload_date} | {platform} | {uploader} | {title} | {duration} | {method} | "
            "[{dirname}]({dirname}/) |\n").format(**row)
    key = f"[{row['dirname']}]({row['dirname']}/)"
    existing = idx.read_text().splitlines(keepends=True)
    kept = [l for l in existing if key not in l]  # a re-capture replaces its own row
    idx.write_text("".join(kept) + line)


def cmd_ingest(args) -> int:
    import yt_dlp
    case_dir = PRIMARY / args.case / "snapshots" / "video"
    case_dir.mkdir(parents=True, exist_ok=True)
    rc = 0
    for url in args.urls:
        log(f"ingest: {url}")
        if args.refetch_media:
            # locate the existing snapshot for this URL by manifest source/canonical URL
            match = None
            for m in case_dir.glob("*/manifest.json"):
                try:
                    mj = json.loads(m.read_text())
                except Exception:  # noqa: BLE001
                    continue
                if url in (mj.get("source_url"), mj.get("canonical_url")) or \
                   (mj.get("id") and str(mj["id"]) in url):
                    match = m.parent
                    break
            if match is None:
                log("  no existing snapshot for this URL; run a normal ingest instead")
                rc = 1
                continue
            if not refetch_media(args, match, url):
                rc = 1
            continue
        tmp = case_dir / f".tmp-{safe_id(hashlib.sha1(url.encode()).hexdigest()[:10])}"
        if tmp.exists():
            shutil.rmtree(tmp)
        tmp.mkdir()
        try:
            with yt_dlp.YoutubeDL(build_ydl_opts(args, tmp)) as ydl:
                info = ydl.extract_info(url, download=True)
                info = ydl.sanitize_info(info)
        except Exception as e:  # noqa: BLE001
            log(f"  FAILED: {e}")
            shutil.rmtree(tmp, ignore_errors=True)
            rc = 1
            continue
        if info.get("_type") == "playlist" and info.get("entries"):
            info = next((e for e in info["entries"] if e), info)
        platform = platform_of(info)
        vid = safe_id(str(info.get("id") or "unknown"))
        upload_date = info.get("upload_date") or "undated"
        dirname = f"{upload_date}-{platform}-{vid}"
        dest = case_dir / dirname
        if dest.exists():
            if not args.force:
                log(f"  exists, skipping (use --force to re-capture): {dest.relative_to(REPO)}")
                shutil.rmtree(tmp, ignore_errors=True)
                continue
            shutil.rmtree(dest)
        tmp.rename(dest)

        # tidy files
        media = next((p for p in dest.iterdir() if p.name.startswith("media.")), None)
        thumb = next((p for p in dest.iterdir() if p.name.startswith("thumbnail.")), None)
        raw_info = dest / "raw-info.info.json"
        if raw_info.exists():
            raw_info.unlink()
        captions = sorted(dest.glob("captions.*.vtt")) or sorted(dest.glob("captions.*"))
        # Privacy: some platforms (archive.org) expose the uploader's e-mail as the uploader
        # name. Redact e-mail-like strings before anything is written to the repo.
        for k in ("uploader", "uploader_id", "channel", "channel_id", "uploader_url", "channel_url"):
            if isinstance(info.get(k), str) and EMAIL_RE.search(info[k]):
                info[k] = EMAIL_RE.sub("[uploader e-mail redacted]", info[k])
        if isinstance(info.get("description"), str):
            info["description"] = EMAIL_RE.sub("[e-mail redacted]", info["description"])
        trimmed = {k: v for k, v in info.items() if k not in INFO_DROP_KEYS}
        (dest / "info.json").write_text(json.dumps(trimmed, indent=1, ensure_ascii=False))

        method = "none"
        whisper_meta: dict = {}
        caption_lang = None
        if captions:
            cap = captions[0]
            m = re.match(r"captions\.([^.]+)\.", cap.name)
            caption_lang = m.group(1) if m else None
            (dest / "transcript.txt").write_text(vtt_to_text(cap.read_text(errors="replace")))
            method = "captions"
        elif media and not args.no_transcribe:
            try:
                text, segs, whisper_meta = transcribe(media, args.model, args.language)
                whisper_meta["model"] = args.model if not (args.language and args.language != "en" and args.model.endswith(".en")) else args.model[:-3]
                (dest / "transcript.txt").write_text(text)
                (dest / "transcript.segments.json").write_text(json.dumps(segs, indent=0, ensure_ascii=False))
                method = f"whisper:{args.model}"
            except Exception as e:  # noqa: BLE001
                log(f"  whisper failed: {e}")
                method = "failed"
                rc = 1

        manifest = {
            "source_url": url,
            "canonical_url": info.get("webpage_url") or url,
            "platform": platform,
            "id": info.get("id"),
            "title": info.get("title"),
            "uploader": info.get("uploader") or info.get("channel"),
            "uploader_id": info.get("uploader_id") or info.get("channel_id"),
            "uploader_url": info.get("uploader_url") or info.get("channel_url"),
            "upload_date": upload_date,
            "duration_s": info.get("duration"),
            "view_count": info.get("view_count"),
            "like_count": info.get("like_count"),
            "comment_count": info.get("comment_count"),
            "description": info.get("description"),
            "capture_utc": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "captured_by": "scripts/snapshot-video.py",
            "yt_dlp_version": yt_dlp.version.__version__,
            "media_file": media.name if media else None,
            "media_sha256": sha256(media) if media else None,
            "media_bytes": media.stat().st_size if media else None,
            "media_kind": None if not media else ("audio" if args.audio_only else f"video<={args.max_height}p"),
            "thumbnail_file": thumb.name if thumb else None,
            "captions_files": [c.name for c in captions],
            "caption_lang": caption_lang,
            "transcript_method": method,
            "whisper": whisper_meta or None,
            "note": args.note,
            "tier_note": ("Tier is assigned at citation time. Default for independent creators is T7; "
                          "outlet-run accounts inherit the outlet's tier."),
        }
        (dest / "manifest.json").write_text(json.dumps(manifest, indent=1, ensure_ascii=False))
        dur = info.get("duration")
        append_index(case_dir, {
            "capture_date": manifest["capture_utc"][:10],
            "upload_date": upload_date if upload_date == "undated" else f"{upload_date[:4]}-{upload_date[4:6]}-{upload_date[6:]}",
            "platform": platform,
            "uploader": (manifest["uploader"] or "?").replace("|", "/"),
            "title": (manifest["title"] or "?").replace("|", "/")[:90],
            "duration": f"{int(dur // 60)}:{int(dur % 60):02d}" if dur else "?",
            "method": method,
            "dirname": dirname,
        })
        words = len((dest / "transcript.txt").read_text().split()) if (dest / "transcript.txt").exists() else 0
        log(f"  saved {dest.relative_to(REPO)}  [{method}, {words} words]")
    return rc


def _print_entries(entries: list[dict], as_json: bool) -> None:
    rows = []
    for e in entries:
        if not e:
            continue
        rows.append({
            "id": e.get("id"),
            "url": e.get("url") or e.get("webpage_url"),
            "title": e.get("title"),
            "uploader": e.get("uploader") or e.get("channel"),
            "duration_s": e.get("duration"),
            "view_count": e.get("view_count"),
            "upload_date": e.get("upload_date"),
        })
    if as_json:
        print(json.dumps(rows, indent=1, ensure_ascii=False))
        return
    print("| # | Uploader | Length | Views | Title | URL |")
    print("|---|---|---|---|---|---|")
    for i, r in enumerate(rows, 1):
        d = r["duration_s"]
        dur = f"{int(d // 60)}:{int(d % 60):02d}" if d else "?"
        views = f"{r['view_count']:,}" if r["view_count"] else "?"
        print(f"| {i} | {r['uploader'] or '?'} | {dur} | {views} | {(r['title'] or '?').replace('|', '/')[:80]} | {r['url']} |")


def cmd_search(args) -> int:
    import yt_dlp
    prefix = {"youtube": "ytsearch"}.get(args.platform, "ytsearch")
    query = f"{prefix}{args.n}:{args.query}"
    with yt_dlp.YoutubeDL(build_ydl_opts(args, None, flat=True)) as ydl:
        info = ydl.sanitize_info(ydl.extract_info(query, download=False))
    _print_entries(info.get("entries") or [], args.json)
    return 0


def cmd_channel(args) -> int:
    import yt_dlp
    opts = build_ydl_opts(args, None, flat=True)
    opts["playlistend"] = args.n
    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.sanitize_info(ydl.extract_info(args.url, download=False))
    entries = info.get("entries") or []
    # channel pages nest tabs → flatten one level
    flat: list[dict] = []
    for e in entries:
        if e and e.get("_type") == "playlist" and e.get("entries"):
            flat.extend(e["entries"])
        elif e:
            flat.append(e)
    owner = info.get("uploader") or info.get("channel") or info.get("title")
    for e in flat:
        if e and not (e.get("uploader") or e.get("channel")):
            e["uploader"] = owner
    _print_entries(flat[: args.n], args.json)
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="snapshot-video", description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--impersonate", default="chrome", help="curl_cffi TLS impersonation target (default chrome)")
    common.add_argument("--cookies-from-browser", dest="cookies_from_browser",
                        help="brave|chrome|safari|firefox — only if a platform demands login (YouTube bot-check)")
    common.add_argument("--extractor-args", action="append", dest="extractor_args",
                        help='yt-dlp extractor args, e.g. "youtubepot-bgutilscript:script_path=/x/generate_once.js"')
    sub = p.add_subparsers(dest="cmd", required=True)

    pi = sub.add_parser("ingest", parents=[common], help="archive one or more video URLs for a case")
    pi.add_argument("--case", required=True, help="case slug (eskridge, garcia, …) or 'cross-case'")
    pi.add_argument("urls", nargs="+")
    pi.add_argument("--model", default="base.en", help="faster-whisper model (base.en, small, medium, large-v3)")
    pi.add_argument("--language", default=None,
                    help="ISO language of the speech (es, zh, ru, pt, …). Non-English input needs a multilingual "
                         "model: pass e.g. --model small --language es (an *.en model is auto-swapped)")
    pi.add_argument("--no-transcribe", action="store_true", help="skip Whisper when no captions exist")
    pi.add_argument("--audio-only", action="store_true",
                    help="store audio (m4a) instead of the default <=720p video — for long audio-centric items")
    pi.add_argument("--max-height", type=int, default=720, help="video height cap (default 720)")
    pi.add_argument("--refetch-media", action="store_true",
                    help="re-download only the media file into the existing snapshot (e.g. upgrade audio → video)")
    pi.add_argument("--force", action="store_true", help="re-capture even if the snapshot dir exists")
    pi.add_argument("--note", default=None, help="free-text relevance note stored in manifest")
    pi.set_defaults(fn=cmd_ingest)

    ps = sub.add_parser("search", parents=[common], help="YouTube search (any language) via yt-dlp")
    ps.add_argument("query")
    ps.add_argument("--n", type=int, default=10)
    ps.add_argument("--platform", default="youtube", choices=["youtube"])
    ps.add_argument("--json", action="store_true")
    ps.set_defaults(fn=cmd_search)

    pc = sub.add_parser("channel", parents=[common], help="enumerate a creator / playlist")
    pc.add_argument("url")
    pc.add_argument("--n", type=int, default=50)
    pc.add_argument("--json", action="store_true")
    pc.set_defaults(fn=cmd_channel)

    args = p.parse_args(argv)
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
