from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
from Crypto.Random import get_random_bytes

class PasswordHelper:
    @staticmethod
    def hash_password(password, salt):
        return PBKDF2(password.encode('UTF-8'), salt, dkLen=16, count=200000, hmac_hash_module=SHA512)

    @staticmethod
    def hash_register(password):
        salt = get_random_bytes(16)
        return PasswordHelper.hash_password(password, salt), salt
  
    @staticmethod
    def hash_login(password, salt):
        return PBKDF2(password.encode('UTF-8'), salt, dkLen=16, count=200000, hmac_hash_module=SHA512), salt
