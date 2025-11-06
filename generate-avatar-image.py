#!/usr/bin/env python3
"""
Digital Avatar Generator
Creates a mockup showing digital identity as sympathetic magic object
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Configuration
OUTPUT_DIR = "/Users/gaia/SYMPATHETIC MAGIC/images"
WIDTH = 1200
HEIGHT = 900
OUTPUT_FILE = "digital-avatar-composite.jpg"

def create_digital_avatar():
    """Generate digital avatar composite image"""
    
    # Create canvas
    img = Image.new('RGB', (WIDTH, HEIGHT), color='#ffffff')
    draw = ImageDraw.Draw(img)
    
    # Try to use system fonts, fall back to default if not available
    try:
        font_large = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 24)
        font_medium = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 16)
        font_small = ImageFont.truetype("/System/Library/Fonts/Courier.dfont", 12)
        font_tiny = ImageFont.truetype("/System/Library/Fonts/Courier.dfont", 10)
    except:
        print("⚠ Using default font (system fonts not found)")
        font_large = ImageFont.load_default()
        font_medium = ImageFont.load_default()
        font_small = ImageFont.load_default()
        font_tiny = ImageFont.load_default()
    
    # Header bar
    draw.rectangle([(0, 0), (WIDTH, 60)], fill='#000000')
    header_text = "DIGITAL IDENTITY AS SYMPATHETIC OBJECT"
    draw.text((WIDTH//2, 30), header_text, fill='#ffffff', font=font_medium, anchor="mm")
    
    # Profile box
    profile_x, profile_y = 80, 100
    profile_w, profile_h = 400, 480
    draw.rectangle(
        [(profile_x, profile_y), (profile_x + profile_w, profile_y + profile_h)],
        outline='#000000', width=3
    )
    
    # Profile circle
    circle_x = profile_x + profile_w//2
    circle_y = profile_y + 100
    circle_r = 75
    draw.ellipse(
        [(circle_x - circle_r, circle_y - circle_r), 
         (circle_x + circle_r, circle_y + circle_r)],
        fill='#666666', outline='#000000', width=4
    )
    draw.text((circle_x, circle_y), "👤", fill='#ffffff', font=font_large, anchor="mm")
    
    # Profile text
    y_offset = profile_y + 220
    draw.text((profile_x + profile_w//2, y_offset), "[USER PROFILE]", 
              fill='#000000', font=font_medium, anchor="mm")
    
    # Profile fields
    fields = [
        "NAME: AGGREGATED_IDENTITY_001",
        "EMAIL: user@████████.com",
        "LOCATION: 40.7128°N, 74.0060°W",
        "AGE: 32 [INFERRED]",
        "INTERESTS: AI ethics, photography",
        "BEHAVIORS: 847 tracked actions/day",
        "CONNECTIONS: 1,247 people",
        "STATUS: CONTINUOUSLY_MONITORED"
    ]
    
    y_pos = y_offset + 40
    for field in fields:
        # Field background
        draw.rectangle(
            [(profile_x + 20, y_pos - 5), (profile_x + profile_w - 20, y_pos + 20)],
            fill='#f0f0f0'
        )
        draw.line([(profile_x + 20, y_pos - 5), (profile_x + 20, y_pos + 20)], 
                  fill='#000000', width=4)
        draw.text((profile_x + 30, y_pos + 7), field, fill='#000000', font=font_tiny)
        y_pos += 30
    
    # Platform nodes
    platforms = [
        {"name": "FACEBOOK", "data": "2,847 data points", "pos": (920, 140)},
        {"name": "INSTAGRAM", "data": "1,293 images tracked", "pos": (940, 300)},
        {"name": "LINKEDIN", "data": "Career trajectory", "pos": (900, 460)},
        {"name": "TWITTER/X", "data": "Sentiment analyzed", "pos": (920, 620)}
    ]
    
    for platform in platforms:
        x, y = platform["pos"]
        # Box
        draw.rectangle([(x, y), (x + 140, y + 60)], 
                      outline='#000000', width=2, fill='#ffffff')
        # Shadow
        draw.rectangle([(x + 4, y + 4), (x + 144, y + 64)], 
                      outline='#cccccc', width=1)
        # Text
        draw.text((x + 70, y + 20), platform["name"], 
                 fill='#000000', font=font_small, anchor="mm")
        draw.text((x + 70, y + 40), platform["data"], 
                 fill='#666666', font=font_tiny, anchor="mm")
    
    # Connection lines
    connections = [
        (480, 220, 920, 160),
        (480, 320, 940, 320),
        (480, 420, 900, 480),
        (480, 520, 920, 640)
    ]
    
    for x1, y1, x2, y2 in connections:
        draw.line([(x1, y1), (x2, y2)], fill='#000000', width=2)
        # Arrow
        draw.text((x1 + (x2-x1)//2, y1 + (y2-y1)//2), "→", 
                 fill='#000000', font=font_medium)
    
    # Metadata tags
    tags = [
        ("COOKIES: 247 ACTIVE", (540, 70)),
        ("IP: 192.168.███.███", (600, 130)),
        ("DEVICE_ID: ████████", (560, 190)),
        ("LAST_ACTIVE: 14s ago", (140, 710)),
        ("CROSS-PLATFORM: SYNCED", (300, 750)),
        ("AD_PROFILE: SEGMENT_A47", (200, 790))
    ]
    
    for text, (x, y) in tags:
        bbox = draw.textbbox((x, y), text, font=font_tiny)
        draw.rectangle(
            [(bbox[0] - 5, bbox[1] - 3), (bbox[2] + 5, bbox[3] + 3)],
            fill='#000000'
        )
        draw.text((x, y), text, fill='#ffffff', font=font_tiny)
    
    # Tracking pixels
    pixels = [(540, 250), (580, 350), (560, 450)]
    for x, y in pixels:
        draw.ellipse([(x-4, y-4), (x+4, y+4)], fill='#000000')
    
    # Digital Shadow box
    shadow_x, shadow_y = 500, 700
    shadow_w, shadow_h = 380, 180
    
    # Dashed border simulation
    dash_length = 10
    for i in range(0, shadow_w, dash_length * 2):
        draw.line([(shadow_x + i, shadow_y), 
                   (shadow_x + min(i + dash_length, shadow_w), shadow_y)], 
                  fill='#000000', width=3)
        draw.line([(shadow_x + i, shadow_y + shadow_h), 
                   (shadow_x + min(i + dash_length, shadow_w), shadow_y + shadow_h)], 
                  fill='#000000', width=3)
    
    for i in range(0, shadow_h, dash_length * 2):
        draw.line([(shadow_x, shadow_y + i), 
                   (shadow_x, shadow_y + min(i + dash_length, shadow_h))], 
                  fill='#000000', width=3)
        draw.line([(shadow_x + shadow_w, shadow_y + i), 
                   (shadow_x + shadow_w, shadow_y + min(i + dash_length, shadow_h))], 
                  fill='#000000', width=3)
    
    # Shadow title
    draw.text((shadow_x + 20, shadow_y + 20), "DIGITAL SHADOW", 
             fill='#000000', font=font_small)
    
    # Shadow items
    shadow_items = [
        "→ Search history: 18,293 queries indexed",
        "→ Purchase data: $47,839 analyzed",
        "→ Location data: 847 daily pings",
        "→ Biometric: Face scan (89% confidence)",
        "→ Social graph: 3rd degree mapped",
        "→ Behavioral pattern: Predictive model active",
        "→ Data brokers: Sold to 23 entities"
    ]
    
    y_pos = shadow_y + 45
    for item in shadow_items:
        draw.text((shadow_x + 20, y_pos), item, fill='#000000', font=font_tiny)
        y_pos += 18
    
    # Convert to grayscale
    img = img.convert('L').convert('RGB')
    
    return img

def main():
    # Create output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"Output directory: {OUTPUT_DIR}\n")
    
    print("Generating Digital Avatar Composite...")
    print("=" * 60)
    
    img = create_digital_avatar()
    
    output_path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)
    img.save(output_path, 'JPEG', quality=90)
    
    file_size = os.path.getsize(output_path) / 1024  # KB
    print(f"✓ Created: {WIDTH}×{HEIGHT}px (4:3 ratio)")
    print(f"✓ Size: {file_size:.1f} KB")
    print(f"✓ Saved: {output_path}")
    
    print("\n" + "=" * 60)
    print("✓ Digital avatar mockup complete!")
    print("\nConcept:")
    print("  - Profile = digital voodoo doll representation")
    print("  - Data connections = contagion principle in action")
    print("  - Aggregation = transfer of essence across platforms")
    print("  - Tracking pixels = permanent trace markers")
    print("\nTheoretical framework:")
    print("  - Sympathetic magic: The digital profile IS the person")
    print("  - Contact magic: Data fragments retain connection to subject")
    print("  - Each platform connection extends the 'digital skin'")

if __name__ == "__main__":
    main()
