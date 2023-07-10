import configparser
import os

config_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "config.ini"))

# Initialize the configparser
config = configparser.ConfigParser()

# Read the config.ini file using the absolute path
config.read(config_file_path)

config.read('config/config.ini')

BASE_URL = config.get('Settings', 'BASE_URL')
BASE_PAGE_URL = config.get('Settings', 'BASE_PAGE_URL')
DEFAULT_USERNAME = config.get('Settings', 'DEFAULT_USERNAME')
DEFAULT_PASSWORD = config.get('Settings', 'DEFAULT_PASSWORD')

config_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "config.ini"))
print("Config file path:", config_file_path)
