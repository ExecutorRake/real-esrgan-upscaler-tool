#include "upscaler.h"

void Upscaler::process(const cv::Mat &input, cv::Mat &output, double scaleFactor) {
    cv::resize(input, output, cv::Size(), scaleFactor, scaleFactor, cv::INTER_CUBIC);
}