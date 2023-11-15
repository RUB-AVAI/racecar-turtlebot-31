import os
import shutil
from random import shuffle

def split_dataset(root_path, train_ratio=0.8, val_ratio=0.1):
    """
    Splits the dataset into train, test, and validation sets.

    Parameters:
    - root_path: path where the numbered files are located.
    - train_ratio: the fraction of data to be used for training.
    - val_ratio: the fraction of data to be used for validation.
    """
    
    # Create train, test, and val directories if they don't exist
    train_dir = os.path.join(root_path, 'train')
    test_dir = os.path.join(root_path, 'test')
    val_dir = os.path.join(root_path, 'val')
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)
    os.makedirs(val_dir, exist_ok=True)

    # List all jpg and png files
    images = [f for f in os.listdir(root_path) if f.endswith(('.jpg', '.png'))]
    base_names = [os.path.splitext(img)[0] for img in images]  # remove extensions

    shuffle(base_names)  # Shuffle to get random distribution

    # Calculate the number of samples for each set
    total_files = len(base_names)
    train_count = int(train_ratio * total_files)
    val_count = int(val_ratio * total_files)

    # Split the base names into train, val, and test lists
    train_files = base_names[:train_count]
    val_files = base_names[train_count:train_count + val_count]
    test_files = base_names[train_count + val_count:]

    # Helper function to move files
    def move_files(file_list, target_dir):
        for base in file_list:

            src_path = os.path.join(root_path, base + '.txt')
            if os.path.exists(src_path):
                shutil.move(src_path, target_dir)
            
            src_path = os.path.join(root_path, base + '.png')
            if os.path.exists(src_path):
                shutil.move(src_path, target_dir)
            else:
                src_path = os.path.join(root_path, base + '.jpg')
                shutil.move(src_path, target_dir)

    # Move the files
    move_files(train_files, train_dir)
    move_files(val_files, val_dir)
    move_files(test_files, test_dir)

# Example usage
split_dataset('data')
