import os

def rename_files_in_folder(folder_path, start_number):
    # List all files in the folder
    files = sorted([f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))])

    # Create a dictionary with base names (without extensions) as keys and a list of related files as values
    grouped_files = {}
    for file in files:
        base_name, ext = os.path.splitext(file)
        if base_name not in grouped_files:
            grouped_files[base_name] = []
        grouped_files[base_name].append(file)

    # Rename files
    current_number = start_number
    for base_name, related_files in grouped_files.items():
        for file in related_files:
            old_path = os.path.join(folder_path, file)
            new_name = f"{current_number}{os.path.splitext(file)[1]}"
            new_path = os.path.join(folder_path, new_name)
            os.rename(old_path, new_path)
        current_number += 1

    print(f"Files in {folder_path} have been renamed starting from {start_number}.")

if __name__ == "__main__":
    folder_path = input("Enter the path to the folder: ")
    start_number = int(input("Enter the starting number: "))
    rename_files_in_folder(folder_path, start_number)
