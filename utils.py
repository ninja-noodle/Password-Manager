import secrets
import base64
from string import ascii_letters, digits, punctuation
from werkzeug.security import generate_password_hash, check_password_hash
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend


class MasterSetup:
    def __init__(self):
        self.master_key = None
        self.hashed_key = None

    def hashify(self, master_key: str):
        self.master_key = master_key
        self.hashed_key = generate_password_hash(self.master_key, method='pbkdf2:sha256',
                                                  salt_length=10)
        return self.hashed_key

    def verify(self, hashed: str, plain: str) -> bool:
        return check_password_hash(hashed, plain)


class FernetSetup:
    def __init__(self):
        self.master = None
        self.salt = None

    def derive_key(self, master: str, salt: bytes) -> bytes:
        self.master = master
        self.salt = salt
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100_000,
            backend=default_backend()
        )
        return base64.urlsafe_b64encode(kdf.derive(master.encode()))

    def encrypt(self, derived_key: bytes, main_fernet_key: bytes) -> bytes:
        cipher = Fernet(derived_key)
        return cipher.encrypt(main_fernet_key)

    def decrypt(self, derived_key: bytes, encrypted_fernet_key: bytes) -> bytes:
        cipher = Fernet(derived_key)
        return cipher.decrypt(encrypted_fernet_key)




class PwdWizzard:
    def __init__(self, fernet_key):
        self.cipher = Fernet(fernet_key) 
        self.characters = ascii_letters + digits + punctuation
        self.generated_pwd = None
        self.length = None
        self.password = None
        self.encrypted_pwd = None

    def forge(self, length: int):
        self.length = length
        self.generated_pwd = "".join(secrets.choice(self.characters) for _ in range(length))
        return self.generated_pwd

    def encrypt(self, password):
        self.password = password
        return self.cipher.encrypt(password.encode())

    def decrypt(self, encrypted_pwd):
        self.encrypted_pwd = encrypted_pwd
        return self.cipher.decrypt(self.encrypted_pwd).decode()
    
