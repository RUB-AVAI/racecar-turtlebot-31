from PIL import Image
import os

def png_to_jpg(path):
    # Ensure the path exists
    if not os.path.exists(path):
        print(f"Path '{path}' does not exist!")
        return

    # Iterate over all files in the directory
    for filename in os.listdir(path):
        if filename.endswith(".png"):
            # Open the PNG image
            img = Image.open(os.path.join(path, filename))
            
            # Remove alpha channel if present (JPG doesn't support transparency)
            if img.mode in ('RGBA', 'LA'):
                background = Image.new(img.mode[:-1], img.size, (255, 255, 255))
                background.paste(img, img.split()[-1])
                img = background

            # Save as JPG with the same name (but different extension)
            jpg_filename = os.path.join(path, os.path.splitext(filename)[0] + ".jpg")
            img.save(jpg_filename, "JPEG")

            print(f"Converted {filename} to {os.path.basename(jpg_filename)}")

# Example usage
png_to_jpg("cones-labeled/")
