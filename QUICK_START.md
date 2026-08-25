# ⚡ Quick Reference: What to Customize

## 🎯 Priority 1: Essential Customizations

### 1️⃣ Add Your Photo
```bash
# Copy your photo to project root
source-photo.jpg

# Then run (requires pillow, numpy, cv2, rembg):
python scripts/prep_photo.py source-photo.jpg
python scripts/make_ascii_svg.py

# Result: avi-ascii.svg gets updated
```

### 2️⃣ Edit Info Card
**File**: `scripts/make_info_card.py` (lines 10-15)
```python
info_rows = [
    ("Now", "YOUR CURRENT ROLE"),           # Change this
    ("Prev", "YOUR PREVIOUS ROLE"),         # Change this
    ("Stack", "Python, JS, React, etc"),    # Change this
    ("Focus", "Your main focus area"),      # Change this
]
```

```bash
# Then regenerate:
python scripts/make_info_card.py
```

### 3️⃣ Update README.md Content

**Tech Stack** - Search for `skillicons.dev`:
```markdown
<!-- BEFORE -->
![](https://skillicons.dev/icons?i=python,java,js,html,css)

<!-- AFTER - Replace with your tech -->
![](https://skillicons.dev/icons?i=python,react,nodejs,typescript,docker)
```

**Projects** - Find and update each project:
```markdown
### 🤟 Your Project Name        ← Change this
Your project description       ← Change this
**Tech:** `tag1` `tag2`       ← Change these
```

**Social Links** - Search for `github.com/Gayatri-015`:
```markdown
<!-- Update to your profiles -->
[![GitHub](badge)](https://github.com/YOUR-USERNAME)
[![LinkedIn](badge)](https://linkedin.com/in/YOUR-USERNAME)
```

---

## 🎨 Priority 2: Nice-to-Have Customizations

### Color Scheme
**File**: `scripts/make_ascii_svg.py` (line 44)
```python
fill: #888888;  # Change hex color
```

**File**: `scripts/render_heatmap_svg.py` (line 8)
```python
PALETTE = [
    "#161b22", "#0e4429", "#006d32",  # Dark greens (GitHub default)
    "#26a641", "#39d353", "#69f0a0"   # Light greens
]
```

### Profile Quote/Footer
**File**: `README.md` (near end)
```markdown
╔════════════════════════════════════════╗
║       YOUR CUSTOM QUOTE HERE 💡        ║  ← Edit this
║       Your tagline or message 🚀       ║  ← Edit this
╚════════════════════════════════════════╝
```

---

## 📋 Files Breakdown

| File | What to Edit | Purpose |
|------|--------------|---------|
| `scripts/make_info_card.py` | `info_rows` list | Customize info card |
| `README.md` | Tech, projects, links | Main profile content |
| `scripts/make_ascii_svg.py` | `fill` color | ASCII art color |
| `scripts/render_heatmap_svg.py` | `PALETTE` | Heatmap colors |
| `source-photo.jpg` | (Add file) | Your profile photo |

---

## 🔄 Workflow After Customization

1. **Make changes** to the files above
2. **Regenerate SVGs** (if needed):
   ```bash
   python scripts/make_ascii_svg.py
   python scripts/make_info_card.py
   ```
3. **Commit**:
   ```bash
   git add .
   git commit -m "Personalize GitHub profile"
   ```
4. **Push**:
   ```bash
   git push
   ```
5. **Wait 5-10 minutes** for GitHub to refresh cache

---

## 📸 Photo Setup (Optional)

If you want the ASCII portrait from your photo:

1. **Prepare a photo**:
   - JPG or PNG format
   - Clear, well-lit face
   - Higher contrast = better ASCII
   - Recommended: 512x512 or larger

2. **Save as**: `source-photo.jpg` in project root

3. **Convert**:
   ```bash
   # First time: install heavy dependencies
   pip install pillow numpy opencv-python rembg
   
   # Then run prep
   python scripts/prep_photo.py source-photo.jpg
   python scripts/make_ascii_svg.py
   ```

4. **Commit new `avi-ascii.svg`**

---

## ✅ Minimal Customization (5 minutes)

1. Edit `scripts/make_info_card.py` - change 4 lines
2. Edit `README.md` - update your tech stack & social links
3. Commit & push

```bash
python scripts/make_info_card.py
git add scripts/make_info_card.py README.md
git commit -m "Customize profile"
git push
```

---

## 🚀 Full Customization (30 minutes)

1. Add photo → Generate ASCII
2. Customize info card
3. Update all README sections
4. Change colors if desired
5. Commit & push

---

**Already customized everything?** Your profile will now auto-update the contribution heatmap daily! 🎉
