import os
import glob
from PIL import Image

def process_images(directory):
    for ext in ("*.png", "*.jpg", "*.jpeg"):
        for filepath in glob.glob(os.path.join(directory, "**", ext), recursive=True):
            print(f"Processing {filepath}")
            try:
                with Image.open(filepath) as img:
                    # Convert to RGB if needed (e.g. for saving JPEG/WebP)
                    if img.mode in ("RGBA", "P"):
                        img = img.convert("RGB")
                    
                    # Resize if width > 1200
                    if img.width > 1200:
                        new_height = int((1200 / img.width) * img.height)
                        img = img.resize((1200, new_height), Image.Resampling.LANCZOS)
                    
                    # Save as WebP
                    webp_path = os.path.splitext(filepath)[0] + ".webp"
                    img.save(webp_path, "WEBP", quality=80)
                    print(f"Saved {webp_path}")
            except Exception as e:
                print(f"Error processing {filepath}: {e}")

def update_references(directory):
    for root, _, files in os.walk(directory):
        if "node_modules" in root or ".firebase" in root:
            continue
        for file in files:
            if file.endswith(".html") or file.endswith(".css"):
                filepath = os.path.join(root, file)
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                
                # Simple replacement of extensions for known images
                new_content = content.replace(".png", ".webp").replace(".jpg", ".webp").replace(".jpeg", ".webp")
                
                if new_content != content:
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"Updated references in {filepath}")

if __name__ == "__main__":
    process_images("images")
    update_references(".")
    print("Done")
