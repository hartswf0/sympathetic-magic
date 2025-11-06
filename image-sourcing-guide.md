# IMAGE SOURCING GUIDE
## For view-03.html and view-04.html
**Compiled:** November 6, 2025  
**Status:** Complete Research & Collection Ready

---

## EXECUTIVE SUMMARY

Total images needed: **7 unique placeholders** (plus 1 series)
- High Priority: **4 images** (essential for core argument)
- Medium Priority: **3 images** (support degradation narrative)
- Optional Enhancement: **3 case study images** (view-03.html)

---

## PART 1: VIEW-04.HTML IMAGE REQUIREMENTS

### PLACEHOLDER 01: Historical Voodoo Doll
**Lines:** 635-640  
**Purpose:** Foundational Concepts section—sympathetic magic origins

#### Sourced Image: Nkisi Nkondi Power Figure
- **Description:** Carved wooden figure with embedded nails/metal from Kongo peoples, 19th century
- **Region:** West Africa/Democratic Republic of Congo
- **Cultural Context:** Spiritual/ritual power figure; represents sympathetic principle
- **Status:** ✅ FOUND - Multiple museum collections available
- **Recommended Source:** Metropolitan Museum of Art (Open Access Collection)
- **Search Query Used:** "historical voodoo doll West African Congo 19th century"
- **Image ID Reference:** [image:5] or [image:8] from search results
- **License:** Museum collection images typically public domain/CC0 when explicitly marked
- **Recommended Steps:**
  1. Visit Metropolitan Museum of Art collection search
  2. Search: "Nkisi Nkondi" or "power figure Kongo"
  3. Filter: Public Domain
  4. Download high-resolution JPEG
  5. Verify metadata before use

#### Alternative Collections:
- British Museum Online Collection
- Smithsonian Collections Search Center
- Artsmia (Minneapolis Institute of Art)

#### Implementation Note:
Replace placeholder with `<img>` tag. Include acquisition metadata in caption.

---

### PLACEHOLDER 02: Contemporary Digital Avatar
**Lines:** 649-654  
**Purpose:** Foundational Concepts section—modern sympathetic principle (digital identity)

#### Sourced Approach: Create Composite Mockup
- **Description:** Social media profile screenshot with biographical data
- **Best Method:** Design mockup using Figma or Photopea (web-based, zero-dependency)
- **Status:** ✅ READY TO CREATE

#### Design Specifications:
- **Format:** Grayscale composite
- **Elements to Include:**
  - Profile picture placeholder (circular frame)
  - Username/handle
  - Bio text (2-3 lines)
  - Follower count
  - Recent activity indicators
  - Visual style: Minimalist, educational
- **Dimensions:** 300px × 400px (responsive)
- **Tools Available:**
  - Figma (free tier, collaborative)
  - Photopea.com (free, browser-based, no registration)
  - GIMP (open source, desktop)

#### Template Content (suggested):
```
Username: @[GENERIC_HANDLE]
Bio: Creative professional | Digital identity | Online presence
Followers: 2.4K
Posts: 143
Following: 521
[Recent post thumbnail] [Recent post thumbnail] [Recent post thumbnail]
```

#### Implementation:
1. Open Photopea.com (no install needed)
2. Create 300×400px canvas
3. Design mockup with generic/anonymized data
4. Export as PNG or JPEG
5. Save to `/images/digital-avatar-mockup.jpg`

---

### PLACEHOLDER 03: "Migrant Mother" — Dorothea Lange, 1936
**Lines:** 692-698  
**Purpose:** Photography & Capture section—ethics of image without consent

#### Status: ✅ LOCATED & DOWNLOAD READY

#### Direct Download Links:
**Large JPEG (recommended for web):**
- URL: https://tile.loc.gov/storage-services/service/pnp/fsa/8b29000/8b29500/8b29516v.jpg
- Size: 353KB
- Resolution: Suitable for web display

**High-Resolution Options:**
- Medium JPEG: 75KB (https://tile.loc.gov/storage-services/service/pnp/fsa/8b29000/8b29500/8b29516r.jpg)
- Large TIFF: 55.8MB (https://tile.loc.gov/storage-services/master/pnp/fsa/8b29000/8b29500/8b29516u.tif)

#### Complete Metadata:
- **Photographer:** Dorothea Lange
- **Subject:** Florence Owens Thompson (later expressed regret about circulation)
- **Date:** March 1936
- **Location:** Nipomo, California (San Luis Obispo County)
- **Original:** Nitrate negative (4×5 in.)
- **Repository:** Library of Congress, Prints & Photographs Division
- **Collection:** Farm Security Administration/Office of War Information (FSA/OWI)
- **Call Number:** LC-USF34-009058-C [P&P]
- **Digital ID:** LC-DIG-fsa-8b29516
- **License:** Public Domain
- **Rights Advisory:** No known restrictions
- **Citation Format (Chicago):**
  > Lange, Dorothea, photographer. Destitute pea pickers in California. Mother of seven children. Age thirty-two. Nipomo, California. California San Luis Obispo County Nipomo United States, 1936. March. Photograph. https://www.loc.gov/item/2017762891/.

#### Important Contextual Notes:
- Subject Florence Owens Thompson was photographed WITHOUT explicit understanding of how widely the image would circulate
- Perfect case study for ethics of representation and circulation
- Negative was retouched in 1930s to remove thumb holding tent pole
- Unretouched version available if needed: https://hdl.loc.gov/loc.pnp/ppmsca.12883

#### Implementation:
1. Download large JPEG from URL above
2. Save to `/images/migrant-mother-lange.jpg`
3. Include complete metadata in caption
4. Link to Library of Congress entry in footer

---

### PLACEHOLDERS 04-06: Poor Image Series (Progressive Degradation)
**Lines:** 805-842  
**Purpose:** Circulation & Poor Images section—Hito Steyerl's theory

#### Concept: Three degradation stages of same source image
1. **Stage 2 (Light compression):** Initial JPEG blocking visible
2. **Stage 3 (Heavy compression):** Pixelation, context loss
3. **Stage 4 (Extreme degradation):** Barely recognizable, pure circulation

#### Current HTML Filters Applied:
- Stage 2: `filter: blur(0.5px);`
- Stage 3: `filter: blur(1px); image-rendering: pixelated;`
- Stage 4: `filter: blur(2px); image-rendering: pixelated;`

#### Recommended Source Image:
**Use Migrant Mother (Placeholder 03)** - Perfect thematic connection:
- Already in public domain
- Iconic photograph
- Strong emotional content that degrades meaningfully
- Reinforces ethical argument about circulation

#### Creation Workflow:

**Step 1: Obtain Source**
- Download original TIFF or large JPEG

**Step 2: Create Series (using any image editor)**

**Stage 2 - Initial Compression:**
- Export as JPEG at 85% quality
- Name: `poor-image-stage-2.jpg`

**Stage 3 - Heavy Compression:**
- Reduce resolution by 50% (e.g., 600×400 → 300×200)
- Export as JPEG at 40% quality
- Apply slight pixelation filter (2-3px)
- Name: `poor-image-stage-3.jpg`

**Stage 4 - Extreme Degradation:**
- Reduce resolution by 75% (e.g., 600×400 → 150×100)
- Export as JPEG at 15% quality
- Apply pixelation filter (4-5px)
- Name: `poor-image-stage-4.jpg`

#### Tools for Series Creation:
- **Photopea** (free, web-based): https://www.photopea.com/
- **GIMP** (open source): https://www.gimp.org/
- **ImageMagick** (command line, batch automation)
- **Python PIL/Pillow** (programmatic approach)

#### Python Script (Automated Approach):
```python
from PIL import Image, ImageFilter
import os

# Load original
img = Image.open('migrant-mother-lange.jpg')

# Stage 2: Light compression
stage2 = img.copy()
stage2.save('poor-image-stage-2.jpg', quality=85)

# Stage 3: Heavy compression + pixelation
stage3 = img.copy()
stage3 = stage3.resize((img.width//2, img.height//2), Image.LANCZOS)
stage3 = stage3.filter(ImageFilter.GaussianBlur(2))
stage3.save('poor-image-stage-3.jpg', quality=40)

# Stage 4: Extreme degradation
stage4 = img.copy()
stage4 = stage4.resize((img.width//4, img.height//4), Image.NEAREST)
stage4 = stage4.filter(ImageFilter.GaussianBlur(4))
stage4.save('poor-image-stage-4.jpg', quality=15)

print("✅ Poor image series created successfully")
```

#### Implementation Notes:
- Each stage should be visibly more degraded than the last
- Maintain thematic consistency with Steyerl's argument
- Test CSS filters in combination with actual image degradation
- Consider accessibility: Ensure alt text explains degradation purpose

---

### PLACEHOLDER 07: Cultural Appropriation Example
**Lines:** 869-874  
**Purpose:** Appropriation & Cultural Power section—case study

#### Status: ⚠️ REQUIRES CAREFUL SOURCING

#### Best Approach: Composite Educational Illustration
Rather than sourcing a specific controversial case, create educational graphic showing:
- Original design/cultural object
- Appropriated commercial version
- No attribution marker
- Side-by-side comparison

#### Recommended Subject Matter:
- Fashion brand appropriating Indigenous pattern
- Wellness brand using sacred symbol
- Food product using ethnic aesthetic without credit
- Technology company using cultural imagery

#### Design Specifications:
- Format: Comparison layout (original vs. appropriated)
- Style: Educational, neutral documentation
- Emphasis: Clear visual difference in context/framing
- Accessibility: Annotations explaining appropriation

#### Tools for Creation:
- Figma (collaborative, free tier)
- Canva (templates available)
- Photopea (web-based)

#### Creation Template:
```
LEFT SIDE (Original):
- [Cultural object/pattern image]
- Source: [Attribution]
- Context: Traditional/cultural use

RIGHT SIDE (Appropriated):
- [Commercial product]
- Source: [Brand name]
- No attribution visible

BOTTOM:
Arrow pointing right: "APPROPRIATION"
Annotation: "Design extracted from cultural context, 
rebranded without source acknowledgment"
```

#### Alternative: Use Documented Case Study
**If using specific case study**, ensure:
- Fair use criteria met
- Educational context clear
- No trademark infringement
- Artist/creator properly credited
- Cultural community not harmed

**Examples of documented appropriation:**
1. Fashion industry + Indigenous patterns (searchable, many documented cases)
2. Wellness industry + sacred symbols (extensively documented)
3. Food packaging + cultural aesthetics (commercial archive)

---

## PART 2: VIEW-03.HTML ENHANCEMENT OPPORTUNITIES

### Optional: Case Study Images

#### CASE STUDY 1: "Portraits and Dreams" — Wendy Ewald (2000)
**Reference:** Lines 975-1025  
**Purpose:** Domain Memory illustration

**Status:** ✅ FOUND
- Source: Wendy Ewald official website
- URL: https://wendyewald.com/portfolio/portraits-and-dreams/
- Description: Children's photography/storytelling project in Appalachia
- Image Found: Book cover [image:3] from search results
- Recommendation: Contact photographer or use book cover (likely fair use for educational documentation)

#### CASE STUDY 2: Voice Casting Ethics
**Reference:** Lines 1028-1078  
**Purpose:** Domain Identity illustration

**Status:** ✅ RESOURCES FOUND
- Image Found: Voice recording studio with diverse cast [image:10] from search results
- Alternative: Animation production still with diverse characters [image:13], [image:15]
- These demonstrate voice casting diversity visually
- License: Fair use for educational context
- Recommendation: Use studio image or animation still—both clearly show diversity in voice work

#### CASE STUDY 3: "Stranger with a Camera" — Elizabeth Barret (1999)
**Reference:** Lines 1080-1131  
**Purpose:** Domain Community illustration

**Status:** ✅ LOCATED
- Documentary film about subject reclaiming camera from photographer
- Source: PBS POV program
- URL: https://www.pbs.org/pov/films/strangerwithacamera/
- Recommendation: Check PBS licensing for educational use; request still or use documentary title card

---

## PART 3: IMPLEMENTATION WORKFLOW

### Phase 1: Immediate Priorities (2-3 hours)

#### Task 1.1: Download Migrant Mother
- [ ] Access: https://tile.loc.gov/storage-services/service/pnp/fsa/8b29000/8b29500/8b29516v.jpg
- [ ] Save as: `/images/migrant-mother-lange.jpg`
- [ ] Verify: File size ~353KB, resolution clear
- [ ] Metadata: Store in separate CSV or JSON

#### Task 1.2: Create Digital Avatar Mockup
- [ ] Open: Photopea.com
- [ ] Create: 300×400px canvas
- [ ] Design: Generic social media profile
- [ ] Export: `/images/digital-avatar-mockup.jpg`
- [ ] Time: ~30 minutes

#### Task 1.3: Source Historical Voodoo Doll
- [ ] Search: Metropolitan Museum, British Museum, Artsmia
- [ ] Filter: Public domain
- [ ] Download: High-resolution JPEG
- [ ] Save as: `/images/historical-voodoo-doll.jpg`
- [ ] Verify: Metadata completeness
- [ ] Time: ~30-45 minutes

### Phase 2: Series Creation (1-2 hours)

#### Task 2.1: Create Poor Image Series
- [ ] Obtain: Migrant Mother TIFF or large JPEG
- [ ] Generate: Stage 2, Stage 3, Stage 4 variants
- [ ] Save: `/images/poor-image-stage-*.jpg` (3 files)
- [ ] Test: CSS filters work correctly with degraded images
- [ ] Method: Photopea or Python script
- [ ] Time: ~45 minutes - 1 hour

### Phase 3: Additional Elements (1-2 hours)

#### Task 3.1: Create Appropriation Example
- [ ] Design: Comparison layout
- [ ] Method: Figma or Canva
- [ ] Save as: `/images/cultural-appropriation-example.jpg`
- [ ] Time: ~1-1.5 hours

#### Task 3.2: Optional Case Study Images
- [ ] Voice casting: Select best image [image:10] or [image:13]
- [ ] Portraits and Dreams: Contact or use book cover [image:3]
- [ ] Stranger with a Camera: Request from PBS or use title card
- [ ] Time: Varies by sourcing method

### Phase 4: HTML Integration (30 minutes)

#### Task 4.1: Update Image References
```html
<!-- Replace placeholder divs with: -->
<img src="images/filename.jpg" alt="[Descriptive alt text]" style="width: 100%; height: auto;">

<!-- Preserve metadata structure: -->
<div class="image-metadata">
    Source: [Institution]<br>
    Creator: [Name]<br>
    Date: [Date]<br>
    Accessed: 2025-11-06<br>
    License: [License Type]<br>
    URL: [Source URL]
</div>
```

#### Task 4.2: Verify Responsive Behavior
- [ ] Test on mobile (320px width)
- [ ] Test on tablet (768px width)
- [ ] Test on desktop (1920px width)
- [ ] Verify: Images scale correctly

---

## PART 4: FILE ORGANIZATION

### Directory Structure:
```
/SYMPATHETIC MAGIC/
├── view-03.html
├── view-04.html
├── css/
│   └── styles.css
├── js/
│   └── scripts.js
├── images/
│   ├── historical-voodoo-doll.jpg
│   ├── digital-avatar-mockup.jpg
│   ├── migrant-mother-lange.jpg
│   ├── poor-image-stage-2.jpg
│   ├── poor-image-stage-3.jpg
│   ├── poor-image-stage-4.jpg
│   ├── cultural-appropriation-example.jpg
│   ├── voice-casting-diversity.jpg (optional)
│   ├── portraits-and-dreams.jpg (optional)
│   └── stranger-with-camera.jpg (optional)
├── data/
│   ├── IMAGE-MANIFEST.md
│   ├── IMAGE-METADATA.json
│   └── image-sourcing-guide.md (this file)
└── README.md
```

### IMAGE-METADATA.json Template:
```json
{
  "images": [
    {
      "id": "historical-voodoo-doll",
      "filename": "historical-voodoo-doll.jpg",
      "placeholder": "01",
      "section": "Foundational Concepts",
      "source": "Metropolitan Museum of Art",
      "creator": "Kongo peoples (artist unknown)",
      "date": "19th century",
      "culture": "West African, Democratic Republic of Congo",
      "description": "Nkisi Nkondi power figure with embedded nails",
      "license": "Public Domain",
      "url": "[Insert museum collection URL]",
      "accessed": "2025-11-06",
      "altText": "Carved wooden power figure with embedded nails from Kongo peoples, 19th century"
    },
    {
      "id": "digital-avatar-mockup",
      "filename": "digital-avatar-mockup.jpg",
      "placeholder": "02",
      "section": "Foundational Concepts",
      "source": "Custom creation",
      "creator": "[Your name]",
      "date": "2025-11-06",
      "description": "Grayscale mockup of social media profile interface",
      "license": "Original Work",
      "altText": "Mock-up of generic social media profile showing biographical data and profile picture"
    },
    {
      "id": "migrant-mother",
      "filename": "migrant-mother-lange.jpg",
      "placeholder": "03",
      "section": "Photography & Capture",
      "source": "Library of Congress",
      "creator": "Dorothea Lange",
      "date": "1936-03",
      "subject": "Florence Owens Thompson",
      "location": "Nipomo, California",
      "description": "Iconic photograph of migrant worker mother and children",
      "license": "Public Domain",
      "callNumber": "LC-USF34-009058-C",
      "reproductionNumber": "LC-DIG-fsa-8b29516",
      "url": "https://www.loc.gov/item/2017762891/",
      "downloadUrl": "https://tile.loc.gov/storage-services/service/pnp/fsa/8b29000/8b29500/8b29516v.jpg",
      "accessed": "2025-11-06",
      "altText": "Black and white photograph of Florence Owens Thompson with two young children, 1936",
      "ethicalNote": "Subject expressed regret about image circulation without consent"
    },
    {
      "id": "poor-image-stage-2",
      "filename": "poor-image-stage-2.jpg",
      "placeholder": "04",
      "section": "Circulation & Poor Images",
      "source": "Derived from migrant-mother-lange.jpg",
      "degradationLevel": 2,
      "quality": "85%",
      "description": "Initial compression artifacts visible",
      "license": "Public Domain (derived)",
      "altText": "Migrant Mother photograph showing early JPEG compression artifacts"
    },
    {
      "id": "poor-image-stage-3",
      "filename": "poor-image-stage-3.jpg",
      "placeholder": "05",
      "section": "Circulation & Poor Images",
      "source": "Derived from migrant-mother-lange.jpg",
      "degradationLevel": 3,
      "quality": "40%",
      "resolution": "50% reduction",
      "description": "Heavy compression with visible pixelation",
      "license": "Public Domain (derived)",
      "altText": "Migrant Mother photograph heavily compressed with pixelation and quality loss"
    },
    {
      "id": "poor-image-stage-4",
      "filename": "poor-image-stage-4.jpg",
      "placeholder": "06",
      "section": "Circulation & Poor Images",
      "source": "Derived from migrant-mother-lange.jpg",
      "degradationLevel": 4,
      "quality": "15%",
      "resolution": "75% reduction",
      "description": "Extreme degradation, barely recognizable",
      "license": "Public Domain (derived)",
      "altText": "Migrant Mother photograph degraded to point of near unrecognizability, demonstrating poor image circulation"
    },
    {
      "id": "cultural-appropriation",
      "filename": "cultural-appropriation-example.jpg",
      "placeholder": "07",
      "section": "Appropriation & Cultural Power",
      "source": "Custom educational creation",
      "creator": "[Your name]",
      "date": "2025-11-06",
      "description": "Educational comparison showing original cultural design and appropriated commercial version",
      "license": "Original Work / Fair Use",
      "altText": "Educational diagram comparing original cultural design with appropriated commercial version without attribution"
    }
  ]
}
```

---

## PART 5: LEGAL & ETHICAL CONSIDERATIONS

### Public Domain Images (✅ CLEAR):
- **Migrant Mother**: US Government photograph (FSA/OWI) = Public Domain
- **Historical Voodoo Doll**: Museum collections explicitly marked as public domain/CC0
- **Derived images from Migrant Mother**: Retain public domain status

### Fair Use Images (⚠️ VERIFY):
- **Voice casting still**: Educational context supports fair use
- **Animation production still**: Animation studio/TV show stills often allow fair use
- **Documentary film stills**: PBS often allows educational use with attribution
- **Book covers**: Fair use for discussing the work

### Original/Created Images (✅ CLEAR):
- **Digital avatar mockup**: Your original creation
- **Appropriation example**: Your original creation
- **Poor image series**: Derived works of public domain image

### Ethical Checklist:
- [ ] All sources properly attributed
- [ ] Licenses verified and documented
- [ ] Alt text provided for accessibility
- [ ] Context prevents exploitation
- [ ] Educational purpose clearly stated
- [ ] Subject dignity respected (especially Migrant Mother note)

---

## PART 6: QUALITY ASSURANCE

### Before Uploading to Production:

#### Image Verification:
- [ ] File size reasonable for web (<500KB each)
- [ ] Resolution sufficient (min 300px width)
- [ ] Format optimized (JPEG for photographs, PNG for graphics)
- [ ] Color space: RGB (not CMYK)
- [ ] Metadata embedded where appropriate

#### Accessibility Check:
- [ ] Alt text descriptive and concise
- [ ] Alt text doesn't repeat caption
- [ ] Image purpose clear from context
- [ ] Decorative images have empty alt text

#### Responsive Design:
- [ ] Images display correctly at all breakpoints
- [ ] CSS filters applied correctly in view-04.html
- [ ] No distortion at any resolution
- [ ] Performance acceptable on mobile

#### Browser Compatibility:
- [ ] Test Chrome, Firefox, Safari
- [ ] Test on iOS and Android
- [ ] Verify JPEG support (universal)
- [ ] CSS filters supported (all modern browsers)

---

## PART 7: RESOURCES & TOOLS

### Image Sourcing:
- **Metropolitan Museum Open Access**: https://www.metmuseum.org/art/collection
- **British Museum Collections**: https://www.britishmuseum.org/collection
- **Artsmia Collections**: https://collections.artsmia.org/
- **Smithsonian Collections**: https://www.si.edu/search/collection-images
- **Commons Wikimedia**: https://commons.wikimedia.org/
- **Creative Commons Search**: https://search.creativecommons.org/

### Image Creation/Editing:
- **Photopea** (free, web-based): https://www.photopea.com/
- **Figma** (free tier): https://www.figma.com/
- **GIMP** (open source): https://www.gimp.org/
- **ImageMagick** (command line): https://imagemagick.org/

### Python Libraries (Automation):
```
Pillow/PIL - Image manipulation
ImageMagick binding - Advanced processing
OpenCV - Computer vision tasks
```

### Library of Congress:
- **Direct Access**: https://www.loc.gov/
- **FSA/OWI Collection**: http://hdl.loc.gov/loc.pnp/pp.fsaowi
- **Reproduductions/Duplication**: Library of Congress Duplication Services

---

## PART 8: TIMELINE & PRIORITY MATRIX

### By Urgency:
**CRITICAL (view-04.html placeholders):**
1. Migrant Mother (1 hour - direct download)
2. Historical Voodoo Doll (45 min - museum search)
3. Digital Avatar Mockup (30 min - creation)
4. Poor Image Series (1 hour - creation)

**IMPORTANT (view-04.html enhancement):**
5. Appropriation Example (1.5 hours - creation/research)

**OPTIONAL (view-03.html enhancement):**
6. Wendy Ewald case study (30 min - sourcing/contact)
7. Voice casting imagery (30 min - sourcing)
8. Stranger with a Camera (30 min - PBS licensing)

### Total Time Investment:
- **Core implementation**: 4-5 hours
- **With all enhancements**: 6-7 hours
- **HTML integration & testing**: 1-2 hours
- **Total project**: ~8 hours (well-distributed, not continuous)

---

## PART 9: NEXT IMMEDIATE STEPS

### Tomorrow's Action Items:
1. [ ] Download Migrant Mother from Library of Congress URL
2. [ ] Start digital avatar mockup design
3. [ ] Search museum collections for voodoo doll
4. [ ] Prepare poor image series (decide tool: Photopea vs Python)

### This Week:
5. [ ] Complete all image acquisition
6. [ ] Update HTML files with image references
7. [ ] Test responsive behavior
8. [ ] Verify all accessibility standards
9. [ ] Document complete sourcing in git commit

### Nice-to-Have (If Time Permits):
10. [ ] Create IMAGE-METADATA.json for future reference
11. [ ] Contact photographers for permissions (Elizabeth Barret, etc.)
12. [ ] Build gallery/slideshow for optional images

---

## CONTACT INFORMATION FOR PERMISSIONS

### Library of Congress - Prints & Photographs Division
- **Phone:** 202-707-6394
- **Website:** http://hdl.loc.gov/loc.pnp/pp.print
- **Hours:** 8:30-5:00 EST (M-F)

### PBS POV (Stranger with a Camera)
- **Email:** Submit via PBS Permissions portal
- **Website:** https://www.pbs.org/
- **Fair use likely applies** for educational documentary context

### Metropolitan Museum of Art
- **Permissions:** https://www.metmuseum.org/
- **Most collection images** marked CC0 (public domain)
- **No permissions needed** for open access images

---

**STATUS:** Ready for implementation  
**LAST UPDATED:** November 6, 2025  
**NEXT REVIEW:** After image download phase
