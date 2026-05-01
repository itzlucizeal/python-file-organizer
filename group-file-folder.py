import os
import shutil

path = '/mnt/c/Users/user/Downloads'
os.chdir(path)
list_files = os.listdir()

list_extensions = {
    '.pdf',
    '.mp4',
    '.docx',
    '.jfif',
    '.png',
    '.zip',
    '.jpg',
    '.pptx',
    '.exe',
    '.xlsx',
    '.webp',
    '.csv',
    '.save',
    '.msi',
    '.ini',
    '.mp3',
    '.gif',
    '.txt',
    '.rar',
    '.ttf',
    '.rmskin',
    '.eps',
    '.fig',
    '.py',
    '.css',
    '.excalidraw'
}

for file in list_files:
    if os.path.isdir(file): continue
    name, extension = os.path.splitext(file)
    extension = extension.lower()

    if extension in list_extensions:
        folder_name = f"{extension.split('.')[-1].capitalize()} Folder"
        dir_path = os.path.join(path, folder_name)
        file_path = os.path.join(path, file)
        destination_file = os.path.join(dir_path, file) # Full path of the future destination
        
        if not os.path.exists(dir_path):
            os.makedirs(dir_path, exist_ok=True)
            print(f"{folder_name} | Created in {dir_path}")

        if os.path.exists(destination_file):
            print(f"Skipping {file}: Already exists in {folder_name}")
            continue

        try:
            shutil.move(file_path, dir_path)
            print(f"{folder_name} | Success moving {file}")
        except PermissionError:
            print(f"Could not move {file}: File is in use by another program")
        except Exception as e:
            print(f"An unexpected error occurred with {file}: {e}")
