#include "opencv2/objdetect/objdetect.hpp"
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"

#include <iostream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;
using namespace cv;

int main(int argc, const char** argv)
{
    if (argc < 4) {
        printf("Usage: facedetect <image_file> <haarcascade_file> <output_folder>\n");
        return -1;
    }

    const char* image = argv[1];
    const char* haarcascade = argv[2];
    const char* output = argv[3];

    Mat im = imread(image, CV_LOAD_IMAGE_GRAYSCALE);

    if(im.rows == 0 || im.cols == 0) {
        printf("Invalid image file\n");
        return -1;
    }

    CascadeClassifier classifier;

    if(!classifier.load(haarcascade)) {
        printf("Haarcascade file not found");
        return -1;
    }

    vector<Rect> faces;

    double scaleFactor = 1.1;
    double minNeighbors = 2;
    double minSizeWidth = 30;
    double minSizeHeight = 30;
    double imageQuality = 15;
    double outputWidth = 92;
    double outputHeight = 112;

    classifier.detectMultiScale(im,
        faces,
        scaleFactor,
        minNeighbors,
        0|CV_HAAR_SCALE_IMAGE,
        Size(minSizeWidth, minSizeHeight)
    );

    vector<int> compressionParams;
    compressionParams.push_back(CV_IMWRITE_JPEG_QUALITY);
    compressionParams.push_back(imageQuality);

    for(size_t i = 0; i < faces.size(); i++)
    {
        int x1, y1, width, height;

        x1 = faces[i].x;
        y1 = faces[i].y;
        width = faces[i].width;
        height = faces[i].height;

        Rect rect(x1, y1, width, height);
        Mat cropped(im, rect);

        resize(cropped, cropped, Size(outputWidth, outputHeight));

        stringstream stream;
        stream << output << "/face_" << i << ".jpg";

        imwrite(stream.str(), cropped, compressionParams);
    }
    return 0;
}
