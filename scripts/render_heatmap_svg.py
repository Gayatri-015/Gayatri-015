#!/usr/bin/env python3
"""
Render contribution heatmap from JSON data to animated SVG.
"""
import json
from datetime import datetime, timedelta
from pathlib import Path

# GitHub-style green palette
PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353", "#69f0a0"]

def render_heatmap_svg(data_file="data/contributions.json", output_file="contrib-heatmap.svg"):
    """
    Convert contribution JSON to an animated heatmap SVG.
    """
    
    # Load contribution data
    if not Path(data_file).exists():
        print(f"Error: {data_file} not found. Run fetch_contributions.py first.")
        return
    
    with open(data_file, 'r') as f:
        data = json.load(f)
    
    contributions = data['contributions']
    stats = data['stats']
    
    # Grid parameters
    cell_size = 14
    cell_spacing = 2
    weeks = 53
    days = 7
    
    margin = 40
    width = margin * 2 + weeks * (cell_size + cell_spacing)
    height = margin * 2 + days * (cell_size + cell_spacing) + 40
    
    svg_parts = [
        f'<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"',
        f'     width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        f'<style>',
        f'  @keyframes slideIn {{',
        f'    0% {{',
        f'      opacity: 0;',
        f'      transform: translate(-20px, -20px);',
        f'    }}',
        f'    100% {{',
        f'      opacity: 1;',
        f'      transform: translate(0, 0);',
        f'    }}',
        f'  }}',
        f'  .heatmap-cell {{',
        f'    animation: slideIn 0.6s ease-out forwards;',
        f'  }}',
        f'  .heatmap-text {{',
        f'    font-family: "Courier New", monospace;',
        f'    font-size: 12px;',
        f'    fill: #888888;',
        f'  }}',
        f'  .stat-text {{',
        f'    font-family: "Courier New", monospace;',
        f'    font-size: 13px;',
        f'    fill: #00d4ff;',
        f'    font-weight: bold;',
        f'  }}',
        f'</style>',
    ]
    
    # Title
    svg_parts.append(
        f'<text class="stat-text" x="{margin}" y="25">'
        f'🔥 {stats.get("total", 0)} contributions in the last year</text>'
    )
    
    # Day labels (Sun, Mon, Tue, Wed, Thu, Fri, Sat)
    day_labels = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    for day_idx, day_label in enumerate(day_labels):
        y = margin + day_idx * (cell_size + cell_spacing) + cell_size
        svg_parts.append(
            f'<text class="heatmap-text" x="10" y="{y}" text-anchor="end">{day_label}</text>'
        )
    
    # Month labels (approximate)
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    for i in range(13):
        x = margin + i * (weeks // 12) * (cell_size + cell_spacing)
        svg_parts.append(
            f'<text class="heatmap-text" x="{x}" y="{margin - 10}" text-anchor="start">'
            f'{months[i % 12]}</text>'
        )
    
    # Build calendar grid for last 53 weeks
    today = datetime.now().date()
    start_date = today - timedelta(days=365)
    
    # Start from Sunday
    while start_date.weekday() != 6:
        start_date -= timedelta(days=1)
    
    cell_index = 0
    for week_idx in range(weeks):
        for day_idx in range(days):
            current_date = start_date + timedelta(days=week_idx * 7 + day_idx)
            date_str = current_date.isoformat()
            
            # Get contribution level
            if date_str in contributions:
                level = contributions[date_str].get('level', 0)
                count = contributions[date_str].get('count', 0)
            else:
                level = 0
                count = 0
            
            # Color based on level
            color = PALETTE[min(level, len(PALETTE) - 1)]
            
            x = margin + week_idx * (cell_size + cell_spacing)
            y = margin + day_idx * (cell_size + cell_spacing)
            delay = (week_idx + day_idx) * 0.02  # Diagonal animation
            
            svg_parts.append(
                f'<rect class="heatmap-cell" x="{x}" y="{y}" '
                f'width="{cell_size}" height="{cell_size}" '
                f'fill="{color}" rx="3" '
                f'title="{count} contributions on {date_str}" '
                f'style="animation-delay: {delay}s;" />'
            )
    
    # Legend
    legend_y = height - 35
    svg_parts.append(f'<text class="heatmap-text" x="{margin}" y="{legend_y}">Less</text>')
    
    for level in range(len(PALETTE)):
        x = margin + 60 + level * (cell_size + 4)
        svg_parts.append(
            f'<rect x="{x}" y="{legend_y - cell_size}" '
            f'width="{cell_size}" height="{cell_size}" '
            f'fill="{PALETTE[level]}" rx="2" />'
        )
    
    svg_parts.append(
        f'<text class="heatmap-text" x="{margin + 60 + len(PALETTE) * (cell_size + 4) + 10}" '
        f'y="{legend_y}">More</text>'
    )
    
    svg_parts.append('</svg>')
    
    svg_content = '\n'.join(svg_parts)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(svg_content)
    
    print(f"Heatmap SVG saved to {output_file}")

if __name__ == "__main__":
    render_heatmap_svg()
