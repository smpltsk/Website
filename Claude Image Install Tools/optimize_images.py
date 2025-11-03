#!/usr/bin/env python3
"""
SMPLTSK Image Optimizer
Helps you organize, rename, resize and optimize all images for your landing page
"""

import os
from PIL import Image
import sys

# Image specifications for each section
IMAGE_SPECS = {
    'hero': {
        'screenshot1.png': (1200, 800)
    },
    'steps': {
        'step1-see-it.png': (400, 220),
        'step2-mark-it.png': (400, 220),
        'step3-do-it.png': (400, 220)
    },
    'features': {
        'feature-visual-markers.png': (400, 280),
        'feature-pinpoint.png': (400, 280),
        'feature-sharing.png': (400, 280),
        'feature-progress.png': (400, 280),
        'feature-construction.png': (400, 280),
        'feature-savings.png': (400, 280)
    },
    'cases': {
        'case1-construction-original.png': (400, 350),
        'case1-construction-marked.png': (400, 350),
        'case1-construction-complete.png': (400, 350),
        'case2-engine-marked.png': (450, 350),
        'case2-engine-complete.png': (450, 350),
        'case3-floor-original.png': (400, 350),
        'case3-floor-marked.png': (400, 350),
        'case3-floor-description.png': (400, 350)
    }
}

def print_header():
    print("\n" + "="*60)
    print("  SMPLTSK IMAGE OPTIMIZER")
    print("  Organize, Resize & Optimize Your Landing Page Images")
    print("="*60 + "\n")

def print_checklist():
    """Print a checklist of all required images"""
    print("📋 REQUIRED IMAGES CHECKLIST:\n")
    
    total = 0
    for category, images in IMAGE_SPECS.items():
        print(f"\n{category.upper()}:")
        for filename, size in images.items():
            print(f"  ☐ {filename} ({size[0]}×{size[1]}px)")
            total += 1
    
    print(f"\n📊 Total images needed: {total}")
    print("="*60 + "\n")

def optimize_image(input_path, output_path, target_size):
    """Resize and optimize an image"""
    try:
        img = Image.open(input_path)
        
        # Convert RGBA to RGB if necessary (for JPEG)
        if img.mode == 'RGBA':
            background = Image.new('RGB', img.size, (255, 255, 255))
            background.paste(img, mask=img.split()[3])
            img = background
        
        # Calculate aspect ratio
        img_ratio = img.width / img.height
        target_ratio = target_size[0] / target_size[1]
        
        # Crop to match target ratio if needed
        if abs(img_ratio - target_ratio) > 0.01:
            if img_ratio > target_ratio:
                # Image is wider - crop width
                new_width = int(img.height * target_ratio)
                left = (img.width - new_width) // 2
                img = img.crop((left, 0, left + new_width, img.height))
            else:
                # Image is taller - crop height
                new_height = int(img.width / target_ratio)
                top = (img.height - new_height) // 2
                img = img.crop((0, top, img.width, top + new_height))
        
        # Resize to target size
        img = img.resize(target_size, Image.Resampling.LANCZOS)
        
        # Save optimized
        img.save(output_path, optimize=True, quality=85)
        
        # Get file sizes
        original_size = os.path.getsize(input_path) / 1024
        optimized_size = os.path.getsize(output_path) / 1024
        savings = ((original_size - optimized_size) / original_size) * 100
        
        return True, original_size, optimized_size, savings
    
    except Exception as e:
        return False, 0, 0, 0, str(e)

def interactive_mode():
    """Interactive mode to process images"""
    print("🔄 INTERACTIVE MODE\n")
    print("Place your screenshots in a folder, and I'll help you organize them.\n")
    
    input_folder = input("Enter the path to your screenshots folder (or press Enter for current folder): ").strip()
    if not input_folder:
        input_folder = "."
    
    if not os.path.exists(input_folder):
        print(f"❌ Error: Folder '{input_folder}' not found")
        return
    
    # Create output folder
    output_folder = os.path.join(input_folder, "optimized")
    os.makedirs(output_folder, exist_ok=True)
    
    # Get all image files
    image_files = [f for f in os.listdir(input_folder) 
                   if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    if not image_files:
        print("❌ No images found in the folder")
        return
    
    print(f"\n✅ Found {len(image_files)} images\n")
    print("Let's match them to the required filenames:\n")
    
    # Flatten all required images
    all_required = {}
    for category, images in IMAGE_SPECS.items():
        all_required.update(images)
    
    processed = 0
    total_original = 0
    total_optimized = 0
    
    for required_name, target_size in all_required.items():
        print(f"\n📸 {required_name} (needs to be {target_size[0]}×{target_size[1]}px)")
        print("Available images:")
        for i, img in enumerate(image_files, 1):
            print(f"  {i}. {img}")
        
        choice = input(f"Enter number (1-{len(image_files)}) or 's' to skip: ").strip().lower()
        
        if choice == 's':
            print("  ⏭️  Skipped")
            continue
        
        try:
            choice_idx = int(choice) - 1
            if 0 <= choice_idx < len(image_files):
                source_file = os.path.join(input_folder, image_files[choice_idx])
                output_file = os.path.join(output_folder, required_name)
                
                result = optimize_image(source_file, output_file, target_size)
                
                if result[0]:
                    _, orig_size, opt_size, savings = result
                    total_original += orig_size
                    total_optimized += opt_size
                    print(f"  ✅ Processed: {orig_size:.1f}KB → {opt_size:.1f}KB (saved {savings:.1f}%)")
                    processed += 1
                else:
                    print(f"  ❌ Error: {result[4]}")
            else:
                print("  ❌ Invalid choice")
        except ValueError:
            print("  ❌ Invalid input")
    
    print("\n" + "="*60)
    print(f"✅ COMPLETE!")
    print(f"Processed: {processed} images")
    print(f"Total size: {total_original:.1f}KB → {total_optimized:.1f}KB")
    print(f"Total savings: {total_original - total_optimized:.1f}KB ({((total_original - total_optimized)/total_original*100):.1f}%)")
    print(f"\n📁 Optimized images saved to: {output_folder}")
    print("="*60 + "\n")

def batch_mode():
    """Batch mode - assumes images are already named correctly"""
    print("🚀 BATCH MODE\n")
    print("This mode assumes your images are already named correctly.")
    print("It will resize and optimize them automatically.\n")
    
    input_folder = input("Enter folder with correctly named images: ").strip()
    if not input_folder:
        input_folder = "."
    
    if not os.path.exists(input_folder):
        print(f"❌ Error: Folder '{input_folder}' not found")
        return
    
    output_folder = os.path.join(input_folder, "optimized")
    os.makedirs(output_folder, exist_ok=True)
    
    all_required = {}
    for category, images in IMAGE_SPECS.items():
        all_required.update(images)
    
    processed = 0
    total_original = 0
    total_optimized = 0
    
    for required_name, target_size in all_required.items():
        source_file = os.path.join(input_folder, required_name)
        
        if not os.path.exists(source_file):
            print(f"⏭️  Skipping {required_name} (not found)")
            continue
        
        output_file = os.path.join(output_folder, required_name)
        result = optimize_image(source_file, output_file, target_size)
        
        if result[0]:
            _, orig_size, opt_size, savings = result
            total_original += orig_size
            total_optimized += opt_size
            print(f"✅ {required_name}: {orig_size:.1f}KB → {opt_size:.1f}KB (saved {savings:.1f}%)")
            processed += 1
        else:
            print(f"❌ {required_name}: Error - {result[4]}")
    
    print("\n" + "="*60)
    print(f"✅ COMPLETE!")
    print(f"Processed: {processed}/{len(all_required)} images")
    print(f"Total size: {total_original:.1f}KB → {total_optimized:.1f}KB")
    print(f"Total savings: {total_original - total_optimized:.1f}KB ({((total_original - total_optimized)/total_original*100):.1f}%)")
    print(f"\n📁 Optimized images saved to: {output_folder}")
    print("="*60 + "\n")

def main():
    print_header()
    
    print("Choose a mode:\n")
    print("  1. Show checklist of required images")
    print("  2. Interactive mode (I'll help you match images)")
    print("  3. Batch mode (images already named correctly)")
    print("  4. Exit\n")
    
    choice = input("Enter choice (1-4): ").strip()
    
    if choice == '1':
        print_checklist()
        input("\nPress Enter to continue...")
        main()
    elif choice == '2':
        interactive_mode()
    elif choice == '3':
        batch_mode()
    elif choice == '4':
        print("👋 Goodbye!\n")
        sys.exit(0)
    else:
        print("❌ Invalid choice")
        main()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!\n")
        sys.exit(0)
