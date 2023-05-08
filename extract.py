import os
import re

# Set the folder path where the input files are located
folder_path = "libretro-core-info"

# Define a regular expression pattern to match the desired lines
pattern = r'firmware\d+_path\s*=\s*"(.*?)"'

# Get a sorted list of file names in the folder
file_names = sorted(os.listdir(folder_path))

# Loop over all files in the folder in alphabetical order
for filename in file_names:
    # Only process files with a .info extension (modify as needed)
    if filename.endswith(".info"):
        # Open the file and read its contents
        with open(os.path.join(folder_path, filename)) as file:
            content = file.read()

        # Use regex to find all matches of the pattern in the content
        matches = re.findall(pattern, content)

        # Extract the file names from the matched paths
        file_names = [os.path.basename(path) for path in matches]

        # Print the filename and list of matched filenames
        print(f"{filename}: {file_names}")
