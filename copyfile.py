import glob, os, shutil

source_dir = '/home/samad/Documents/Abdus Samad/Computer Vision/Stomata and Density detection/Intensive Study/Dataset/all_images/val/images'

destination_dir = '/home/samad/Documents/Abdus Samad/Computer Vision/Stomata and Density detection/Intensive Study/Dataset/images/val/images'

files = glob.iglob(os.path.join(source_dir, "*.jpg"))

for file in files:
    if os.path.isfile(file):
        shutil.copy2(file, destination_dir)
        print(file)