from PIL import Image

def get_image_dimensions(image_path):
    img = Image.open(image_path)
    width, height = img.size
    print(f"Image dimensions (width x height): {width} x {height} pixels")

# Replace 'input_image.jpg' with the path to your image file
get_image_dimensions('ก_1.png')
