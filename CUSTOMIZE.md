# 🎨 Customization Guide for Your Animated GitHub Profile

## Step 1: Add Your Photo to ASCII Art

### Requirements
- A clear, well-lit photo of yourself (JPG/PNG)
- Preferably with good contrast and a plain or blurred background

### Process
1. **Place your photo** in the repository root:
   ```bash
   source-photo.jpg
   ```

2. **Run the photo prep script** (first time only):
   ```bash
   python scripts/prep_photo.py source-photo.jpg
   ```
   This creates `source-prepped.png` with background removed and contrast boosted.

3. **Convert to ASCII SVG**:
   ```bash
   python scripts/make_ascii_svg.py
   ```
   This generates the animated `avi-ascii.svg`

4. **Commit and push**:
   ```bash
   git add avi-ascii.svg source-prepped.png
   git commit -m "Update ASCII portrait with custom photo"
   git push
   ```

---

## Step 2: Customize the Info Card

### Edit `scripts/make_info_card.py`

Find this section (~line 12):
```python
info_rows = [
    ("Now", "AI/ML + Full Stack Dev"),
    ("Prev", "Computer Science Student"),
    ("Stack", "Python, JS, React, TensorFlow"),
    ("Focus", "Sign Language Recognition"),
]
```

**Change to your information:**
```python
info_rows = [
    ("Now", "YOUR CURRENT ROLE"),
    ("Prev", "YOUR PREVIOUS ROLE"),
    ("Stack", "YOUR TECH STACK"),
    ("Focus", "YOUR MAIN FOCUS"),
]
```

### Example Customizations
- **Now**: "Senior Developer" or "ML Engineer"
- **Prev**: "Intern at Company" or "Student"
- **Stack**: "Python, Java, React, TensorFlow, AWS"
- **Focus**: "Computer Vision" or "Web Development"

### Regenerate the card:
```bash
python scripts/make_info_card.py
git add info-card.svg
git commit -m "Update info card"
git push
```

---

## Step 3: Update README.md Content

### Sections to Customize

1. **Tech Stack** (lines with skillicons):
   ```markdown
   ![](https://skillicons.dev/icons?i=python,java,js,html,css)
   ```
   Replace icons: `python,java,js,react,nodejs,docker,git,etc`

2. **Projects Section**:
   - Change project names and descriptions
   - Update tech tags
   - Add your actual project links

3. **Currently Learning**:
   - Update the skills you're learning
   - Add/remove topics based on your focus

4. **Social Links**:
   ```markdown
   [![LinkedIn](...)LinkedIn](https://www.linkedin.com/in/YOUR-USERNAME)
   [![Twitter](...)Twitter](https://twitter.com/YOUR-USERNAME)
   [![Portfolio](...)Portfolio](https://yourwebsite.com)
   ```

### Example Edit
```markdown
### 🤟 Indian Sign Language Recognition
→ Your Project Name

Research-oriented... → Your project description
```

---

## Step 4: Update Contribution Data (Automatic)

The contribution heatmap **updates automatically** every day at ~06:17 UTC via GitHub Actions.

**To manually update**:
```bash
python scripts/fetch_contributions.py
python scripts/render_heatmap_svg.py
git add data/contributions.json contrib-heatmap.svg
git commit -m "Update contributions"
git push
```

---

## Step 5: Personalize the Footer

In `README.md`, update the footer message:
```markdown
<p align="center">

```
╔════════════════════════════════════════╗
║                                        ║
║    "YOUR CUSTOM MOTIVATIONAL QUOTE"    ║
║                                        ║
║       Your tagline or closing 🚀       ║
║                                        ║
╚════════════════════════════════════════╝
```

---

## Step 6: Advanced Customizations

### Change ASCII Art Colors
In `scripts/make_ascii_svg.py`, modify line ~44:
```python
fill: #888888;  # Change to your color (hex code)
# Examples: #00d4ff (cyan), #00ff00 (green), #ff00ff (magenta)
```

### Change Heatmap Theme
In `scripts/render_heatmap_svg.py`, modify line ~8:
```python
PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353", "#69f0a0"]
# Current: GitHub green theme
# Try: ["#0d1117", "#161f2a", "#1f2d3d", "#2d424d", "#3d5a6d", "#4d7a8d"]
```

### Add More Projects
In `README.md`, duplicate a project section:
```markdown
### 🎯 Project Name
Description

**Tech:** `tag1` `tag2` `tag3`

---
```

---

## ⚡ Quick Customization Checklist

- [ ] Add `source-photo.jpg`
- [ ] Run `python scripts/prep_photo.py source-photo.jpg`
- [ ] Run `python scripts/make_ascii_svg.py`
- [ ] Edit `scripts/make_info_card.py` with your details
- [ ] Run `python scripts/make_info_card.py`
- [ ] Update README.md sections (projects, tech stack, links)
- [ ] Update social media links in footer
- [ ] Commit: `git add . && git commit -m "Personalize profile"`
- [ ] Push: `git push`

---

## 📝 Optional: Add More Sections

You can add new sections to README:

```markdown
## 🏆 Achievements
- Award 1
- Award 2

## 📖 Blog
- [Article Title](link)

## 🎓 Education
- Bachelor's in CS
```

---

## 🔄 Update Frequency

| File | How Often | Method |
|------|-----------|--------|
| `contrib-heatmap.svg` | Daily | Automatic (GitHub Actions) |
| `info-card.svg` | Manual | Run `make_info_card.py` |
| `avi-ascii.svg` | Manual | Run `make_ascii_svg.py` |
| `README.md` | As needed | Direct edit |

---

## 🐛 Troubleshooting

**Issue**: Script fails with encoding error
```bash
# Solution: Ensure UTF-8 encoding in scripts
python scripts/render_heatmap_svg.py
```

**Issue**: SVGs not showing on profile
- Clear GitHub cache (wait 5-10 minutes)
- Check file paths in README
- Verify SVG files exist in repo

**Issue**: Photo to ASCII looks bad
- Ensure photo has good contrast
- Try different lighting
- Use rembg's web version first: https://www.remove.bg

---

Need help with any specific customization? Just ask! 🚀
