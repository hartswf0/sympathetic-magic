# IMAGE LOCATIONS SUMMARY
## Quick Reference for view-03.html and view-04.html

**Date:** 2025-11-06  
**Purpose:** Map all image placeholders to their exact locations in the HTML files

---

## VIEW-03.HTML (ETH-REP-2025 / SYMPATHEIA PROTOCOL)

### Visual Elements Present:
1. **SVG Mission Patch** (Line 886-891)
   - Custom-created SVG badge with star design
   - Text: "SYMPATHEIA"
   - ✅ **COMPLETE** - No replacement needed

### Image Placeholders:
**NONE FOUND** - This file uses primarily text-based content with CSS styling.

### Potential Image Enhancement Opportunities:

#### Slide 3: Domain Memory (Lines 975-1025)
- **Case Study:** "Portraits and Dreams" - Wendy Ewald, 2000
- Could add: Sample photograph from project
- Source: https://wendyewald.com/portfolio/portraits-and-dreams/

#### Slide 4: Domain Identity (Lines 1028-1078)  
- **Case Study:** "Voice Casting Ethics"
- Could add: Animation production still, diverse voice cast photo
- Source: Industry documentation, fair use consideration

#### Slide 5: Domain Community (Lines 1080-1131)
- **Case Study:** "Stranger with a Camera" - Elizabeth Barret, 1999
- Could add: Documentary film still
- Source: https://www.pbs.org/pov/films/strangerwithacamera/

---

## VIEW-04.HTML (SYMPATHETIC MAGIC & MEDIA REPRESENTATION)

### Section 1: Foundational Concepts (Lines 616-672)

#### IMAGE PLACEHOLDER 01 (Lines 635-640)
```html
<div class="image-placeholder">
    [HISTORICAL VOODOO DOLL]<br>
    Carved wooden figure with nails/pins<br>
    Congo/West African origin, 19th century<br>
    [GRAYSCALE]
</div>
```
**Metadata Provided:**
- Source: Ethnographic Museum Collection
- Accessed: 2025-11-06
- License: Public Domain

**Action Required:** Source ethnographic object photograph

---

#### IMAGE PLACEHOLDER 02 (Lines 649-654)
```html
<div class="image-placeholder">
    [CONTEMPORARY DIGITAL AVATAR]<br>
    Social media profile screenshot<br>
    Profile picture + biographical data<br>
    [GRAYSCALE]
</div>
```
**Metadata Provided:**
- Source: Composite Example
- Accessed: 2025-11-06
- License: Fair Use (Educational)

**Action Required:** Create mockup or composite of social media profile

---

### Section 2: Photography & Capture (Lines 674-730)

#### IMAGE PLACEHOLDER 03 (Lines 692-698)
```html
<div class="image-placeholder">
    ["MIGRANT MOTHER"]<br>
    Dorothea Lange, 1936<br>
    Florence Owens Thompson<br>
    FSA documentation<br>
    [GRAYSCALE]
</div>
```
**Metadata Provided:**
- Photographer: Dorothea Lange
- Subject: Florence Owens Thompson
- Source: Library of Congress
- Accessed: 2025-11-06
- License: Public Domain
- **Note:** Subject later expressed regret at being photographed without understanding how widely image would circulate.

**Action Required:** Download from Library of Congress
**Direct URL:** https://www.loc.gov/pictures/item/2017762891/

---

### Section 4: Circulation & Poor Images (Lines 778-857)

#### IMAGE PLACEHOLDER 04 (Lines 805-808)
```html
<div class="image-placeholder" style="filter: blur(0.5px);">
    [IMAGE: First compression artifacts visible]<br>
    [JPEG blocking begins to appear]
</div>
```
**Purpose:** Stage 2 of degradation series
**Action Required:** Create compressed image showing initial quality loss

---

#### IMAGE PLACEHOLDER 05 (Lines 819-823)
```html
<div class="image-placeholder" style="filter: blur(1px); image-rendering: pixelated;">
    [IMAGE: Heavy compression]<br>
    [Pixelation visible]<br>
    [Original context lost]
</div>
```
**Purpose:** Stage 3 of degradation åseries
**Action Required:** Create heavily degraded image with visible artifacts

---

#### IMAGE PLACEHOLDER 06 (Lines 837-842)
```html
<div class="image-placeholder" style="filter: blur(2px); image-rendering: pixelated;">
    [IMAGE: Extreme degradation]<br>
    [Barely recognizable]<br>
    [Pure circulation]<br>
    [The poor image triumphant]
</div>
```
**Purpose:** Stage 4 - final degradation
**Action Required:** Create maximally compressed/degraded image

**Note:** These three images (04-06) should be the same source image at progressive compression levels to demonstrate Hito Steyerl's "poor image" concept.

---

### Section 5: Appropriation & Cultural Power (Lines 860-916)

#### IMAGE PLACEHOLDER 07 (Lines 869-874)
```html
<div class="image-placeholder">
    [APPROPRIATED DESIGN]<br>
    [Commercial product]<br>
    [No attribution]<br>
    [GRAYSCALE]
</div>
```
**Metadata Provided:**
- Source: Contemporary example
- Context: Cultural appropriation

**Action Required:** Source documented case of cultural appropriation or create educational composite

---

## IMAGE COUNT SUMMARY

### view-03.html:
- **Placeholders:** 0
- **Complete SVGs:** 1
- **Potential Additions:** 3 (case study images)

### view-04.html:
- **Placeholders:** 7 (6 unique images, 1 series of 3)
- **High Priority:** 3 (Historical object, Digital avatar, Migrant Mother)
- **Medium Priority:** 4 (Poor image series + Appropriation example)

### Total Work Required:
- **Essential:** 4 unique images
- **Series:** 1 source image with 3 degradation states
- **Optional Enhancement:** 3 case study images for view-03.html

---

## SOURCING WORKFLOW

### Immediate Actions:

1. **Migrant Mother** (Easiest)
   - ✅ Public domain confirmed
   - ✅ URL known: Library of Congress
   - ⏱️ Time: 5 minutes to download and verify metadata

2. **Historical Voodoo Doll** (Moderate)
   - Search Metropolitan Museum, British Museum collections
   - Filter for public domain/open access
   - ⏱️ Time: 30-60 minutes research

3. **Poor Image Series** (Moderate)
   - Select public domain source image
   - Create degradation series using image editor
   - ⏱️ Time: 45 minutes creation

4. **Digital Avatar Mockup** (Moderate-Complex)
   - Design composite interface in Figma/Sketch
   - Use generic placeholder data
   - ⏱️ Time: 1-2 hours design

5. **Appropriation Example** (Complex)
   - Research documented appropriation cases
   - Ensure ethical sourcing and fair use
   - ⏱️ Time: 1-2 hours research + verification

---

## TECHNICAL IMPLEMENTATION

### Once Images Are Sourced:

Replace placeholder div structure:
```html
<!-- OLD: -->
<div class="image-placeholder">
    [PLACEHOLDER TEXT]
</div>

<!-- NEW: -->
<img src="images/filename.jpg" alt="Descriptive alt text" style="width: 100%; height: auto;">
```

Maintain metadata structure:
```html
<div class="image-metadata">
    Source: [Institution]<br>
    Creator: [Name]<br>
    Date: [Date]<br>
    Accessed: [Date]<br>
    License: [License Type]<br>
    URL: [Source URL]
</div>
```

### File Organization:
```
/SYMPATHETIC MAGIC/
  ├── view-03.html
  ├── view-04.html
  ├── IMAGE-MANIFEST.md
  ├── IMAGE-LOCATIONS-SUMMARY.md
  └── images/
      ├── historical-voodoo-doll.jpg
      ├── digital-avatar-mockup.jpg
      ├── migrant-mother-lange.jpg
      ├── poor-image-stage-2.jpg
      ├── poor-image-stage-3.jpg
      ├── poor-image-stage-4.jpg
      └── cultural-appropriation-example.jpg
```

---

## NEXT STEPS

1. **Phase 1: Essential Images** (Priority: HIGH)
   - [ ] Download Migrant Mother from Library of Congress
   - [ ] Source historical voodoo doll from museum collection
   - [ ] Design digital avatar mockup

2. **Phase 2: Series Creation** (Priority: MEDIUM)
   - [ ] Select source image for poor image series
   - [ ] Create three degradation stages
   - [ ] Apply CSS filters as specified

3. **Phase 3: Case Study Enhancement** (Priority: LOW)
   - [ ] Research cultural appropriation documented cases
   - [ ] Create composite or source approved example
   - [ ] Add view-03.html case study images if desired

4. **Phase 4: Integration** (Priority: HIGH)
   - [ ] Update HTML with actual image paths
   - [ ] Verify all metadata is complete
   - [ ] Test responsive behavior
   - [ ] Validate alt text accessibility

---

## RESOURCES COMPILED

### Direct URLs for Immediate Use:

**Migrant Mother:**
- https://www.loc.gov/pictures/item/2017762891/
- https://www.loc.gov/resource/fsa.8b29516/

**Museum Collections (Public Domain Search):**
- https://www.metmuseum.org/art/collection
- https://www.britishmuseum.org/collection
- https://collections.artsmia.org/
- https://www.si.edu/search/collection-images

**Creative Commons Search:**
- https://search.creativecommons.org/
- https://commons.wikimedia.org/

**Mockup Tools:**
- Figma (free tier): https://www.figma.com/
- Photopea (free, web-based): https://www.photopea.com/

---

**STATUS:** Ready for implementation  
**ESTIMATED TOTAL TIME:** 4-6 hours for complete image sourcing and integration  
**PRIORITY:** View-04.html requires immediate attention (7 placeholders)

