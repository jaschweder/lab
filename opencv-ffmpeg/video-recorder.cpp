#include "opencv2/opencv.hpp"

#include <iostream>
#include <stdio.h>
#include <chrono>
#include <ctime>

using namespace std;
using namespace cv;

int main(int argc, const char** argv)
{
    VideoCapture video0;
    video0.set(CAP_PROP_FRAME_WIDTH, 640.0);
    video0.set(CAP_PROP_FRAME_HEIGHT, 480.0);
    video0.set(CAP_PROP_FPS, 25.0);
    video0.set(CAP_PROP_FOURCC, CV_FOURCC('X','2', '6', '4'));
    video0.set(CAP_PROP_AUTOFOCUS, 1);
    video0.set(CAP_PROP_CONVERT_RGB, 1);
    video0.open("/dev/video2");

    if (!video0.isOpened()) {
        cerr << "ERROR: Unable to open device" << endl;
        return 1;
    }

    VideoCapture video1;
    video1.set(CAP_PROP_FRAME_WIDTH, 640.0);
    video1.set(CAP_PROP_FRAME_HEIGHT, 480.0);
    video1.set(CAP_PROP_FPS, 25.0);
    video1.set(CAP_PROP_FOURCC, CV_FOURCC('X','2', '6', '4'));
    video1.set(CAP_PROP_AUTOFOCUS, 1);
    video1.set(CAP_PROP_CONVERT_RGB, 1);
    video1.open("/dev/video3");

    if (!video1.isOpened()) {
        cerr << "ERROR: Unable to open device" << endl;
        return 1;
    }

    Size resolution = Size(640, 480);
    bool isColor = true;
    int codec = CV_FOURCC('M', 'J', 'P', 'G');
    double fps = 25.0;
    string filename = "./out.mkv";
    string filename2 = "./out2.mkv";

    VideoWriter writer;
    writer.open(filename, codec, fps, resolution);

    if (!writer.isOpened()) {
        cerr << "ERROR: Could not open output file for write" << endl;
        return 1;
    }

    VideoWriter writer2;
    writer2.open(filename2, codec, fps, resolution);

    if (!writer2.isOpened()) {
        cerr << "ERROR: Could not open output file for write" << endl;
        return 1;
    }

    unsigned int totalFrames = 30 * fps;
    unsigned int qtdFrames = 0;

    Mat frame;
    Mat frame2;

    cout << "Start recording.." << endl;
    for(;;) {
        video0.read(frame);
        writer.write(frame);

        video1.read(frame2);
        writer2.write(frame2);

        qtdFrames++;

        if (qtdFrames == totalFrames) {
            break;
        }
    }
    cout << "End recording" << endl;

    return 0;
}
