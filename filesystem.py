import config
import json
import os
import errno
from typing import Dict


def read_mastermac() -> str:
    with open(config.MASTERMAC_FILE, 'rb') as file:
        key = file.read()
    return key


def read_salt() -> str:
    with open(config.SALT_FILE, 'rb') as salt_file:
        return salt_file.read()


def write_salt(salt: str) -> None:
    check_path_dirs(config.SALT_FILE)
    with open(config.SALT_FILE, 'wb') as salt_file:
        return salt_file.write(salt)


def read_passwords_json() -> Dict[str, str]:
    json_str = "{}"
    if not os.path.exists(config.PWD_STORE_FILE):
        return json.loads(json_str)
    with open(config.PWD_STORE_FILE, 'r') as file:
        json_str = file.read()
    if not json_str:
        json_str = "{}"
    return json.loads(json_str)


def write_passwords_json(json_str: str) -> None:
    check_path_dirs(config.PWD_STORE_FILE)
    with open(config.PWD_STORE_FILE, 'w') as file:
        file.write(json_str)


def check_path_dirs(path: str) -> None:
    """Checks path directory and creates directory if not exists

    Args:
        path (str): directory/file path
    """
    if not os.path.exists(os.path.dirname(path)):
        try:
            os.makedirs(os.path.dirname(path))
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
