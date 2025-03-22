import os

def get_folder_size(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(file_path)
    return total_size

def get_folders_sizes(directory):
    folder_sizes = {}
    for root, dirs, files in os.walk(directory):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            folder_sizes[dir_path] = get_folder_size(dir_path)
    return folder_sizes

directory = "./Module 6/data/"
folder_sizes = get_folders_sizes(directory)

for folder, size in folder_sizes.items():
    print(f"Folder: {folder}, Size: {size / (1024 * 1024):.2f} MB")
