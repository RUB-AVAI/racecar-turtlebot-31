import os
import shutil

def sort_files(base_path):
    image_exts = ['.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff']
    text_exts = ['.txt']

    # Create subfolders if they don't exist
    images_path = os.path.join(base_path, 'images')
    labels_path = os.path.join(base_path, 'labels')
    if not os.path.exists(images_path):
        os.mkdir(images_path)
    if not os.path.exists(labels_path):
        os.mkdir(labels_path)

    for filename in os.listdir(base_path):
        file_path = os.path.join(base_path, filename)
        # Only move files, skip directories
        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1]
            # Move images to the 'images' subfolder
            if ext.lower() in image_exts:
                shutil.move(file_path, os.path.join(images_path, filename))
            # Move text files to the 'labels' subfolder
            elif ext.lower() in text_exts:
                shutil.move(file_path, os.path.join(labels_path, filename))

if __name__ == '__main__':
    path = input("Enter the path: ")
    sort_files(path)
    print("Files have been sorted!")
