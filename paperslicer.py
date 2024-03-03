from PIL import Image, ImageFilter, ImageEnhance
import os

def replace_red_with_white(img, distance_threshold=150):
    data = img.getdata()

    def is_red(pixel):
        r, g, b = pixel
        #Calculate the distance from pure red (255, 0, 0)
        distance_from_red = ((r - 255) ** 2 + (g - 100) ** 2 + (b - 100) ** 2) ** 0.5
        return distance_from_red < distance_threshold

    new_data = [(255, 255, 255) if is_red(pixel) else pixel for pixel in data]

    img.putdata(new_data)
    return img

def make_brighter(image, factor=1.2):
    
    enhancer = ImageEnhance.Brightness(image)
    new_image = enhancer.enhance(factor)

    return new_image

def slice_a4_image(image_path, output_folder, square_size_pixels):
    img = Image.open(image_path)
    width, height = img.size
    
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)
    id = 1
    count = 0
    flag = 0
    for y in range(0, height, square_size_pixels):
        for x in range(0, width, square_size_pixels):
            flag += 1
            if flag%14 != 0 and count < 247:
                box = (x, y, x + square_size_pixels, y + square_size_pixels)
                cropped_img = img.crop(box)
                brighter_cropped_img = make_brighter(cropped_img, factor=1.5) 
                brighter_cropped_img = replace_red_with_white(brighter_cropped_img)
                #blurred_img = brighter_cropped_img.filter(ImageFilter.GaussianBlur(radius=0.5))
                
                # Save the images
                brighter_cropped_img.save(os.path.join(output_folder, f"เ-ะ_{id}.png"))
                #blurred_img.save(os.path.join(output_folder, f"เ-ะ_{id}.png"))
                id += 1
                count +=1
    print("Slice the input image into", count)
def get_image_dimensions(image_path):
    img = Image.open(image_path)
    width, height = img.size
    print(f"Input Image dimensions (width x height): {width} x {height} pixels")

#get_image_dimensions('1.jpg')
if __name__ == "__main__":
    slice_a4_image("1.jpg", "C:\\Users\\Jigsaw\\Desktop\\Paperslicer\\เ-ะ", 88)

