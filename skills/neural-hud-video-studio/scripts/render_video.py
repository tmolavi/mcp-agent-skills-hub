#!/usr/bin/env python3
"""
Neural HUD Video Studio — Core Deterministic Video Renderer
Renders high-tech HUD telemetry videos from HTML/Canvas templates using Playwright and FFmpeg.
"""
import os
import sys
import json
import argparse
import asyncio
import subprocess
import tempfile
from pathlib import Path
from playwright.async_api import async_playwright

from generate_audio import generate_hud_audio

REPO_PRESETS = {
    "mwie": {
        "repo_name": "Molavi Web Intelligence (MWIE)",
        "repo_slug": "mwie",
        "status_tag": "PRODUCTION_V2.4",
        "module_1": "SEMANTIC_GRAPH_INDEX",
        "module_2": "GEO_CITATION_PROBE",
        "module_3": "SAFETY_CANONICAL_GATE",
        "logs": [
            {"level": "INIT", "msg": "MWIE Core v2.4 initialized on socket :3050"},
            {"level": "INSPECT", "msg": "Auditing raw HTML DOM vs hydrated client state"},
            {"level": "PROBE", "msg": "Multi-engine citation probe dispatched to Gemini/Perplexity"},
            {"level": "CANONICAL", "msg": "Canonical parity 100% matched across 5 locales"},
            {"level": "EMIT", "msg": "Web Intelligence report synthesized in 412ms"}
        ]
    },
    "sage-audit": {
        "repo_name": "SAGE Audit Engine",
        "repo_slug": "sage-audit",
        "status_tag": "VERIFIED_AUDIT",
        "module_1": "TRI-PILLAR_INSPECTION",
        "module_2": "EVIDENCE_VERIFIER",
        "module_3": "DETERMINISTIC_GATE",
        "logs": [
            {"level": "INIT", "msg": "SAGE Audit daemon initialized with 0-hallucination policy"},
            {"level": "EVAL", "msg": "Evaluating Core Web Vitals 2026 INP/LCP/CLS limits"},
            {"level": "VERIFY", "msg": "Physical evidence verified on disk: 0 assumption drift"},
            {"level": "SCORE", "msg": "Tri-pillar composite score: 98.4 / 100 [A-CLASS]"},
            {"level": "REPORT", "msg": "Deterministic JSON/MD audit ledger published"}
        ]
    },
    "geo-scope": {
        "repo_name": "GEO-Scope AI Benchmark",
        "repo_slug": "geo-scope",
        "status_tag": "BENCHMARK_2026",
        "module_1": "PROMPT_FANOUT_ENGINE",
        "module_2": "CITATION_ABSORPTION",
        "module_3": "CROSS_LLM_MATRIX",
        "logs": [
            {"level": "INIT", "msg": "GEO-Scope testbed active: 600 bilingual commercial queries"},
            {"level": "FANOUT", "msg": "Hydrogen dark-attribution query fanout running"},
            {"level": "EXTRACT", "msg": "Parsing brand citations from Perplexity/SearchGPT"},
            {"level": "CALC", "msg": "Information Gain delta: +42.8% entity recognition"},
            {"level": "FREEZE", "msg": "Reproducible benchmark evidence sealed to SQLite"}
        ]
    },
    "tm-second-brain": {
        "repo_name": "TM Second Brain",
        "repo_slug": "tm-second-brain",
        "status_tag": "PERSISTENT_MEMORY",
        "module_1": "SQLITE_VECTOR_VAULT",
        "module_2": "EPISODIC_RECALL",
        "module_3": "ZERO_CLOUD_LOCKIN",
        "logs": [
            {"level": "MOUNT", "msg": "Local SQLite memory vault opened at /db/second_brain.db"},
            {"level": "INDEX", "msg": "Full-text FTS5 + semantic embeddings synchronized"},
            {"level": "QUERY", "msg": "Cross-session memory retrieval resolved in 2.1ms"},
            {"level": "PRUNE", "msg": "Scratchpad memory garbage collection complete"},
            {"level": "STATUS", "msg": "Zero cloud leakage: 100% offline sovereign storage"}
        ]
    },
    "neural-hud-video-studio": {
        "repo_name": "TM Neural HUD Video Studio",
        "repo_slug": "neural-hud-video-studio",
        "status_tag": "STUDIO_ONLINE",
        "module_1": "CHROMIUM_FRAME_PIPELINE",
        "module_2": "DETERMINISTIC_SEEK_BUS",
        "module_3": "FFMPEG_CYBER_SYNTH",
        "logs": [
            {"level": "INIT", "msg": "Neural HUD Studio engine mounted to headless pipeline"},
            {"level": "STREAM", "msg": "Canvas 3D neural mesh particle coordinates projected"},
            {"level": "MUX", "msg": "Synchronous frame-by-frame pipe streaming to FFmpeg"},
            {"level": "AUDIO", "msg": "Algorithmic cyber sub-bass & telemetry radar synthesized"},
            {"level": "OUTPUT", "msg": "Broadcast-grade MP4 container encoded [H.264 / AAC]"}
        ]
    }
}

async def render_video(
    repo_slug: str,
    output_path: str,
    aspect: str = "9:16",
    duration: float = 6.0,
    fps: int = 24,
    custom_title: str = None
):
    preset = REPO_PRESETS.get(repo_slug, REPO_PRESETS["neural-hud-video-studio"])
    repo_name = custom_title or preset["repo_name"]

    # Resolution settings
    if aspect == "9:16":
        width, height = 720, 1280
    else:
        width, height = 1280, 720

    out_file = Path(output_path).resolve()
    out_file.parent.mkdir(parents=True, exist_ok=True)

    # 1. Read HTML template
    template_path = Path(__file__).resolve().parent.parent / "templates" / "dashboard.html.tmpl"
    if not template_path.exists():
        raise FileNotFoundError(f"Template not found: {template_path}")

    html_content = template_path.read_text(encoding="utf-8")

    # Inject variables
    html_content = html_content.replace("{{SYSTEM_TITLE}}", repo_name)
    html_content = html_content.replace("{{REPO_NAME}}", repo_name)
    html_content = html_content.replace("{{REPO_SLUG}}", preset["repo_slug"])
    html_content = html_content.replace("{{STATUS_TAG}}", preset["status_tag"])
    html_content = html_content.replace("{{MODULE_1_TITLE}}", preset["module_1"])
    html_content = html_content.replace("{{MODULE_2_TITLE}}", preset["module_2"])
    html_content = html_content.replace("{{MODULE_3_TITLE}}", preset["module_3"])
    html_content = html_content.replace("{{ASPECT_RATIO}}", aspect)
    html_content = html_content.replace("{{DURATION}}", str(duration))
    html_content = html_content.replace("{{LOGS_JSON}}", json.dumps(preset["logs"]))
    html_content = html_content.replace("{{METRICS_JSON}}", json.dumps({}))

    total_frames = int(duration * fps)

    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_html = Path(tmpdir) / "index.html"
        tmp_html.write_text(html_content, encoding="utf-8")
        tmp_audio = Path(tmpdir) / "hud_audio.aac"
        tmp_video = Path(tmpdir) / "video_raw.mp4"

        # 2. Synthesize Audio
        print(f"[{repo_slug}] Synthesizing cybernetic audio ({duration}s)...")
        generate_hud_audio(duration, str(tmp_audio))

        # 3. Launch FFmpeg process to receive PNG frames via stdin
        ffmpeg_cmd = [
            "ffmpeg", "-y",
            "-f", "image2pipe",
            "-vcodec", "png",
            "-r", str(fps),
            "-i", "-",
            "-c:v", "libx264",
            "-pix_fmt", "yuv420p",
            "-preset", "veryfast",
            "-crf", "18",
            str(tmp_video)
        ]
        ffmpeg_proc = subprocess.Popen(ffmpeg_cmd, stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)

        # 4. Playwright Capture Loop
        print(f"[{repo_slug}] Capturing {total_frames} frames ({width}x{height} @ {fps}fps)...")
        async with async_playwright() as p:
            browser = await p.chromium.launch(
                headless=True,
                args=["--disable-web-security", "--allow-file-access-from-files", "--no-sandbox"]
            )
            page = await browser.new_page(viewport={"width": width, "height": height})
            await page.goto(f"file://{tmp_html}?aspect={aspect}&duration={duration}")
            await page.wait_for_function("typeof window.seekTo === 'function'")
            await page.evaluate("document.fonts.ready")

            for frame_idx in range(total_frames):
                t = frame_idx / fps
                await page.evaluate(f"window.seekTo({t})")
                # Screenshot buffer directly into FFmpeg stdin
                frame_bytes = await page.screenshot(type="png", timeout=60000, animations="disabled")
                ffmpeg_proc.stdin.write(frame_bytes)

            ffmpeg_proc.stdin.close()
            ffmpeg_proc.wait()
            await browser.close()

        if ffmpeg_proc.returncode != 0:
            stderr = ffmpeg_proc.stderr.read().decode()
            raise RuntimeError(f"FFmpeg video encoding failed: {stderr}")

        # 5. Final Mux Video + Audio
        print(f"[{repo_slug}] Muxing video and audio container...")
        mux_cmd = [
            "ffmpeg", "-y",
            "-i", str(tmp_video),
            "-i", str(tmp_audio),
            "-c:v", "copy",
            "-c:a", "aac",
            "-b:a", "192k",
            "-shortest",
            str(out_file)
        ]
        mux_res = subprocess.run(mux_cmd, capture_output=True, text=True)
        if mux_res.returncode != 0:
            raise RuntimeError(f"FFmpeg muxing failed: {mux_res.stderr}")

        print(f"✓ Video successfully rendered: {out_file}")

        # 6. ffprobe Verification
        probe_cmd = [
            "ffprobe", "-v", "error",
            "-show_entries", "format=duration,size:stream=width,height,codec_name,codec_type",
            "-of", "json",
            str(out_file)
        ]
        probe_res = subprocess.run(probe_cmd, capture_output=True, text=True)
        print(f"Probe verification:\n{probe_res.stdout}")
        return out_file

def main():
    parser = argparse.ArgumentParser(description="Neural HUD Video Studio Renderer")
    parser.add_argument("--repo", default="neural-hud-video-studio", choices=list(REPO_PRESETS.keys()), help="Target repo preset")
    parser.add_argument("--output", default="output/hud_demo.mp4", help="Output MP4 path")
    parser.add_argument("--aspect", default="9:16", choices=["9:16", "16:9"], help="Aspect ratio")
    parser.add_argument("--duration", type=float, default=6.0, help="Duration in seconds")
    parser.add_argument("--fps", type=int, default=24, help="Frames per second")
    parser.add_argument("--title", default=None, help="Custom system title")
    args = parser.parse_args()

    asyncio.run(render_video(
        repo_slug=args.repo,
        output_path=args.output,
        aspect=args.aspect,
        duration=args.duration,
        fps=args.fps,
        custom_title=args.title
    ))

if __name__ == "__main__":
    main()
