import os
from pathlib import Path

# The list of all files and directories to be created for the project
list_of_files = [
    "app.py",
    "requirements.txt",
    "README.md",
    ".env",
    ".gitignore",
    "templates/index.html",
    "static/css/style.css",
    "static/js/script.js"
]

# Loop through each file path in the list
for filepath_str in list_of_files:
    # Convert the string path to a Path object for OS compatibility
    filepath = Path(filepath_str)
    
    # Split the path into its directory and filename components
    filedir, filename = os.path.split(filepath)

    # If the directory part is not empty, create the directory
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        print(f"Creating directory: {filedir} for the file {filename}")

    # Check if the file does not exist or if it is an empty file
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        # Create an empty file
        with open(filepath, 'w') as f:
            pass  # 'pass' does nothing, just ensures the file is created
        print(f"Creating empty file: {filepath}")
    
    # If the file already exists and is not empty, print a message
    else:
        print(f"File '{filename}' already exists.")

print("\nProject structure created successfully! 🚀")