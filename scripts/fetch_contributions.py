#!/usr/bin/env python3
"""
Fetch GitHub contributions data from public HTML (no token needed).
"""
import json
import sys
from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup
from pathlib import Path

def fetch_contributions(username="Gayatri-015", output_file="data/contributions.json"):
    """
    Scrape contributions from GitHub's public contribution calendar HTML.
    """
    url = f"https://github.com/users/{username}/contributions"
    
    print(f"Fetching contributions for {username}...")
    
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching contributions: {e}")
        sys.exit(1)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all day cells in the contribution graph
    # GitHub renders them as data-level="0-4" with data-date="YYYY-MM-DD"
    contribution_data = {}
    current_streak = 0
    longest_streak = 0
    total_contributions = 0
    
    # Parse each day cell
    for cell in soup.find_all('td', {'data-date': True}):
        date = cell.get('data-date')
        level = cell.get('data-level', '0')
        count = 0
        
        # Extract contribution count from title or aria-label
        title = cell.get('aria-label', '')
        if 'contributions' in title or 'contribution' in title:
            try:
                count_str = title.split()[0]
                count = int(count_str) if count_str.isdigit() else 0
            except:
                count = 0
        
        contribution_data[date] = {
            'count': count,
            'level': int(level) if level.isdigit() else 0
        }
        
        total_contributions += int(count)
        
        # Track streaks
        if count > 0:
            current_streak += 1
            longest_streak = max(longest_streak, current_streak)
        else:
            current_streak = 0
    
    # Calculate stats
    stats = {
        'total': total_contributions,
        'current_streak': current_streak,
        'longest_streak': longest_streak,
        'last_updated': datetime.now().isoformat(),
        'username': username,
    }
    
    output_data = {
        'contributions': contribution_data,
        'stats': stats,
    }
    
    # Ensure directory exists
    Path(output_file).parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_file, 'w') as f:
        json.dump(output_data, f, indent=2)
    
    print(f"Saved contribution data to {output_file}")
    print(f"Total contributions: {total_contributions}")
    print(f"Current streak: {current_streak}")
    print(f"Longest streak: {longest_streak}")

if __name__ == "__main__":
    username = sys.argv[1] if len(sys.argv) > 1 else "Gayatri-015"
    fetch_contributions(username)
