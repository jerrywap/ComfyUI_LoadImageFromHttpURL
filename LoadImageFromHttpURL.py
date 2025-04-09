import requests
from PIL import Image
import io
import numpy as np
import torch

class LoadImageFromHttpURL:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image_url": ("STRING", {
                    "default": "https://placehold.co/600x400/EEE/31343C"
                }),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "load_image"
    CATEGORY = "jerrywap/loaders"

    def load_image(self, image_url: str):
        try:
            response = requests.get(image_url)
            response.raise_for_status()
            image = Image.open(io.BytesIO(response.content)).convert("RGB")

            image_np = np.array(image).astype(np.float32) / 255.0
            image_tensor = torch.from_numpy(image_np).unsqueeze(0)

            return (image_tensor,)
        except Exception as e:
            print(f"Failed to load image from URL: {e}")
            return (torch.zeros(1, 512, 512, 3),)  # fallback black image
