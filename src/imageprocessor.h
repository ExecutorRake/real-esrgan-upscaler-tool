#ifndef IMAGEPROCESSOR_H
#define IMAGEPROCESSOR_H

#include <QImage>

class ImageProcessor {
public:
    QImage upscaleImage(const QImage &input, double scaleFactor);
};

#endif // IMAGEPROCESSOR_H