# IMAGE SOURCING CHECKLIST
## Quick Action List for Sympathetic Magic Presentation

**Files:** view-03.html, view-04.html  
**Total Images Needed:** 7 placeholders  
**Estimated Time:** 4-6 hours total  

---

## ✅ IMMEDIATE ACTIONS (Start Here)

### IMAGE 01: Migrant Mother ⭐ EASIEST
- [ ] Visit Library of Congress: https://www.loc.gov/pictures/item/2017762891/
- [ ] Download high-resolution JPG
- [ ] Rename: `migrant-mother-lange-1936.jpg`
- [ ] Save to: `/images/` folder
- [ ] Verify public domain status: ✅ FSA/OWI Collection
- [ ] **Time:** 5 minutes

**Metadata to copy:**
```
Photographer: Dorothea Lange
Subject: Florence Owens Thompson  
Date: March 1936
Source: Library of Congress, FSA/OWI Collection
License: Public Domain
Note: Subject later expressed regret about lack of informed consent
```

---

### IMAGE 02: Historical Voodoo Doll
- [ ] Search Metropolitan Museum: https://www.metmuseum.org/art/collection
  - Query: "nkondi Congo sculpture nails"
  - Filter: Public Domain/Open Access
- [ ] Alternative: British Museum collections
- [ ] Alternative: Wikimedia Commons ethnographic collections
- [ ] Select image with clear provenance
- [ ] Download high-res version
- [ ] Rename: `african-power-figure-nkondi.jpg`
- [ ] **Time:** 30-45 minutes

**Search tips:**
- Use term "nkondi" or "nkisi" (authentic names)
- Filter for "nail figure" or "power figure"
- Avoid sensationalized "voodoo doll" imagery
- Verify museum attribution and cultural context

**Required metadata:**
- Museum/collection name
- Object number/catalog ID
- Cultural origin (specific people group if known)
- Approximate date/period
- Current location

---

### IMAGE 03: Digital Avatar Mockup
- [ ] Option A: Design in Figma (recommended)
  - Create 1200x900px canvas (4:3 ratio)
  - Mock social media profile interface
  - Show: profile pic, bio fields, metadata tags
  - Include visual elements: platform logos, data connections
  - Export as JPG, convert to grayscale
  
- [ ] Option B: Screenshot + Heavy Editing
  - Use deactivated public account or test account
  - Screenshot profile page
  - Anonymize all identifying info in Photoshop
  - Add annotations showing data flow
  
- [ ] Rename: `digital-avatar-composite.jpg`
- [ ] **Time:** 1-2 hours

**Design elements to include:**
- Generic silhouette for profile photo
- Visible data fields (name, location, interests)
- Connection lines to other platforms
- Tracking pixel indicators
- Metadata tags visible
- "Shadow self" visual metaphor

---

### IMAGE 04-06: Poor Image Degradation Series
**Note:** This is ONE source image with THREE compression states

#### Step 1: Select Source Image
- [ ] Choose public domain image (historical photo or artwork)
- [ ] Alternatives:
  - Use "Migrant Mother" as source (creates thematic link)
  - Famous meme with documented circulation history
  - Public domain artwork from Met Museum
- [ ] Start with high-resolution version (2000px+ width)

#### Step 2: Create Stage 2 (First Compression)
- [ ] Open in Photoshop/GIMP
- [ ] Resize to 1080px width
- [ ] Save as JPEG, quality: 60%
- [ ] Rename: `poor-image-stage-2-compression.jpg`

#### Step 3: Create Stage 3 (Heavy Compression)
- [ ] Take Stage 2 image
- [ ] Resize to 720px width  
- [ ] Save as JPEG, quality: 30%
- [ ] Add slight screenshot artifact (optional: crop/resize again)
- [ ] Rename: `poor-image-stage-3-remix.jpg`

#### Step 4: Create Stage 4 (Extreme Degradation)
- [ ] Take Stage 3 image
- [ ] Resize to 480px width
- [ ] Save as JPEG, quality: 15%
- [ ] Additional step: Save, reopen, save again (compounds artifacts)
- [ ] Rename: `poor-image-stage-4-circulation.jpg`

- [ ] **Time:** 30-45 minutes for all three

**CSS note:** The blur filters are applied in the HTML, not the images themselves.

---

### IMAGE 07: Cultural Appropriation Example
- [ ] Research documented cases:
  - Urban Outfitters appropriation controversies
  - Fashion brand using indigenous designs without permission
  - Well-documented legal/public disputes
  
- [ ] Option A: Side-by-side composite
  - Left: Original cultural artifact (museum source)
  - Right: Commercial product appropriation
  - Center: Arrow showing extraction
  
- [ ] Option B: Before/after documentation
  - Community design tradition
  - Mass-market product using same design
  
- [ ] Ensure fair use justification (educational, transformative)
- [ ] Credit source community and advocates
- [ ] Rename: `cultural-appropriation-documented-case.jpg`
- [ ] **Time:** 1-2 hours (research-heavy)

**Ethical requirements:**
- Must be well-documented case with public record
- Include community response/advocacy
- Proper attribution to source culture
- Educational fair use justification

---

## 📋 TECHNICAL CHECKLIST

### Image Processing Standards:
- [ ] All images converted to grayscale
- [ ] Aspect ratio: 4:3 maintained
- [ ] Minimum width: 1200px (will scale responsively)
- [ ] Maximum file size: 500KB per image (optimize)
- [ ] Format: Progressive JPEG or optimized PNG
- [ ] File naming: lowercase, hyphens, descriptive

### Metadata Template (copy for each):
```html
<div class="image-metadata">
    Source: [Institution/Collection Name]<br>
    Creator: [Artist/Photographer]<br>
    Date: [Original date]<br>
    Accessed: 2025-11-06<br>
    License: [Public Domain / CC BY / Fair Use]<br>
    URL: [Direct source link]
</div>
```

---

## 🔄 IMPLEMENTATION WORKFLOW

### After Images Are Sourced:

1. **Create Images Folder**
   ```
   /SYMPATHETIC MAGIC/images/
   ```

2. **Place All Images in Folder**
   - migrant-mother-lange-1936.jpg
   - african-power-figure-nkondi.jpg
   - digital-avatar-composite.jpg
   - poor-image-stage-2-compression.jpg
   - poor-image-stage-3-remix.jpg
   - poor-image-stage-4-circulation.jpg
   - cultural-appropriation-documented-case.jpg

3. **Update view-04.html**
   - Replace each `<div class="image-placeholder">` with `<img src="images/[filename]">`
   - Add descriptive alt text for accessibility
   - Verify metadata div is complete and accurate

4. **Test**
   - [ ] Open view-04.html in browser
   - [ ] Verify all images load correctly
   - [ ] Check responsive behavior (resize window)
   - [ ] Validate alt text is descriptive
   - [ ] Confirm metadata is visible and accurate

---

## 🎯 PRIORITY LEVELS

### Must Have (Blocks completion):
1. ⭐ Migrant Mother (5 min) - START HERE
2. ⭐ Historical Voodoo Doll (45 min)
3. ⭐ Digital Avatar (1-2 hrs)

### Should Have (Strengthens argument):
4. ⭐ Poor Image Series (45 min)

### Could Have (Nice to have):
5. ⭕ Cultural Appropriation (1-2 hrs)

---

## 📚 QUICK REFERENCE URLS

**Direct Image Sources:**
- Migrant Mother: https://www.loc.gov/pictures/item/2017762891/
- Met Museum: https://www.metmuseum.org/art/collection
- British Museum: https://www.britishmuseum.org/collection
- Wikimedia Commons: https://commons.wikimedia.org/

**Design Tools:**
- Figma (free): https://www.figma.com/
- Photopea (free, web-based Photoshop): https://www.photopea.com/
- GIMP (free, open-source): https://www.gimp.org/

**License Verification:**
- Creative Commons Search: https://search.creativecommons.org/
- Public Domain Review: https://publicdomainreview.org/

---

## ⏱️ TIME ESTIMATES

| Task | Time | Difficulty |
|------|------|------------|
| Migrant Mother | 5 min | ⭐ Easy |
| Historical Object | 45 min | ⭐⭐ Moderate |
| Digital Avatar | 1-2 hrs | ⭐⭐⭐ Complex |
| Poor Image Series | 45 min | ⭐⭐ Moderate |
| Appropriation Case | 1-2 hrs | ⭐⭐⭐ Complex |
| Implementation | 30 min | ⭐ Easy |
| **TOTAL** | **4-6 hrs** | |

---

## ✅ COMPLETION CRITERIA

**Project is complete when:**
- [ ] All 7 image placeholders replaced with actual images
- [ ] All metadata sections filled with accurate information
- [ ] All images optimized for web (grayscale, <500KB)
- [ ] All images properly sourced with attribution
- [ ] Ethical checklist verified for each image
- [ ] HTML updated and tested in browser
- [ ] Responsive behavior verified on mobile/tablet/desktop
- [ ] Alt text provides descriptive context for accessibility

---

## 🚨 ETHICAL RED FLAGS

**Do NOT proceed with an image if:**
- ❌ License is unclear or contested
- ❌ Subject could be harmed by republication
- ❌ Cultural context is missing or unclear
- ❌ Source cannot be properly attributed
- ❌ Fair use justification is weak
- ❌ More recent permissions override historical public domain status

**When in doubt:**
- Use mockup instead of real photograph
- Choose different case study with clearer permissions
- Contact institution/rights holder for clarification
- Document decision-making process

---

## 📝 NOTES

Remember: This presentation practices what it preaches. Every image choice is an ethical decision. The metadata is not decorative—it demonstrates the `[trace]`, `[contextualize]`, and `[consent-seek]` morphisms in action.

Take time to verify sources properly. Rushing through licensing verification undermines the entire project's argument about responsible representation.

**Good luck with the image hunt! 🎯**

---

**Last Updated:** 2025-11-06  
**Status:** Ready for implementation  
**Next Action:** Start with Migrant Mother (easiest win)
