#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QImage>

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow {
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void on_openImageButton_clicked();
    void on_upscaleButton_clicked();

private:
    Ui::MainWindow *ui;
    QImage currentImage;
    void displayImage(const QImage &image);
};

#endif // MAINWINDOW_H