from os import getenv

from cryptography.fernet import Fernet
from dotenv import load_dotenv


class FernetCypher:
    load_dotenv()
    fernet = Fernet(getenv("FERNET_KEY").encode())

    def encrypt(self, text: str) -> bytes:
        return self.fernet.encrypt(text.encode())

    def decrypt(self, encrypted: bytes) -> str:
        return self.fernet.decrypt(encrypted).decode()

    def secret(self):
        return b'gAAAAABjnnBkfDGxKOAdc3T9sxdtdXEfwTzBUvOiAZWE64ResgFs7--XBgV0BUpaT8D9f1Fqzg7coKrm_mF5GwBv5CqeXg-3zg=='
