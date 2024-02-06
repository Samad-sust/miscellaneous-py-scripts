# importing the libraries 
import glob
from PIL import Image

# the directory of the images to be resized 
image_dir = "png"

# the place where the imaged get saved 
target_dir = "jpg"

# entensions of the file to be look for in a certain directory
image_extension = ".png"

# Targer extension
target_ext = "jpg"

imagefiles = glob.glob( image_dir + '/*' + image_extension)


for i, image in enumerate(imagefiles):

    img = Image.open(image)
    
    print(f"{target_dir}/{image.split(sep='/')[-1].split(sep='.')[:-1][0]}")

    img.save(f"{target_dir}/{image.split(sep='/')[-1].split(sep='.')[:-1][0]}.{target_ext}", optimize=True, quality=70)