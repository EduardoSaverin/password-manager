import utilities
import sys
import config


def initialize():
    if utilities.check_if_already_initialized():
        print('''WARNING! Password manager was already setup in past on this machine.
        Proceeding would delete any existing data.''')
        while True:
            proceed: str = input("Would you like to continue? Y/N")
            proceed = proceed.lower()
            if proceed in ['y', 'n']:
                if proceed == 'y':
                    break
                if proceed == 'n':
                    return
    print('''Enter master password that will be used for:
    1. To get the passwords.
    2. To add/modify passwords.
    3. To delete passwords.
    4. To import/export password in JSON format.
    ''')

    master_password: str = utilities.read_password_and_check('Master Password')
    utilities.generate_mastermac(master_password)


def show_options():
    print('\n')
    print(f"Welcome to Python Password Manager {config.APP_VERSION}")
    if not utilities.check_if_already_initialized():
        initialize()

    print('''
    Choose the operation you would like to do :
    1. Add New Password
    2. Delete Password
    3. Modify Password
    4. Show Password
    5. Setup
    6. Quit

    ''')
    option = int(input('Choose Option : '))
    if option == 1:
        master_password = input('Please enter master password : ')
        if not utilities.auth(master_password):
            print('Authentication failed')
        else:
            key = input('Please enter key : ')
            password = input('Password : ')
            utilities.store_password(key, password)
    elif option == 2:
        master_password = input('Please enter master password : ')
        if not utilities.auth(master_password):
            print('Authentication failed')
        else:
            key = input('Please enter key : ')
            password = utilities.delete_password(key)
            if password is not None:
                print(f'Password was {password}')
    elif option == 3:
        master_password = input('Please enter master password : ')
        if not utilities.auth(master_password):
            print('Authentication failed')
        else:
            key = input('Please enter key : ')
            value = utilities.get_password(key)
            if value:
                password = input("New Password : ")
                utilities.delete_password(key)
                utilities.store_encrypted_password(key, password)
            else:
                print(
                    f"Password for Key {key} not found. Try adding new password instead")
    elif option == 4:
        master_password = input('Please enter master password : ')
        if not utilities.auth(master_password):
            print('Authentication failed')
        else:
            key = input('Please enter key : ')
            print(f'Password for Key {key} is {utilities.get_password(key)}')
    elif option == 5:
        initialize()
    elif option == 6:
        print("Quiting...")
        sys.exit()

    show_options()


if __name__ == '__main__':
    show_options()
