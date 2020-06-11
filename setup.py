import utilities


def initialize():
    if utilities.check_if_already_initialized():
        print("WARNING! Password manager was already setup in past on this machine. \
        Proceeding would delete any existing data.")

    while True:
        proceed: str = input("Would you like to continue? Y/N")
        proceed = proceed.lower()
        if proceed in ['y', 'n']:
            if proceed == 'y':
                break
            if proceed == 'n':
                return

    print('''Now you will be asked to enter master password that will be used for:
    1. To get the passwords.
    2. To add/modify passwords.
    3. To delete passwords.
    4. To import/export password in JSON format.
    ''')

    master_password: str = utilities.read_password_and_check('Master Password')


if __name__ == '__main__':
    pass
