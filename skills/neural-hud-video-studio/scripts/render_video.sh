#!/usr/bin/env bash
set -euo pipefail

# Neural HUD Video Studio - Batch Render Wrapper
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_BIN="${PYTHON_BIN:-python3}"

REPO="${1:-neural-hud-video-studio}"
OUTPUT="${2:-output/${REPO}_hud.mp4}"
ASPECT="${3:-9:16}"
DURATION="${4:-6.0}"
FPS="${5:-24}"

echo "=========================================================="
echo "  TM Neural HUD Video Studio — Telemetry Video Renderer"
echo "=========================================================="
echo "Target Repo: $REPO"
echo "Output Path: $OUTPUT"
echo "Aspect:      $ASPECT"
echo "Duration:    ${DURATION}s"
echo "FPS:         $FPS"
echo "=========================================================="

"$PYTHON_BIN" "$SCRIPT_DIR/render_video.py" \
  --repo "$REPO" \
  --output "$OUTPUT" \
  --aspect "$ASPECT" \
  --duration "$DURATION" \
  --fps "$FPS"

echo "✓ Rendering complete: $OUTPUT"
