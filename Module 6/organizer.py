import os
import shutil

# Run only once after crawler has been ran

def move_files_in_groups(parent_dir, files_per_group=5):
    # Get a list of all files in the parent directory
    files = [f for f in os.listdir(parent_dir) if os.path.isfile(os.path.join(parent_dir, f))]
    
    # Determine the number of subdirectories needed
    num_subdirs = (len(files) + files_per_group - 1) // files_per_group  # Round up division

    # Loop through and move files to subdirectories
    for i in range(num_subdirs):
        # Create the subdirectory if it doesn't exist
        subdir_name = os.path.join(parent_dir, f"{i:04}")
        os.makedirs(subdir_name, exist_ok=True)
        
        # Get the files for this subdirectory
        start_index = i * files_per_group
        end_index = min(start_index + files_per_group, len(files))
        files_to_move = files[start_index:end_index]

        # Move the files to the subdirectory
        for file in files_to_move:
            src = os.path.join(parent_dir, file)
            dst = os.path.join(subdir_name, file)
            shutil.move(src, dst)
            
        print(f"Moved files to {subdir_name}")

# Example usage:
parent_directory = "./Module 6/data/"
move_files_in_groups(parent_directory, files_per_group=1000)
