#!/bin/bash

set -xe

gst-launch-1.0 \
    v4l2src device=/dev/video8 ! videoconvert ! videoscale ! video/x-raw,format=I420,width=320,height=240,framerate=10/1 ! \
    videomixer name=mix \
    sink_0::xpos=0   sink_0::ypos=0 \
    sink_1::xpos=320   sink_1::ypos=0 \
    sink_2::xpos=0   sink_2::ypos=240 \
    sink_3::xpos=320   sink_3::ypos=240 \
    ! jpegenc quality=50 ! rtpjpegpay quality=50 ! udpsink host=127.0.0.1 port=5000 auto-multicast=true \
    v4l2src device=/dev/video6 ! videoconvert ! videoscale ! video/x-raw,format=I420,width=320,height=240,framerate=10/1 ! mix.sink_1 \
    v4l2src device=/dev/video4 ! videoconvert ! videoscale ! video/x-raw,format=I420,width=320,height=240,framerate=10/1 ! mix.sink_2 \
    v4l2src device=/dev/video2 ! videoconvert ! videoscale ! video/x-raw,format=I420,width=320,height=240,framerate=10/1 ! mix.sink_3
