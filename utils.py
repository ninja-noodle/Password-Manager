import secrets
from string import ascii_letters, digits, punctuation

class PwdWizzard:
    def __init__(self):
        self.characters = ascii_letters + digits + punctuation
        self.generated_pwd = None
        self.length = None

    def forge(self, length: int):
        self.length = length
        self.generated_pwd = "".join(secrets.choice(self.characters) for _ in range(length))
        return self.generated_pwd
