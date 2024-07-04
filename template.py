import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "mlProject"

# Base directory (assuming the script is in the project root)
base_dir = os.getcwd()

# Use relative paths for directories within the project
file_paths = [
    os.path.join(base_dir,"src",project_name,"utils", "common.py"),
    os.path.join(base_dir,"src",project_name,"utils","__init__.py"),
    os.path.join(base_dir,"src",project_name,"config","configuration.py"),
    os.path.join(base_dir,"src",project_name,"pipeline","__init__.py"),
    os.path.join(base_dir,"src",project_name,"entity","config_entity.py"),
    os.path.join(base_dir,"src",project_name,"entity","__init__.py"),
    os.path.join(base_dir,"src",project_name,"constants","__init__.py"),
    os.paty.join(base_dir,"src",project_name,"components","__init__.py"),
    os.path.join(base_dir, "research", "trials.ipynb"),
    os.path.join(base_dir, "templates", "index.html"),
]

# Separate list for files outside the project structure
other_files = [
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "requirements.txt",
    "setup.py",
]

# Create directories with relative paths
for filepath in file_paths:
    directory = os.path.dirname(filepath)  # Get directory path
    if not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)
        logging.info(f"Creating directory: {directory}")

# Handle files outside the project structure
for filename in other_files:
    filepath = os.path.join(base_dir, filename)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")

# Check existing files in the project structure
for filepath in file_paths:
    if os.path.exists(filepath):
        logging.info(f"{os.path.basename(filepath)} is already exists")
