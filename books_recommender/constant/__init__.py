import os

# Get the current working directory
ROOT_DIR = os.getcwd()

# Define the folder where the configuration file is stored
CONFIG_FOLDER_NAME = "config"

# Specify the name of the configuration file
CONFIG_FILE_NAME = "config.yaml"

# Construct the full path to the configuration file
CONFIG_FILE_PATH = os.path.join(ROOT_DIR, CONFIG_FOLDER_NAME, CONFIG_FILE_NAME)
