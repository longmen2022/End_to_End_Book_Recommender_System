import os  # Import the OS module to interact with the filesystem
from pathlib import Path  # Import Path from pathlib to handle file paths
import logging  # Import logging to track execution events

# Configure logging to display timestamps and messages
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Define the project directory where files and folders will be created
project_name = "C:/Users/men_l/Downloads/End_to_End_Book_Recommender_System/books_recommender"

# List of files to be created within the project structure
list_of_files = [
    f"{project_name}/__init__.py",  # Initialize the main project package
    f"{project_name}/components/__init__.py",  # Initialize the components module
    f"{project_name}/components/stage_00_data_ingestion.py",  # Data ingestion stage
    f"{project_name}/components/stage_01_data_validation.py",  # Data validation stage
    f"{project_name}/components/stage_02_data_transformation.py",  # Data transformation stage
    f"{project_name}/components/stage_03_model_trainer.py",  # Model training stage
    f"{project_name}/config/__init__.py",  # Initialize the configuration module
    f"{project_name}/config/configuration.py",  # Configuration file for the project
    f"{project_name}/constant/__init__.py",  # Initialize the constants module
    f"{project_name}/entity/__init__.py",  # Initialize the entity module
    f"{project_name}/entity/config_entity.py",  # Configuration entity definitions
    f"{project_name}/exception/__init__.py",  # Initialize the exception module
    f"{project_name}/exception/exception_handler.py",  # Exception handling script
    f"{project_name}/logger/__init__.py",  # Initialize the logger module
    f"{project_name}/logger/log.py",  # Logger configuration script
    f"{project_name}/pipeline/__init__.py",  # Initialize the pipeline module
    f"{project_name}/pipeline/training_pipeline.py",  # Training pipeline script
    f"{project_name}/utils/__init__.py",  # Initialize the utilities module
    f"{project_name}/utils/util.py",  # Utility functions script
    "config/config.yaml",  # Configuration file in YAML format
    ".dockerignore",  # Docker ignore file
    "app.py",  # Main application script
    "Dockerfile",  # Docker container configuration file
    "setup.py"  # Setup script for package installation
]

# Iterate over each file path in the list
for filepath in list_of_files:
    filepath = Path(filepath)  # Convert the file path into a Path object

    # Extract the directory and filename from the file path
    filedir, filename = os.path.split(filepath)

    # If the directory does not exist, create it
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  # Ensure the directory is created
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    # If the file does not exist or is empty, create an empty file
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:  # Open file in write mode (creates an empty file)
            pass  # No content is written, just creates the file
        logging.info(f"Creating empty file: {filename}")

    else:
        # Log if the file already exists
        logging.info(f"{filename} is already created")
