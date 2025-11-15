import os
import shutil
from pathlib import Path

# File type mapping
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".md"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Archives": [".zip", ".rar", ".tar"],
    "Code": [".py", ".js", ".html", ".css", ".sql"],
    "Audio": [".mp3", ".wav"],
}

def organize_files(folder_path):
    folder = Path(folder_path)

    if not folder.exists():
        print("❌ Folder does not exist")
        return

    for file in folder.iterdir():
        if file.is_file():
            ext = file.suffix.lower()
            moved = False

            for category, extensions in FILE_TYPES.items():
                if ext in extensions:
                    category_folder = folder / category
                    category_folder.mkdir(exist_ok=True)
                    shutil.move(str(file), str(category_folder / file.name))
                    print(f"➡  Moved {file.name} → {category}/")
                    moved = True
                    break

            if not moved:
                other_folder = folder / "Others"
                other_folder.mkdir(exist_ok=True)
                shutil.move(str(file), str(other_folder / file.name))
                print(f"➡  Moved {file.name} → Others/")

    print("\n🎉 File organization completed!")


if __name__ == "__main__":
    path = input("Enter folder path to organize: ")
    organize_files(path)
