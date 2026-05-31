import os
from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QPushButton,
                             QLabel, QFileDialog, QMessageBox, QProgressBar)
from PyQt5.QtCore import Qt
from upscaler import RealESRGANUpscaler

class UpscalerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Real-ESRGAN Upscaler Tool")
        self.setGeometry(100, 100, 500, 300)
        self.upscaler = RealESRGANUpscaler()
        self.input_path = None
        self.output_path = None
        self.init_ui()

    def init_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)

        self.label = QLabel("Select an image to upscale (2x)")
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        self.select_btn = QPushButton("Select Image")
        self.select_btn.clicked.connect(self.select_image)
        layout.addWidget(self.select_btn)

        self.upscale_btn = QPushButton("Upscale")
        self.upscale_btn.clicked.connect(self.upscale_image)
        self.upscale_btn.setEnabled(False)
        layout.addWidget(self.upscale_btn)

        self.progress = QProgressBar()
        self.progress.setValue(0)
        layout.addWidget(self.progress)

    def select_image(self):
        fname, _ = QFileDialog.getOpenFileName(self, "Open Image", "",
                                                "Images (*.png *.jpg *.jpeg *.bmp)")
        if fname:
            self.input_path = fname
            base, ext = os.path.splitext(fname)
            self.output_path = base + "_upscaled" + ext
            self.label.setText(f"Input: {os.path.basename(fname)}")
            self.upscale_btn.setEnabled(True)

    def upscale_image(self):
        if not self.input_path or not self.output_path:
            return
        self.progress.setValue(50)
        try:
            self.upscaler.upscale(self.input_path, self.output_path)
            self.progress.setValue(100)
            QMessageBox.information(self, "Done", f"Saved to {self.output_path}")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
            self.progress.setValue(0)
        finally:
            self.upscale_btn.setEnabled(False)
            self.input_path = None
            self.output_path = None
            self.label.setText("Select an image to upscale (2x)")