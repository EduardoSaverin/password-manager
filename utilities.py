import os
import config
from password_strength import PasswordPolicy, PasswordStats
from hashlib import pbkdf2_hmac
from Crypto.Cipher import AES
import filesystem
import json
from cipher import AESCipher

policy = PasswordPolicy.from_names(
    length=8,
    uppercase=1,
    numbers=1,
    special=1
)

aes = AESCipher()


def check_if_already_initialized() -> bool:
    """checks if password manager is already initialized

    Returns:
        boolean: True if data directory already exists
    """
    if not os.path.exists(config.DATA_FOLDER):
        return True
    elif os.path.exists(config.DATA_FOLDER) and len(os.listdir(config.DATA_FOLDER)) != 0:
        return True
    return False


def check_password_eligibility(password: str) -> bool:
    """Checks if entered password meets all conditions
    1. Min length of 8
    2. One Uppercase letter
    3. One number
    4. One Special Character


    Args:
        password (str): password

    Returns:
        bool: True if all conditions met otherwise False
    """
    # output comes empty [] if everything is right
    output = policy.test(password)
    return len(output) == 0


def check_password_strength(password: str) -> float:
    """Returns password strength on scale of 0.00 to 0.99. Good, strong passwords start at 0.66

    Args:
        password (str): password

    Returns:
        float: strength on scale of 0.00 to 0.99
    """
    stats = PasswordStats(password)
    return stats.strength()


def get_strength_string(strength: int) -> str:
    print(strength)
    if strength >= 0.66:
        return "Strong"
    elif strength >= 0.3 and strength < 0.66:
        return "Fair"
    elif strength < 0.3:
        return "Weak"


def read_password_and_check(pwd_type: str) -> str:
    password = ''
    while True:
        password = input(f'{pwd_type} : ')
        if not check_password_eligibility(password):
            print("Entered password doesn't satisy all(Min Len 8, One Special Character, One Upper Case, One Number) conditions.")
        else:
            break
    print(
        f'Password Strength : {get_strength_string(check_password_strength(password))}')
    return password


def generate_mastermac(master_pwd: str) -> str:
    salt: str = os.urandom(16)
    block_size = os.urandom(16)
    filesystem.write_salt(salt)
    filesystem.write_block_size(block_size)
    derived_key = pbkdf2_hmac(
        'sha512', master_pwd.encode(), salt, 10000, dklen=16)
    key = derived_key.hex()
    filesystem.check_path_dirs(config.MASTERMAC_FILE)
    with open(config.MASTERMAC_FILE, 'wb') as file:
        file.write(key.encode())
    return key


def store_password(key: str, password: str) -> None:
    salt: str = filesystem.read_mastermac()
    ciphertext = aes.encrypt(password, salt)
    json_data = filesystem.read_passwords_json()
    if key in json_data:
        print(
            f'Password for Key {key} already exists. You can try modifying password if needed.')
    json_data[key] = ciphertext
    filesystem.write_passwords_json(json.dumps(json_data))


def auth(master_pwd: str) -> bool:
    verified = False
    salt = filesystem.read_salt()
    derived_key = pbkdf2_hmac('sha512', master_pwd, salt)
    key = derived_key.hex()
    if key == filesystem.read_mastermac():
        verified = True
    return verified


def get_password(key: str) -> str:
    """Returns password from stored passwords

    Args:
        key (str): Name of the key with which password was stored.

    Returns:
        str: stored password or None either Key is invalid or password is not found
    """
    if not key:
        print('Supplied KEY is not valid')
        return None
    json_dump = filesystem.read_passwords_json()
    enc_password: str = json_dump.get(key)
    salt: str = filesystem.read_mastermac()
    password = aes.decrypt(enc_password, salt)
    return password


def delete_password(key: str) -> str:
    """Deletes key password from stored Passwords

    Args:
        key (str): Name of the key whose password to be removed.

    Returns:
        str: stored password or None either Key is invalid or password is not found
    """
    if not key:
        print('Supplied KEY is not valid')
        return None
    json_dump = filesystem.read_passwords_json()
    if key not in json_dump:
        print(f'Key {key} does not exist.')
        return None
    del json_dump[key]
    password = get_password(key)
    filesystem.write_passwords_json(json.dumps(json_dump))
    return password
