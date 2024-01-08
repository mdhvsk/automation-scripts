import os
import glob
import shutil

downloads_path = os.path.expanduser('~/Downloads')

dmg_files = glob.glob(os.path.join(downloads_path, '*.dmg'))

print(downloads_path)
for file in dmg_files:
    try:
        os.remove(file)
        print(f"Deleted: {file}")
    except Exception as e:
        print(f"Error deleting {file}: {e}")

print("Deletion of dmg files complete.")

zip_files = glob.glob(os.path.join(downloads_path, '*.zip'))

print(downloads_path)
for file in zip_files:
    try:
        os.remove(file)
        print(f"Deleted: {file}")
    except Exception as e:
        print(f"Error deleting {file}: {e}")

print("Deletion of dmg files complete.")

pdf_files = glob.glob(os.path.join(downloads_path, '*.pdf'))
for file in pdf_files:
    if 'resume' in file.lower():
        try:
            os.remove(file)
            print(f"Deleted: {file}")
        except Exception as e:
            print(f"Error deleting {file}: {e}")


pictures_path = os.path.expanduser('~/Documents/Pictures')
file_types = ['*.jpeg', '*.png', '*.jpg']

for file_type in file_types:
    for file in glob.glob(os.path.join(downloads_path, file_type)):
        try:
            dest_path = os.path.join(pictures_path, os.path.basename(file))
            shutil.move(file, dest_path)
            print(f"Moved: {file} to {dest_path}")
        except Exception as e:
            print(f"Error moving {file}: {e}")
