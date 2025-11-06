# QUICK IMAGE URLS - COPY/PASTE READY
## Sympathetic Magic Presentation

### IMAGE 01: Migrant Mother
**Best option for presentation (high-res, moderate file size):**
```
https://tile.loc.gov/storage-services/service/pnp/fsa/8b29000/8b29500/8b29516v.jpg
```
**Metadata URL for full attribution:**
```
https://www.loc.gov/pictures/item/2017762891/
```

---

### IMAGE 02: Mangaaka Power Figure (Nkisi)
**Best option for presentation (highest resolution):**
```
https://upload.wikimedia.org/wikipedia/commons/8/8f/WLA_metmuseum_Kongo_Power_Figure_2.jpg
```
**Alternative (good balance of quality/file size):**
```
https://upload.wikimedia.org/wikipedia/commons/f/fb/WLA_metmuseum_Kongo_Power_Figure_Nkisi_NKondi_Mangaaka.jpg
```
**Metadata URL for full attribution:**
```
https://www.metmuseum.org/art/collection/search/320053
```
**Source category (all versions):**
```
https://commons.wikimedia.org/wiki/Category:Mangaaka_(MET_2008.30)
```

---

### IMAGE 03: Digital Avatar Mockup
**Status:** CREATE YOURSELF (not sourced)
- Tool: Figma (free) https://www.figma.com/
- Size: 1200×900px, 4:3 ratio
- Process: Build mockup showing personal data flows

---

### IMAGES 04-06: Poor Image Series (Degradation stages)
**Status:** CREATE YOURSELF using public domain base
- Start with: Migrant Mother (LOC URL above) or any public domain image
- Stage 2: Resize 1080px, JPEG quality 60%
- Stage 3: Resize 720px, JPEG quality 30%
- Stage 4: Resize 480px, JPEG quality 15%

**Theory reference for presentation:**
- Hito Steyerl, "In Defense of the Poor Image" (2009)
- Lucie Chateau, "Alienated Aesthetics of Purposefully-Poor Images" (2022)

---

### IMAGE 07: Cultural Appropriation (Urban Outfitters/Navajo)
**Recommended visual:** Side-by-side of traditional design + commercial product

**Where to source traditional design:**
- Met Museum search "Navajo": https://www.metmuseum.org/art/collection
- Try specific search: "Navajo weaving" or "Navajo textile"

**Where to source commercial product image:**
- News coverage (VICE, The Week articles cited below have images)
- Wayback Machine for archived Urban Outfitters pages

**Documentation sources:**
- VICE article: https://vice.com/en/article/navajo-artist-urban-outfitters-lawsuit/
- The Week (controversies list): https://theweek.com/articles/480961/15-urban-outfitters-controversies
- Global Citizen: https://www.globalcitizen.org/en/content/urban-outfitters-cultural-appropriation-navajo-law/

---

## HTML Implementation Template

```html
<figure class="image-figure">
    <img 
        src="images/[filename].jpg" 
        alt="[Descriptive alt text here]"
        class="presentation-image"
    >
    <figcaption class="image-metadata">
        <strong>Source:</strong> [Institution]<br>
        <strong>Creator:</strong> [Artist/Photographer]<br>
        <strong>Date:</strong> [Year]<br>
        <strong>License:</strong> Public Domain<br>
        <strong>Accessed:</strong> 2025-11-06<br>
        <strong>URL:</strong> [Link to source]
    </figcaption>
</figure>
```

```css
.presentation-image {
    filter: grayscale(100%);
    max-width: 100%;
    height: auto;
}
```

---

## Priority Download Order

1. **Migrant Mother** (5 min) ← START HERE
   - URL: https://tile.loc.gov/storage-services/service/pnp/fsa/8b29000/8b29500/8b29516v.jpg
   
2. **Mangaaka** (1 min - just right-click save)
   - URL: https://upload.wikimedia.org/wikipedia/commons/8/8f/WLA_metmuseum_Kongo_Power_Figure_2.jpg

3. **Digital Avatar** (1-2 hours creating in Figma)

4. **Poor Image Series** (45 min - compression experiments)

5. **Cultural Appropriation case** (1-2 hours research + design)

---

**Everything else you need:** See complete `image-sourcing-urls.md` file

**Last updated:** 2025-11-06