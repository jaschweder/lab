#!/bin/bash

set -xe

rm -f video.webm

gst-launch-1.0 -e \
    webmmux name=mux ! filesink location=./video.webm \
    udpsrc port=5000 \
    ! application/x-rtp,encoding-name=JPEG,payload=26 ! rtpjpegdepay ! jpegdec \
    ! videoconvert ! vp8enc threads=4 cq-level=10 dropframe-threshold=3 lag-in-frames=3 noise-sensitivity=0 target-bitrate=256000 ! queue ! mux.video_0 \
    alsasrc device=sysdefault:CARD=U0x46d0x825 ! queue ! audioconvert ! vorbisenc ! queue ! mux.audio_0
