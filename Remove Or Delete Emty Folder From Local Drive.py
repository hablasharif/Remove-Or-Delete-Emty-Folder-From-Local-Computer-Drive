import os

def remove_empty_folders(path):
    for root, dirs, files in os.walk(path, topdown=False):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            try:
                if not os.listdir(dir_path):  # Check if the directory is empty
                    os.rmdir(dir_path)  # Remove the empty directory
                    print(f"Removed empty folder: {dir_path}")
            except Exception as e:
                print(f"Error removing {dir_path}: {e}")

# Specify the path to the C: drive
c_drive_path = "C:\\"

# Remove empty folders from the C: drive
remove_empty_folders(c_drive_path)
