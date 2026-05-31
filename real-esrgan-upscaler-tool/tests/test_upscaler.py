import unittest
import os
import tempfile
import cv2
import numpy as np
from upscaler import RealESRGANUpscaler

class TestUpscaler(unittest.TestCase):
    def setUp(self):
        self.upscaler = RealESRGANUpscaler(scale=2)
        self.temp_dir = tempfile.mkdtemp()

    def create_test_image(self, filename="test.png"):
        img = np.zeros((100, 100, 3), dtype=np.uint8)
        img[:] = (128, 128, 128)
        path = os.path.join(self.temp_dir, filename)
        cv2.imwrite(path, img)
        return path

    def test_upscale_shape(self):
        input_path = self.create_test_image()
        output_path = os.path.join(self.temp_dir, "output.png")
        self.upscaler.upscale(input_path, output_path)
        img_out = cv2.imread(output_path)
        self.assertEqual(img_out.shape, (200, 200, 3))

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            self.upscaler.upscale("nonexistent.png", "out.png")

    def tearDown(self):
        for f in os.listdir(self.temp_dir):
            os.remove(os.path.join(self.temp_dir, f))
        os.rmdir(self.temp_dir)

if __name__ == "__main__":
    unittest.main()