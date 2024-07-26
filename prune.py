import os
import re

# Function to clean the filename by keeping only the content within brackets before removing brackets
def clean_wbfs_filename(filename):
    base_name, extension = os.path.splitext(filename)
    
    # Check if the file has a relevant extension and the base name length is more than 6 characters
    if extension.lower() in ['.wbfs', '.wbf1', '.wbf2'] and len(base_name) > 6:
        # Extract content within brackets
        bracket_content = re.findall(r'\[([^\[\]]+)\]', base_name)
        if bracket_content:
            cleaned_name = ' '.join(bracket_content)
        else:
            cleaned_name = base_name
        cleaned_name = re.sub(r'[\[\](){}]', '', cleaned_name).strip()
        return cleaned_name + extension
    else:
        return filename

# Specify the target directory containing .wbfs, .wbf1, and .wbf2 files
target_directory = './wbfs'

# Dictionary to keep track of files by their base name
file_dict = {}
