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

# First pass: Gather all files by base name
for filename in os.listdir(target_directory):
    if filename.startswith("._"):
        continue  # Skip macOS metadata files
    
    file_path = os.path.join(target_directory, filename)
    
    # Check if it's a .wbfs, .wbf1, or .wbf2 file
    if os.path.isfile(file_path) and filename.lower().endswith(('.wbfs', '.wbf1', '.wbf2')):
        base_name, extension = os.path.splitext(filename)
        if base_name not in file_dict:
            file_dict[base_name] = []
        file_dict[base_name].append(filename)

# Process each set of files with the same base name
for base_name, files in file_dict.items():
    # Create a folder with the name of the base file (excluding the extension)
    folder_name = base_name
    folder_path = os.path.join(target_directory, folder_name)
    
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    for filename in files:
        file_path = os.path.join(target_directory, filename)
        
        # Move the file to the new folder
        new_file_path_in_folder = os.path.join(folder_path, filename)
        try:
            os.rename(file_path, new_file_path_in_folder)
        except FileNotFoundError:
            print(f'File not found: {file_path}. Skipping.')
            continue
        
        # Clean the filename
        cleaned_filename = clean_wbfs_filename(filename)
        if cleaned_filename != filename:
            # Rename the file inside the folder
            final_file_path = os.path.join(folder_path, cleaned_filename)
            try:
                os.rename(new_file_path_in_folder, final_file_path)
                print(f'Renamed: {file_path} -> {final_file_path}')
            except FileNotFoundError:
                print(f'File not found during renaming: {new_file_path_in_folder}. Skipping.')
        else:
            print(f'No change needed: {file_path}')
