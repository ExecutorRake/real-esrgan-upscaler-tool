#ifndef UPSCALER_H
#define UPSCALER_H

#include <opencv2/opencv.hpp>

class Upscaler {
public:
    void process(const cv::Mat &input, cv::Mat &output, double scaleFactor);
};

#endif // UPSCALER_H