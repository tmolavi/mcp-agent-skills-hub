#!/usr/bin/env python3
"""
Audio Generator for Neural HUD Video Studio
Synthesizes a high-tech cyberpunk HUD telemetry soundtrack using FFmpeg.
"""
import sys
import subprocess
from pathlib import Path

def generate_hud_audio(duration: float, output_path: str):
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    fade_out_start = max(0.5, duration - 1.2)

    # Complex audio filter graph for futuristic telemetry ambience
    filter_complex = (
        f"aevalsrc=exprs='0.3*sin(2*PI*55*t)+0.15*sin(2*PI*110*t)':s=44100:d={duration}[sub];"
        f"anoisesrc=d={duration}:c=pink:r=44100,lowpass=f=260,volume=0.32[drone];"
        f"aevalsrc=exprs='0.18*sin(2*PI*920*t)*gt(mod(t,2.0),1.93)+0.12*sin(2*PI*1840*t)*gt(mod(t,4.0),3.95)':s=44100:d={duration}[beeps];"
        f"aevalsrc=exprs='0.08*sin(2*PI*(440+160*sin(2*PI*0.3*t))*t)':s=44100:d={duration}[sweep];"
        f"[sub][drone][beeps][sweep]amix=inputs=4:duration=first,"
        f"afade=t=in:ss=0:d=0.8,afade=t=out:st={fade_out_start}:d=1.2[out]"
    )

    cmd = [
        "ffmpeg", "-y",
        "-filter_complex", filter_complex,
        "-map", "[out]",
        "-t", str(duration),
        "-c:a", "aac",
        "-b:a", "192k",
        str(output_file)
    ]
    
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if res.returncode != 0:
        raise RuntimeError(f"FFmpeg audio generation failed: {res.stderr}")
    print(f"Generated HUD Audio: {output_file} ({duration}s)")
    return output_file

if __name__ == "__main__":
    dur = float(sys.argv[1]) if len(sys.argv) > 1 else 6.0
    out = sys.argv[2] if len(sys.argv) > 2 else "/tmp/test_hud_audio.aac"
    generate_hud_audio(dur, out)
