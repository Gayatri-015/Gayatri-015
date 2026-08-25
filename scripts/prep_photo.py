#!/usr/bin/env python3
"""
Prep photo: remove background, boost contrast, composite onto white.
"""
import sys
import cv2
import numpy as np
from rembg import remove
from PIL import Image

def prep_photo(input_path, output_path="source-prepped.png"):
    """
    1. Remove background with rembg
    2. Boost local contrast with CLAHE
    3. Composite onto pure white
    """
    print(f"Loading {input_path}...")
    img = cv2.imread(input_path)
    if img is None:
        print(f"Error: Could not load {input_path}")
        sys.exit(1)
    
    # Convert to PIL for rembg
    img_pil = Image.open(input_path)
    print("Removing background...")
    img_no_bg = remove(img_pil)
    
    # Convert back to OpenCV
    img_rgba = cv2.cvtColor(np.array(img_no_bg), cv2.COLOR_RGBA2BGRA)
    
    # Extract RGB and alpha
    img_bgr = img_rgba[:, :, :3]
    alpha = img_rgba[:, :, 3] / 255.0
    
    # Convert to grayscale
    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    
    # Apply CLAHE (Contrast Limited Adaptive Histogram Equalization)
    print("Boosting local contrast with CLAHE...")
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    gray = clahe.apply(gray)
    
    # Composite onto white: white * (1 - alpha) + subject * alpha
    print("Compositing onto white background...")
    white_bg = 255
    result = (white_bg * (1 - alpha[:, :, np.newaxis]) + 
              gray[:, :, np.newaxis] * alpha[:, :, np.newaxis]).astype(np.uint8)
    
    # Save
    cv2.imwrite(output_path, result)
    print(f"Saved prepped photo to {output_path}")

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "source-photo.jpg"
    prep_photo(input_file)
