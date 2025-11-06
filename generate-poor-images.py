#!/usr/bin/env python3
"""
Poor Image Degradation Generator
Creates 3 stages of progressive image compression to demonstrate Hito Steyerl's "poor image" concept
"""

import requests
from PIL import Image
from io import BytesIO
import os

# Configuration
SOURCE_URL = "https://tile.loc.gov/storage-services/service/pnp/fsa/8b29000/8b29500/8b29516v.jpg"
OUTPUT_DIR = "/Users/gaia/SYMPATHETIC MAGIC/images"

# Degradation stages
STAGES = [
    {
        'name': 'poor-image-stage-2-compression.jpg',
        'width': 1080,
        'quality': 60,
        'description': 'Stage 2: First Compression - Social media platform compression'
    },
    {
        'name': 'poor-image-stage-3-remix.jpg',
        'width': 720,
        'quality': 30,
        'description': 'Stage 3: Screenshot & Remix - Heavy compression with artifacts'
    },
    {
        'name': 'poor-image-stage-4-circulation.jpg',
        'width': 480,
        'quality': 15,
        'description': 'Stage 4: Infinite Circulation - Extreme degradation'
    }
]

def download_source_image(url):
    """Download the source image from URL"""
    print(f"Downloading source image from Library of Congress...")
    response = requests.get(url)
    response.raise_for_status()
    img = Image.open(BytesIO(response.content))
    print(f"✓ Downloaded: {img.size[0]}×{img.size[1]}px, mode: {img.mode}")
    return img

def create_degraded_image(source_img, width, quality, output_path):
    """Create a degraded version of the image"""
    # Calculate new height maintaining aspect ratio
    aspect_ratio = source_img.size[1] / source_img.size[0]
    height = int(width * aspect_ratio)
    
    # Resize image
    img = source_img.resize((width, height), Image.Resampling.LANCZOS)
    
    # Convert to RGB if needed (for JPEG compatibility)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    # Save with specified JPEG quality
    img.save(output_path, 'JPEG', quality=quality, optimize=False)
    
    file_size = os.path.getsize(output_path) / 1024  # KB
    print(f"  → {width}×{height}px, quality {quality}%, size: {file_size:.1f} KB")
    
    return img

def main():
    # Create output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"Output directory: {OUTPUT_DIR}\n")
    
    # Download source image
    try:
        source_img = download_source_image(SOURCE_URL)
    except Exception as e:
        print(f"✗ Error downloading source image: {e}")
        return
    
    # Save original for reference
    original_path = os.path.join(OUTPUT_DIR, 'migrant-mother-original.jpg')
    if source_img.mode != 'RGB':
        source_img_rgb = source_img.convert('RGB')
    else:
        source_img_rgb = source_img
    source_img_rgb.save(original_path, 'JPEG', quality=95)
    print(f"✓ Saved original: {original_path}\n")
    
    # Generate degraded stages
    print("Generating poor image degradation series...")
    print("=" * 60)
    
    current_img = source_img
    
    for stage in STAGES:
        print(f"\n{stage['description']}")
        output_path = os.path.join(OUTPUT_DIR, stage['name'])
        
        current_img = create_degraded_image(
            current_img, 
            stage['width'], 
            stage['quality'], 
            output_path
        )
        
        print(f"✓ Saved: {stage['name']}")
    
    print("\n" + "=" * 60)
    print("✓ Poor image degradation series complete!")
    print(f"\nFiles created in: {OUTPUT_DIR}")
    print("\nTheoretical framework:")
    print("  - Hito Steyerl: 'In Defense of the Poor Image' (2009)")
    print("  - Each stage demonstrates loss of quality, gain in circulation")
    print("  - Compression artifacts become aesthetic markers of virality")

if __name__ == "__main__":
    main()
