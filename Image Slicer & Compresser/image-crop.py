# importing the libraries 
import glob
from PIL import Image

# the directory of the images to be resized 
image_dir = "/home/samad/Desktop/Species/gewa"

# the place where the imaged get saved 
cropped_image_dir = "/home/samad/Desktop/Species/gewa/cropped"

# entensions of the file to be look for in a certain directory
image_extension = ".jpg"

imagefiles = glob.glob( image_dir + '/*' + image_extension)

start_x = 0
start_y = 0
end_x   = 2448
end_y   = 2448

box = (start_x, start_y, end_x, end_y)

for i, image in enumerate(imagefiles):

    img = Image.open(image)
    cropped_img = img.crop(box)
    # cropped_img.save(f"{cropped_image_dir}/{image[-8:-4]}.jpg")
    
    cropped_img.save(f"{cropped_image_dir}/{image.split(sep='/')[-1]}", optimize=True, quality=30)