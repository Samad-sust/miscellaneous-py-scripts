import glob, os

# function that count lines in a single file
def lines_in_single_file(filename):
    
    if not os.path.isfile(filename):
        raise FileNotFoundError

    total_stomata = 0
    with open(filename) as f:
        total_stomata = len(f.readlines())
    return total_stomata

# get all the filename of the target directory
def get_all_file_names(directory, file_ext = "*"):
    all_filenames = glob.glob(directory + '/*.' + file_ext)
    return all_filenames

# count total number of lines of all the (text) files in the target directory
def count_stomata_in_dir(directory, file_ext="*"):
    # initialize the counter
    total_stom_in_dir = 0

    # get the name of the file to traverse given target folder and extension
    all_files = get_all_file_names(directory, file_ext)

    # check if there are some files or return warning if there is no file
    if len(all_files) <= 0:
        return 'No file found'

    # Traverse and count all the line in all files
    for f in all_files:
        
        # updating the counter for each iteration
        total_stom_in_dir += lines_in_single_file(f)
    
    # return the total number of lines in all files (final result)
    return total_stom_in_dir

# The target folder
dir_path = './labels'

print('total', count_stomata_in_dir(dir_path, 'txt'))