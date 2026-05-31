import cv2
import numpy as np
from basicsr.archs.rrdbnet_arch import RRDBNet
from realesrgan import RealESRGANer

class RealESRGANUpscaler:
    def __init__(self, model_path: str = None, scale: int = 2):
        self.scale = scale
        model = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64, num_block=23, num_grow_ch=32, scale=scale)
        self.upsampler = RealESRGANer(
            scale=scale,
            model_path=model_path,
            model=model,
            tile=0,
            tile_pad=10,
            pre_pad=0,
            half=False
        )

    def upscale(self, input_path: str, output_path: str):
        img = cv2.imread(input_path, cv2.IMREAD_COLOR)
        if img is None:
            raise ValueError("Cannot read image")
        output, _ = self.upsampler.enhance(img, outscale=self.scale)
        cv2.imwrite(output_path, output)