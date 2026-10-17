import os
import shutil

def organize_files(folder_path):
    if not os.path.isdir(folder_path):
        print("Folder not found!")
        return

    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".doc", ".docx", ".txt"],
        "Audio": [".mp3", ".wav"],
        "Videos": [".mp4", ".mkv"],
        "Others": []
    }

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            extension = os.path.splitext(filename)[1].lower()
            category = "Others"

            for folder, extensions in file_types.items():
                if folder != "Others" and extension in extensions:
                    category = folder
                    break

            target_folder = os.path.join(folder_path, category)
            os.makedirs(target_folder, exist_ok=True)

            target_path = os.path.join(target_folder, filename)

            if os.path.exists(target_path):
                print(f"Skipped duplicate file: {filename}")
                continue

            shutil.move(file_path, target_path)
            print(f"Moved {filename} to {category}")

    print("File organization completed!")


if __name__ == "__main__":
    path = input("Enter the folder path to organize: ").strip().strip('"')
    organize_files(path)