#!/usr/bin/env python3
"""
Convert prepped grayscale image to self-typing ASCII art SVG.
"""
import sys
import cv2
import numpy as np
from pathlib import Path

# ASCII density ramp: bright (sparse) -> dark (dense)
RAMP = " .`:-=+*cs#%@"

def image_to_ascii_grid(image_path, width=100, height=53):
    """
    Convert grayscale image to ASCII character grid.
    """
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"Error: Could not load {image_path}")
        sys.exit(1)
    
    # Resize to target grid size
    img = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)
    
    # Normalize to 0-1
    img = img.astype(float) / 255.0
    
    # Map to ASCII ramp
    grid = []
    for row in img:
        ascii_row = ""
        for pixel in row:
            idx = int(pixel * (len(RAMP) - 1))
            ascii_row += RAMP[idx]
        grid.append(ascii_row)
    
    return grid

def create_typing_svg(grid, output_path="avi-ascii.svg"):
    """
    Create SVG with row-by-row typing animation (wipe left-to-right per row).
    """
    char_width = 8
    line_height = 16
    width = len(grid[0]) * char_width
    height = len(grid) * line_height
    
    # Font size that fits: roughly 1 char per 8px width, 16px line height
    font_size = 13
    
    svg_parts = [
        f'<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"',
        f'     width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        f'<style>',
        f'  @keyframes type-row {{',
        f'    0% {{ clip-path: polygon(0% 0%, 0% 100%, 0% 100%, 0% 0%); }}',
        f'    100% {{ clip-path: polygon(0% 0%, 100% 100%, 100% 100%, 0% 0%); }}',
        f'  }}',
        f'  .ascii-row {{',
        f'    animation: type-row 0.5s ease-out forwards;',
        f'    font-family: "Courier New", monospace;',
        f'    font-size: {font_size}px;',
        f'    fill: #888888;',
        f'    font-weight: normal;',
        f'    white-space: pre;',
        f'  }}',
        f'</style>',
    ]
    
    # Add each row with staggered animation delay
    for row_idx, row_text in enumerate(grid):
        y = (row_idx + 1) * line_height - 4
        delay = row_idx * 0.03  # Stagger each row by 30ms
        svg_parts.append(
            f'<text class="ascii-row" x="0" y="{y}" '
            f'style="animation-delay: {delay}s">{row_text}</text>'
        )
    
    svg_parts.append('</svg>')
    
    svg_content = '\n'.join(svg_parts)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(svg_content)
    
    print(f"ASCII SVG saved to {output_path}")

if __name__ == "__main__":
    input_file = "source-prepped.png"
    grid = image_to_ascii_grid(input_file)
    create_typing_svg(grid)
