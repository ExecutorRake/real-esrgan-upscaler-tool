#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "imageprocessor.h"
#include <QFileDialog>
#include <QMessageBox>

MainWindow::MainWindow(QWidget *parent) : QMainWindow(parent), ui(new Ui::MainWindow) {
    ui->setupUi(this);
    connect(ui->openImageButton, &QPushButton::clicked, this, &MainWindow::on_openImageButton_clicked);
    connect(ui->upscaleButton, &QPushButton::clicked, this, &MainWindow::on_upscaleButton_clicked);
}

MainWindow::~MainWindow() {
    delete ui;
}

void MainWindow::on_openImageButton_clicked() {
    QString fileName = QFileDialog::getOpenFileName(this, tr("Open Image"), "", tr("Image Files (*.png *.jpg *.bmp)"));
    if (!fileName.isEmpty()) {
        currentImage.load(fileName);
        displayImage(currentImage);
    }
}

void MainWindow::on_upscaleButton_clicked() {
    if (currentImage.isNull()) {
        QMessageBox::warning(this, tr("Error"), tr("No image loaded!"));
        return;
    }

    ImageProcessor processor;
    QImage upscaled = processor.upscaleImage(currentImage, 2.0);
    displayImage(upscaled);
}

void MainWindow::displayImage(const QImage &image) {
    ui->imageLabel->setPixmap(QPixmap::fromImage(image).scaled(
        ui->imageLabel->size(), Qt::KeepAspectRatio, Qt::SmoothTransformation));
}