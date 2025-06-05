# Import necessary functions from setuptools to package the project
from setuptools import setup, find_packages

# Open the README.md file to use as the long description for the package
with open(r"C:\Users\men_l\Downloads\End_to_End_Book_Recommender_System\README.md", "r", encoding="utf-8") as f:

    long_description = f.read()  # Read the content of README.md into a variable

# Define key variables for project metadata (these can be modified as needed)
REPO_NAME = "ML Based Books Recommender System"  # Name of the repository
AUTHOR_USER_NAME = "Long Men"  # Author's name
SRC_REPO = "books_recommender"  # Name of the source package folder
LIST_OF_REQUIREMENTS = []  # List of dependencies required for the project

# Call the setup function to package the project
setup(
    name=SRC_REPO,  # Define the package name
    version="0.0.1",  # Define the initial version of the package
    author="BOKTIAR AHMED BAPPY",  # Author's name
    description="A small local package for ML-based book recommendations",  # Short description of the package
    long_description=long_description,  # Use the content of README.md as the detailed package description
    long_description_content_type="text/markdown",  # Specify the format of long description (Markdown)
    url="https://github.com/longmen2022/End_to_End_Book_Recommender_System.git",  # URL of the project repository
    author_email="lmen776@gmail.com",  # Author's email address
    packages=find_packages(),  # Automatically find and include all packages in the directory
    license="MIT",  # License type for the project
    python_requires=">=3.7",  # Specify minimum Python version required for this package
    install_requires=LIST_OF_REQUIREMENTS  # Define dependencies (currently empty, can be updated)
)
