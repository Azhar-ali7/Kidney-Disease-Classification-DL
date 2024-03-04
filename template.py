import os
from pathlib import Path
import logging

# logging string
# asctime for current timestamp and message of log
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s')

project_name = 'cnnClassifier'

list_of_files = [
    # .gitkeep (if a folder is empty it won't be uploaded in github repo)
    # it will be removed when we do CICD pipeline
    ".github/workflows/.gitkeep",

    # standard practice to create src (source) 
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

for filepath in list_of_files:
    # windows support backslash and mac and linus supports forward slash
    # Path makes file path compatible to all OS
    filepath = Path(filepath)

    # folder path and file name
    filedir, filename = os.path.split(filepath)


    if filedir != "":
        os.makedirs(filedir, exist_ok=True) #exist_ok (won't re create folder)
        # message in terminal
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    # only create if not present or file size is zero
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    # if already present
    else:
        logging.info(f"{filename} already exists")