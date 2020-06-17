import utilities


class PasswordManager(object):
    def __init__(self):
        super().__init__()

    def get_password(self, key: str) -> str:
        return utilities.get_password(key)
