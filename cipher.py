from Crypto import Random
from Crypto.Cipher import AES
import base64
from binascii import unhexlify, hexlify
import os
import filesystem

IV = "qwertyuiopasdfgh"


BS = 16
def pad(s): return s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
def unpad(s): return s[:-ord(s[len(s)-1:])]


class AESCipher:
    def __init__(self):
        super().__init__()

    def encrypt(self, raw, salt):
        raw = pad(raw)
        cipher = AES.new(salt, AES.MODE_CBC, filesystem.read_block_size())
        return hexlify(cipher.encrypt(raw.encode())).decode()

    def decrypt(self, enc, salt):
        enc = unhexlify(enc)
        cipher = AES.new(salt, AES.MODE_CBC, filesystem.read_block_size())
        return unpad(cipher.decrypt(enc)).decode()
