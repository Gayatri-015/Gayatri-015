#!/usr/bin/env python3
"""
Generate neofetch-style info card SVG with fade-in animation.
"""
import os
from datetime import datetime

def create_info_card_svg(output_path="info-card.svg"):
    """
    Create an animated neofetch-style info card.
    """
    
    # Data for the card
    info_rows = [
        ("Now", "AI/ML + Full Stack Dev"),
        ("Prev", "Computer Science Student"),
        ("Stack", "Python, JS, React, TensorFlow"),
        ("Focus", "Sign Language Recognition"),
    ]
    
    row_height = 32
    card_width = 480
    card_height = len(info_rows) * row_height + 60
    
    svg_parts = [
        f'<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"',
        f'     width="{card_width}" height="{card_height}" viewBox="0 0 {card_width} {card_height}">',
        f'<style>',
        f'  @keyframes fadeInDown {{',
        f'    0% {{',
        f'      opacity: 0;',
        f'      transform: translateY(-10px);',
        f'    }}',
        f'    100% {{',
        f'      opacity: 1;',
        f'      transform: translateY(0);',
        f'    }}',
        f'  }}',
        f'  .card-line {{',
        f'    animation: fadeInDown 0.6s ease-out forwards;',
        f'  }}',
        f'  .card-label {{',
        f'    font-family: "Courier New", monospace;',
        f'    font-size: 14px;',
        f'    font-weight: bold;',
        f'    fill: #00d4ff;',
        f'  }}',
        f'  .card-value {{',
        f'    font-family: "Courier New", monospace;',
        f'    font-size: 14px;',
        f'    fill: #888888;',
        f'  }}',
        f'  .card-border {{',
        f'    stroke: #444444;',
        f'    stroke-width: 2;',
        f'    fill: none;',
        f'  }}',
        f'</style>',
        f'<rect class="card-border" x="4" y="4" width="{card_width - 8}" height="{card_height - 8}" rx="8" />',
    ]
    
    # Header
    svg_parts.append(
        f'<text class="card-line" x="16" y="28" style="animation-delay: 0s;"'
        f' style="font-family: Courier New, monospace; font-size: 14px; fill: #00d4ff; font-weight: bold;">'
        f'$ whoami</text>'
    )
    
    # Info rows with staggered animation
    for idx, (label, value) in enumerate(info_rows):
        y = 60 + idx * row_height
        delay = (idx + 1) * 0.15
        
        svg_parts.append(
            f'<g class="card-line" style="animation-delay: {delay}s;">'
            f'<text class="card-label" x="16" y="{y}">{label}:</text>'
            f'<text class="card-value" x="100" y="{y}">{value}</text>'
            f'</g>'
        )
    
    svg_parts.append('</svg>')
    
    svg_content = '\n'.join(svg_parts)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(svg_content)
    
    print(f"Info card SVG saved to {output_path}")

if __name__ == "__main__":
    create_info_card_svg()
