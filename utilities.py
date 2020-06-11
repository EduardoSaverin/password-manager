import os
import config
from password_strength import PasswordPolicy, PasswordStats

policy = PasswordPolicy.from_names(
    length=8,
    uppercase=1,
    numbers=1,
    special=1
)


def check_if_already_initialized() -> bool:
    """checks if password manager is already initialized

    Returns:
        boolean: True if data directory already exists
    """
    if not os.path.exists(config.DATA_FOLDER):
        return True
    directory = os.listdir(config.DATA_FOLDER)
    if len(directory) == 0:
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
        [bool]: True if all conditions met otherwise False
    """
    # output comes empty [] if everything is right
    output = policy.test(password)
    return len(output) == 0


def check_password_strength(password: str) -> float:
    """Returns password strength on scale of 0.00 to 0.99. Good, strong passwords start at 0.66

    Args:
        password (str): password

    Returns:
        [float]: strength on scale of 0.00 to 0.99
    """
    stats = PasswordStats(password)
    return stats.strength()


def get_strength_string(strength: int) -> str:
    if strength >= 0.66:
        return "Strong"
    elif strength >= 0.4 and strength < 0.66:
        return "Fair"
    elif strength < 0.4:
        return "Weak"


def read_password_and_check(pwd_type: str) -> str:
    password = ''
    while True:
        password = input(pwd_type)
        if check_password_eligibility(password):
            print("Entered password doesn't satisy all(Min Len 8, One Special Character, One Upper Case, One Number) conditions.")
        else:
            break
    print(
        f'Password Strength :{get_strength_string(check_password_strength(password))}')
    return password
