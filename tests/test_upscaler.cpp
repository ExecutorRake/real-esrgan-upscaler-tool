#include "upscaler.h"
#include <opencv2/opencv.hpp>
#include <gtest/gtest.h>

TEST(UpscalerTest, BasicUpscale) {
    Upscaler upscaler;
    cv::Mat input(100, 100, CV_8UC3, cv::Scalar(255, 0, 0));
    cv::Mat output;

    upscaler.process(input, output, 2.0);

    EXPECT_EQ(output.cols, 200);
    EXPECT_EQ(output.rows, 200);
}

TEST(UpscalerTest, ZeroScaleFactor) {
    Upscaler upscaler;
    cv::Mat input(100, 100, CV_8UC3);
    cv::Mat output;

    upscaler.process(input, output, 0.0);

    EXPECT_TRUE(output.empty());
}