import appdirs
import os
import pathlib

# Project Descriptors
APP_NAME: str = "password-manager"
APP_VERSION: int = 1.0
DESCRIPTION: str = "A utility that can be used to store hashed password for db/service and program that need those password to connect db/service can retrieve password from this utility, this way there is no need to store password in programs."
AUTHOR: str = "Sumit Kumar"
GITHUB: str = "github.com/EduardoSaverin"

# System Paths & Files
APP_FOLDER = pathlib.Path(os.path.abspath(__file__)).parent
DATA_FOLDER = pathlib.Path(appdirs.user_data_dir(APP_NAME))
DICTIONARY_FILE = pathlib.Path(DATA_FOLDER, '.dictionary')
MASTERMAC_FILE = pathlib.Path(DATA_FOLDER, '.mmac')
PWD_STORE_FILE = pathlib.Path(DATA_FOLDER, '.pwdstore')
SALT_FILE = pathlib.Path(DATA_FOLDER, '.salt')
