---
name: neural-hud-video-studio
description: "Autonomous studio for rendering cyberpunk HUD telemetry showcase videos (9:16 vertical & 16:9 widescreen) for repositories and AI agent architectures. Features 3D particle canvas centerpiece, real-time telemetry strip, live AST diffs, and algorithmic cybernetic audio muxing via Playwright and FFmpeg."
category: automation
risk: low
source: official
author: Taqi Molavi
version: "1.0.0"
triggers:
  - "مهارت ساخت ویدئو اچ تی ام تی"
  - "مهارت ساخت ویدیو اچ تی ام تی"
  - "مهارت ساخت ویدیو html"
  - "مهارت ساخت ویدئو html"
  - "مهارت ساخت ویدیو اچ تی ام ال"
  - "مهارت ساخت ویدئو اچ تی ام ال"
  - "ساخت ویدئو اچ تی ام تی"
  - "ساخت ویدیو اچ تی ام تی"
  - "ساخت ویدیو html"
  - "ساخت ویدئو html"
  - "neural hud video studio"
  - "neural-hud-video-studio"
  - "رندر ویدیوی هاد"
  - "ویدیوی تلمتری هاد"
  - "هاد ویدیو استودیو"
  - "render hud video"
  - "render telemetry video"
---

# Neural HUD Video Studio (`neural-hud-video-studio`)
# مهارت ساخت ویدیو اچ تی ام ال / مهارت ساخت ویدئو اچ تی ام تی

> **Autonomous Broadcast Telemetry & Video Engine for AI Repositories**  
> Developed by **Taqi Molavi** ([molavi.pro](https://molavi.pro)) • Inten Digital Marketing Suite ([inten.asia](https://inten.asia))

`neural-hud-video-studio` transforms abstract code repositories, microservices, and AI agent architectures into **high-tech, Hollywood-grade cyberpunk HUD telemetry videos**. It generates deterministic frames from HTML5/Canvas using headless Chromium via Playwright, mixes algorithmic sub-bass cyber audio in FFmpeg, and outputs broadcast-ready MP4 files for GitHub documentation, YouTube Shorts, Instagram Reels, and web showcase articles.

```
       [ Repository Code & Telemetry Data ]
                        │
                        ▼
    ┌───────────────────────────────────────┐
    │     HTML5 / Canvas HUD Engine         │
    │  • 3D Neural Particle Mesh Sphere     │
    │  • Inset Holographic Subsystem Box    │
    │  • 3 Module Performance Cards         │
    │  • Real-Time Routing / Terminal Logs  │
    │  • Throughput Waveform Sparkline      │
    │  • Thread & Trace Metrics Grid        │
    │  • Live AST Code Diff Stream          │
    └──────────────────┬────────────────────┘
                       │ window.seekTo(t)
        ┌──────────────┴──────────────┐
        ▼                             ▼
 ┌──────────────┐              ┌──────────────┐
 │  Playwright  │              │    FFmpeg    │
 │ Headless     │              │ Algorithmic  │
 │ Frame-by-    │              │ Cyber Audio  │
 │ Frame Pipe   │              │ Synthesizer  │
 └──────┬───────┘              └──────┬───────┘
        │                             │
        └──────────────┬──────────────┘
                       ▼
          [ Broadcast-Ready MP4 ]
    (H.264 Video + AAC Cyber Telemetry Audio)
```

---

## 🚀 Key Features

1. **Ultra-Crisp Cyberpunk Telemetry Aesthetics**:
   - `#060608` deep obsidian base, `#0d0e12` panel containers, neon crimson `#ff2a3c` and amber `#ff5533` accents, with glowing CRT scanlines.
   - Fibonacci sphere 3D neural particle matrix with rotating orbital rings and dynamic node callouts.
   - Inset holographic radar sweep window locked to target subsystems.

2. **100% Deterministic Frame Pipeline**:
   - Zero dropped frames: the browser exposes `window.seekTo(t)` which renders exact mathematical states for frame index `i / fps`.
   - Screenshots are piped directly into FFmpeg stdin via `image2pipe`, avoiding disk thrashing.

3. **Algorithmic Cybernetic Audio Generation**:
   - Synthesizes deep sub-bass drones (55Hz/110Hz), filtered pink noise data center ambiance, high-tech radar chirps, and holographic pulse sweeps natively in FFmpeg. Zero external audio samples required.

4. **Multi-Aspect Ratio & Multi-Language Support**:
   - **`9:16` (720x1280 or 1080x1920)**: Formatted for mobile reels, shorts, and vertical hero slots.
   - **`16:9` (1280x720 or 1920x1080)**: Formatted for desktop headers, GitHub README hero banners, and YouTube embeds.
   - Ready for English, Persian, Azerbaijani, Turkish, and Arabic metadata.

5. **Clean Git Footprint**:
   - Videos are rendered and hosted on `molavi.pro` CDN (`/videos/neural-hud/`), keeping repository commits lightweight while delivering fast streaming to global users.

---

## 🛠️ Quick CLI Usage

### 1. Render Preset Repository Showcase Video
```bash
python3 scripts/render_video.py \
  --repo mwie \
  --output output/mwie_hud.mp4 \
  --aspect 9:16 \
  --duration 6.0 \
  --fps 24
```

Available repository presets:
- `mwie`: Molavi Web Intelligence Engine
- `sage-audit`: SAGE Audit Engine
- `geo-scope`: GEO-Scope AI Benchmark
- `tm-second-brain`: TM Second Brain Persistent Memory
- `neural-hud-video-studio`: TM Neural HUD Video Studio itself

### 2. Custom Repo / System Rendering
```bash
python3 scripts/render_video.py \
  --repo neural-hud-video-studio \
  --title "Custom Agent OS" \
  --output output/custom_agent_hud.mp4 \
  --aspect 16:9 \
  --duration 8.0 \
  --fps 30
```

### 3. Generate Audio Only
```bash
python3 scripts/generate_audio.py 8.0 output/cyber_ambience.aac
```

---

## 📋 Directory Architecture

```
neural-hud-video-studio/
├── SKILL.md                          # Skill definition & execution manual
├── scripts/
│   ├── render_video.py               # Deterministic Playwright + FFmpeg engine
│   ├── generate_audio.py             # Algorithmic cyber audio synthesizer
│   └── render_video.sh               # Quick bash CLI wrapper
├── templates/
│   └── dashboard.html.tmpl           # Modular HUD telemetry HTML5/Canvas template
└── examples/                         # Reference configurations
```

---

## 🌐 Ecosystem Integration

- **Hosted Videos CDN**: `https://molavi.pro/videos/neural-hud/<repo-slug>.mp4`
- **GitHub Repository**: [tmolavi/TM-neural-hud-video-studio](https://github.com/tmolavi/TM-neural-hud-video-studio)
- **Showcase Articles**: [molavi.pro/notes/tm-neural-hud-video-studio](https://molavi.pro/notes/tm-neural-hud-video-studio)
- **Author & Strategy**: [Taghi Molavi](https://molavi.pro) | [Inten Asia](https://inten.asia)
