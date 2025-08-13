import os
from PIL import Image

# --------- SETTINGS ---------
input_folder = "images"       # Folder with original images
output_folder = "resized"     # Folder to save resized images
new_size = (800, 600)         # Width x Height in pixels
output_format = "JPEG"        # "JPEG", "PNG", etc.
# ----------------------------

input_folder = r"C:\Users\Snehal Vagare\OneDrive\Desktop\skillbit project 3\Skillbit Project 7\images"


# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        img_path = os.path.join(input_folder, filename)
        
        try:
            with Image.open(img_path) as img:
                # Resize image
                resized_img = img.resize(new_size)
                
                # Create output path
                base_name = os.path.splitext(filename)[0]
                output_path = os.path.join(output_folder, f"{base_name}.{output_format.lower()}")
                
                # Save resized image
                resized_img.save(output_path, output_format)
                print(f"✅ Resized and saved: {output_path}")
        except Exception as e:
            print(f"❌ Error processing {filename}: {e}")

print("\n🎯 All images have been resized and saved in the output folder!")
