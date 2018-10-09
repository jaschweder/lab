#include "opencv2/core/core.hpp"
#include "opencv2/contrib/contrib.hpp"
#include "opencv2/highgui/highgui.hpp"

#include <iostream>
#include <fstream>

using namespace cv;
using namespace std;

int error(std::string message) {
    cerr << "{\"error\": \"" << message << "\"}" << endl;
    return 1;
}

int main(int argc, const char *argv[]) {
    if (argc < 3) {
        cout << "Usage: "
        << argv[0]
        << " <cache_file>"
        << " <test_img_file>"
        << " <number_of_components>"
        << " <threshold_limit>"
        << endl;
        return 1;
    }

    string cacheFile = string(argv[1]);
    string testFile = string(argv[2]);

    Mat testSample;

    try {
        testSample = imread(testFile, CV_LOAD_IMAGE_GRAYSCALE);
    } catch (int e) {
        return error("Can't load test file in " + cacheFile);
    }

    setUseOptimized(true);

    setNumThreads(getNumberOfCPUs() + 1);

    int numberComponents = 80;

    if (argc >= 4) {
        numberComponents = stoi(argv[3]);
    }

    double limit = 5000.0;

    if (argc >= 5) {
        limit = stof(argv[4]);
    }

    int testSampleLabel = -1;
    double testSampleConfidence = 0.0;

    Ptr<FaceRecognizer> model = createEigenFaceRecognizer(numberComponents, limit);

    try {
        model->load(cacheFile);
    } catch (int e) {
        return error("Can't load cache file in " + cacheFile);
    }

    try {
        model->predict(testSample, testSampleLabel, testSampleConfidence);
    } catch (int e) {
        return error("Can't call predict method");
    }
    cout << "{" << "\"numberComponents\": " << numberComponents << ","
    << "\"limit\": " << limit << ",";

    if (testSampleConfidence > limit) {
        testSampleLabel = -1;
        testSampleConfidence = limit;
    }

    cout << "\"label\": " << testSampleLabel << ","
    << "\"confidence\": " << testSampleConfidence
    << "}"
    << endl;
    return 0;
}
