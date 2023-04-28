import os
import shutil

#  user select the directory to organize
directory = input("Enter the directory to organize: ")

# get a list of all files in the directory
files = os.listdir(directory)

# filter the type of file and type of directory
file_types = {
    '.jpg': 'image',
    '.jpeg': 'image',
    '.png': 'image',
    '.gif': 'image',
    '.bmp': 'image',
    '.tiff': 'image',
    '.avi': 'video',
    '.mp4': 'video',
    '.mkv': 'video',
    '.mov': 'video',
    '.pdf': 'document',
    '.doc': 'document',
    '.docx': 'document',
    '.txt': 'document',
    '.xlsx': 'document',
    '.pptx': 'document'
}

folder_names = {
    'image': 'Images',
    'video': 'Videos',
    'document': 'Documents'
}

# create new folders for each file type if they dont already exist
for folder_name in folder_names.values():
    folder_path = os.path.join(directory, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# move files to the folder based on the type
for file in files:
    file_path = os.path.join(directory, file)
    file_extension = os.path.splitext(file)[1]
    file_type = file_types.get(file_extension, None)
    if file_type:
        folder_name = folder_names[file_type]
        folder_path = os.path.join(directory, folder_name)
        new_file_path = os.path.join(folder_path, file)
        shutil.move(file_path, new_file_path)

print('Done, all files are organized!')
