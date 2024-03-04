# these three lines of code will help if we publish this project as pypi package 
# it will display the README.md file
import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Kidney-Disease-Classification-DL"
AUTHOR_USER_NAME = "Azhar-ali7"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "aliazhar007007@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version= __version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description="text/markdown",
    url=f"https://github.com/Azhar-ali7/Kidney-Disease-Classification-DL",
    project_urls={
        "Bug Tracker": f"https://github.com/Azhar-ali7/Kidney-Disease-Classification-DL/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)