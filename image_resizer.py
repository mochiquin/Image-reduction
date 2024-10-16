import sys
import os
from PIL import Image

def resize_image(input_path, output_size=(1024, 1024)):
    try:
        # Open the image
        with Image.open(input_path) as img:
            # Get the original format
            original_format = img.format

            # Resize the image
            resized_img = img.resize(output_size, Image.LANCZOS)

            # Prepare the output filename
            filename = os.path.basename(input_path)
            name, ext = os.path.splitext(filename)
            output_filename = f"{name}_resized{ext}"
            output_path = os.path.join(os.path.dirname(sys.executable), output_filename)

            # Save the resized image
            resized_img.save(output_path, format=original_format)
            print(f"Resized image saved as {output_filename}")

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: Drag and drop an image file onto this program.")
        return

    input_path = sys.argv[1]
    
    # Check if the file is a JPG or PNG
    _, ext = os.path.splitext(input_path.lower())
    if ext not in ['.jpg', '.jpeg', '.png']:
        print("Only JPG and PNG files are supported.")
        return

    resize_image(input_path)

if __name__ == "__main__":
    main()
