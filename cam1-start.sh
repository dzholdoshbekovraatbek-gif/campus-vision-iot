#!/usr/bin/env bash
# Test signal from FFmpeg to the local MediaMTX container
set -euo pipefail
ffmpeg -hide_banner -loglevel warning -re -f lavfi -i 'testsrc2=size=960x540:rate=15' -vf "drawtext=text='CAMPUS CAM / RAATBEK':fontsize=20:fontcolor=white:box=1:boxcolor=black@0.5:x=24:y=24" -c:v libx264 -preset ultrafast -tune zerolatency -pix_fmt yuv420p -f rtsp rtsp://127.0.0.1:8554/cam1
