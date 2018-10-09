#include "opencv2/core/core.hpp"
#include "opencv2/contrib/contrib.hpp"
#include "opencv2/highgui/highgui.hpp"

#include <iostream>
#include <fstream>

using namespace cv;
using namespace std;

int main(int argc, const char *argv[]) {
    if (argc < 3) {
        cout << "Usage: "
        << argv[0]
        << " <csv_file> "
        << " <destination_file>"
        << endl;
        return 1;
    }

    string csvFile = string(argv[1]);
    string destinationFile = string(argv[2]);

    vector<Mat> images;
    vector<int> labels;

    setUseOptimized(true);

    setNumThreads(getNumberOfCPUs() + 1);

    try {
        std::ifstream file(csvFile.c_str(), ifstream::in);
        if (!file) {
            cerr << "{\"error\": \"No valid input file was given, please check the given CSV file\"}" << endl;
            return 1;
        }
        string line, path, classlabel;
        while (getline(file, line)) {
            stringstream liness(line);
            getline(liness, path, ';');
            getline(liness, classlabel);
            if(!path.empty() && !classlabel.empty()) {
                images.push_back(imread(path, 0));
                labels.push_back(atoi(classlabel.c_str()));
            }
        }
    } catch (cv::Exception& e) {
        cerr << "{\"error\": \"Error opening file '" << csvFile << "', reason: " << e.msg << "\"}" << endl;
        return 1;
    }

    Ptr<FaceRecognizer> model = createEigenFaceRecognizer();

    model->train(images, labels);
    model->save(destinationFile);

    cout << "{"
    << "\"file\": "
    << "\""
    << destinationFile
    << "\""
    << "}"
    << endl;

    return 0;
}
