## GStreamer example of how record/stream two (or more) cameras in same time

#### Recording

```sh
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
```

#### Streaming

```sh
gst-launch-1.0 -e \
    # pipeline, input = /dev/video0, output = http://127.0.0.1:8080
    v4l2src device=/dev/video0 \
        ! videoconvert ! videoscale ! video/x-raw,width=640,height=480 \
        ! theoraenc bitrate=128 ! oggmux ! tcpserversink host=127.0.0.1 port=8080 \

    # pipeline, input = /dev/video1, output = http://127.0.0.1:8081
    v4l2src device=/dev/video1 \
        ! videoconvert ! videoscale ! video/x-raw,width=640,height=480 \
        ! theoraenc bitrate=128 ! oggmux ! tcpserversink host=127.0.0.1 port=8081
```
