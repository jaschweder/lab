#!/bin/bash

gst-launch-1.0 \
    udpsrc port=5000 ! application/x-rtp,encoding-name=JPEG,payload=26 ! rtpjpegdepay ! jpegdec ! \
    videomixer name=mix \
    sink_0::xpos=0   sink_0::ypos=0 \
    sink_1::xpos=0   sink_1::ypos=240 \
    ! jpegenc ! rtpjpegpay ! udpsink host=127.0.0.1 port=5002 auto-multicast=true \
    udpsrc port=5001 ! application/x-rtp,encoding-name=JPEG,payload=26 ! rtpjpegdepay ! jpegdec ! mix.sink_1
