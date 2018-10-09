#!/bin/sh

gst-launch -e \
   # pipeline 1, input = /dev/video0, output = video0.ogg
   v4l2src device=/dev/video0 ! video/x-raw-yuv,format=\(fourcc\)YUY2,framerate=30/1,width=640,height=480 ! \
   ffmpegcolorspace ! \
   tee name="video0" ! \
   queue ! videorate ! video/x-raw-yuv ! \
   theoraenc bitrate=256 ! oggmux ! \
   filesink location=video0.ogg \

   # pipeline 2, input = /dev/video1, output = video1.ogg
   v4l2src device=/dev/video1 ! video/x-raw-yuv,format=\(fourcc\)YUY2,framerate=30/1,width=640,height=480 ! \
   ffmpegcolorspace ! \
   tee name="video1" ! \
   queue ! videorate ! video/x-raw-yuv ! \
   theoraenc bitrate=256 ! oggmux ! filesink location=video1.ogg \

   # pipeline 3, input = defaul audio device, output = audio.ogg
   alsasrc device=sysdefault:CARD=U0x46d0x825 ! \
   queue ! audioconvert ! vorbisenc ! oggmux ! filesink location=audio.ogg
