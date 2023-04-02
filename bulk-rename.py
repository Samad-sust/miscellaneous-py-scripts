# Import the required modules
import os

# Main function to rename the files in a direcory
def main():
    """
        This function is responsible for renaming all the files according to the specified patterns
    """
    # This should be the absolute path to the folder
    targer_folder = "/home/samad/Desktop/Images/A"

    # check its a directory 
    if not os.path.isdir(targer_folder):
        return "Not a directory!"

    # traverse through the folder and find the files
    for counter, filename in enumerate(os.listdir(targer_folder)):

        filename_prefix = "h"
        file_extension = filename.split(sep='.')[-1]

        # Target filename will be generated based upon the filename prefix and the extension
        target_filename = f"{filename_prefix}_{counter+1}.{file_extension}"

        # the source of the files inputted from the user
        source_destination = f"{targer_folder}/{filename}"
        target_destination = f"{targer_folder}/{target_filename}"

        # final renaming happens here
        os.rename(source_destination, target_destination)

if __name__ == "__main__":
    # calling the main function
    main()
