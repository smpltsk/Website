# SMPLTSK Landing Page - Complete Setup Guide

## 🎯 Quick Start - What You Need to Do

You have:
- ✅ Screenshots taken
- ✅ Video recorded (no sound)

You need to:
1. Organize and optimize images
2. Add music/text to video
3. Upload everything to your website

---

## 📸 PART 1: Image Organization (3 Easy Options)

### **OPTION A: Browser Tool (Easiest - Recommended)**

1. **Open the image organizer:**
   - Double-click `image-organizer.html`
   - Opens in your web browser

2. **Upload all your screenshots:**
   - Drag all images into the upload zone
   - Or click to browse and select them

3. **Assign images:**
   - Click "Assign" on each slot
   - Type the number of the image you want to use
   - Image automatically resizes and crops to correct dimensions

4. **Download:**
   - Click "Download All Optimized"
   - All images download with correct names

5. **Upload to website:**
   - Place all downloaded images in the same folder as your HTML file

---

### **OPTION B: Python Script (If you prefer command line)**

1. **Install required library:**
   ```bash
   pip install Pillow
   ```

2. **Run the script:**
   ```bash
   python3 optimize_images.py
   ```

3. **Choose Interactive Mode (Option 2)**

4. **Follow the prompts:**
   - Tell it where your screenshots are
   - Match each required filename to your screenshots
   - Script resizes and optimizes automatically

5. **Get optimized images:**
   - Find them in the "optimized" subfolder
   - Upload to your website

---

### **OPTION C: Manual (If you want full control)**

Use any photo editor (even your phone):

**Required Sizes:**
- Hero: `screenshot1.png` (1200×800px)
- Steps: 3 images (400×220px each)
- Features: 6 images (400×280px each)  
- Cases: 8 images (400×350px or 450×350px)

**Online Tools:**
- ResizeImage.net
- Pixlr.com (free Photoshop alternative)
- Squoosh.app (Google's image optimizer)

---

## 🎬 PART 2: Video Processing (No Sound → Awesome Demo)

Since your video has no sound, you have 3 great options:

### **OPTION A: Add Background Music (Recommended)**

**Free Music Sources:**
- YouTube Audio Library (youtube.com/audiolibrary)
- Uppbeat.io (free tier)
- Pixabay Music (pixabay.com/music)

**Search for:** "upbeat tech" or "corporate motivational"

**Editing Tools:**

#### **On Phone:**
1. **CapCut (Free, iOS & Android)**
   - Import your screen recording
   - Tap "Audio" → "Sounds"
   - Choose upbeat background music
   - Adjust volume (music should be subtle)
   - Export in HD

2. **iMovie (iOS)**
   - Import video
   - Tap + → Audio → Soundtracks
   - Choose "Corporate" or "Upbeat"
   - Export → Save Video

#### **On Computer:**
1. **DaVinci Resolve (Free, Professional)**
   - Import video and music file
   - Drag both to timeline
   - Adjust music volume to -12dB
   - Export → YouTube 1080p preset

2. **Clipchamp (Free, Web-based)**
   - Upload video to clipchamp.com
   - Add music from their library
   - Export

---

### **OPTION B: Add Text Overlays**

Add text descriptions of what's happening:

**Use CapCut or DaVinci Resolve:**

**Text overlay script:**
```
0:00 - "Open SMPLTSK App"
0:03 - "Take or select a photo"
0:06 - "Tap to place marker #1"
0:10 - "Add task description"
0:15 - "Add more markers"
0:25 - "Send to your team"
0:30 - "Team receives task"
0:35 - "Tap marker to read"
0:40 - "Mark complete (turns green)"
0:50 - "All tasks done!"
```

**Font recommendations:**
- Inter (modern, clean)
- Helvetica/Arial (safe, readable)
- Montserrat (bold, professional)

**Text styling:**
- White text with black shadow/outline
- Bottom third of screen
- Large enough to read on mobile (36-48pt)

---

### **OPTION C: Both Music + Text (Best Result)**

Combine both approaches:
1. Add background music (subtle, 30-40% volume)
2. Add text overlays at key moments
3. This creates a professional, clear demo

---

## 📤 PART 3: Embedding Your Video

### **Step 1: Upload to YouTube**

1. **Go to:** youtube.com/upload
2. **Upload your edited video**
3. **Set details:**
   - Title: "SMPLTSK Demo - Visual Task Management"
   - Description: "See how SMPLTSK makes task communication simple"
   - Visibility: **Unlisted** (only people with link can view)

4. **Copy video ID:**
   - Your URL: `youtube.com/watch?v=ABC123XYZ`
   - Video ID: `ABC123XYZ`

### **Step 2: Update Your HTML**

1. **Open your HTML file**
2. **Find this section** (around line 1850):
   ```html
   <div class="video-placeholder">
       <div class="video-placeholder-icon">▶</div>
       <p>Video Coming Soon</p>
   </div>
   ```

3. **Replace with:**
   ```html
   <iframe 
       width="100%" 
       height="100%" 
       src="https://www.youtube.com/embed/ABC123XYZ?rel=0" 
       title="SMPLTSK Demo"
       frameborder="0" 
       allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
       allowfullscreen
       style="border-radius: 32px;">
   </iframe>
   ```

4. **Replace `ABC123XYZ`** with your actual video ID

### **Step 3: Test It**

1. Open your HTML file in a browser
2. Scroll to the video section
3. Video should play embedded in the page

---

## 🚀 PART 4: Final Checklist

### **Before Going Live:**

- [ ] All 18 images optimized and in place
- [ ] Video edited with music/text
- [ ] Video uploaded to YouTube (unlisted)
- [ ] Video embedded in HTML
- [ ] Test page in different browsers (Chrome, Safari, Firefox)
- [ ] Test on mobile device
- [ ] Check all images load correctly
- [ ] Video plays smoothly

### **Image Checklist:**
- [ ] screenshot1.png (hero)
- [ ] step1-see-it.png
- [ ] step2-mark-it.png
- [ ] step3-do-it.png
- [ ] feature-visual-markers.png
- [ ] feature-pinpoint.png
- [ ] feature-sharing.png
- [ ] feature-progress.png
- [ ] feature-construction.png
- [ ] feature-savings.png
- [ ] case1-construction-original.png
- [ ] case1-construction-marked.png
- [ ] case1-construction-complete.png
- [ ] case2-engine-marked.png
- [ ] case2-engine-complete.png
- [ ] case3-floor-original.png
- [ ] case3-floor-marked.png
- [ ] case3-floor-description.png

---

## 💡 Pro Tips

### **For Images:**
- Use real screenshots from actual app usage
- Make sure text in screenshots is readable
- Use consistent lighting/quality across all images
- Show actual app interface, not mockups

### **For Video:**
- Keep it under 90 seconds
- Show the complete workflow start-to-finish
- Use landscape orientation (not portrait)
- Make sure screen is clean (no notifications)
- Record in good lighting
- Use smooth, deliberate movements

### **For Music:**
- Choose upbeat but not distracting
- Volume should be background level (30-40%)
- Pick music that matches your brand (professional, tech)
- Avoid music with lyrics (distracting)

### **File Organization:**
```
your-website-folder/
├── index.html (your main page)
├── screenshot1.png
├── step1-see-it.png
├── step2-mark-it.png
├── step3-do-it.png
├── feature-visual-markers.png
├── feature-pinpoint.png
├── ... (all other images)
└── (video hosted on YouTube, not in folder)
```

---

## ⚡ Quick Reference Commands

### **If using Python script:**
```bash
# Install requirements
pip install Pillow

# Run script
python3 optimize_images.py

# Choose option 2 (Interactive mode)
```

### **If using browser tool:**
```
1. Double-click image-organizer.html
2. Drag images to upload zone
3. Assign each image
4. Download all
5. Upload to website folder
```

---

## 🆘 Troubleshooting

### **Images not showing:**
- Check filenames match exactly (case-sensitive)
- Ensure images are in same folder as HTML
- Try clearing browser cache (Ctrl+F5)

### **Video not playing:**
- Check YouTube video is "Unlisted" not "Private"
- Verify video ID is correct
- Test YouTube link directly first

### **Images look stretched:**
- Use the optimizer tools - they handle aspect ratios
- Don't manually resize without maintaining proportions

### **Page loads slowly:**
- Make sure images are optimized (under 200KB each)
- Video is hosted on YouTube (not self-hosted)
- Run images through TinyPNG.com for extra compression

---

## 📞 Next Steps

1. **Start with images** (use browser tool - easiest)
2. **Then do video** (add music in CapCut)
3. **Upload video** to YouTube
4. **Embed video** in HTML
5. **Test everything**
6. **Go live!**

---

## 🎉 You're Almost Done!

The hardest parts are already complete:
- ✅ Website designed
- ✅ Screenshots taken
- ✅ Video recorded

Now just:
1. Organize images (15 minutes)
2. Add music to video (10 minutes)
3. Upload and embed (5 minutes)

**Total time: ~30 minutes to completion!**

---

Need help with any step? Just ask! 🚀
