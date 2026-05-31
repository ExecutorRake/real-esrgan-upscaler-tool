#include "imageprocessor.h"
#include "upscaler.h"
#include <opencv2/opencv.hpp>

QImage ImageProcessor::upscaleImage(const QImage &input, double scaleFactor) {
    cv::Mat cvImage(input.height(), input.width(), CV_8UC4, const_cast<uchar*>(input.bits()), input.bytesPerLine());
    cv::Mat upscaled;

    Upscaler upscaler;
    upscaler.process(cvImage, upscaled, scaleFactor);

    QImage result(upscaled.data, upscaled.cols, upscaled.rows, upscaled.step, QImage::Format_RGBA8888);
    return result.copy();
}