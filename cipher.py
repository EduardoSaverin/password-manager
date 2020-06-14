from Crypto.Cipher import AES


class AESCipher(object):
    def __init__(self):
        super().__init__()

    def encrypt(self, password: str, key: str) -> bytes:
        cipher = AES.new(key, AES.MODE_PGP)
        ciphertext = cipher.encrypt(password)
        return ciphertext

    def decrypt(self, enc_password: bytes, key: str) -> bytes:
        cipher = AES.new(key, AES.MODE_PGP)
        ciphertext = cipher.decrypt(enc_password)
        return ciphertext
