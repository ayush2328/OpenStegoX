# crypto.py
import base64, hashlib
from cryptography.fernet import Fernet

def derive_key(password: str) -> bytes:
    digest = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(digest)

def encrypt_message(message: str, password: str) -> bytes:
    key = derive_key(password)
    return Fernet(key).encrypt(message.encode())

def decrypt_message(cipher: bytes, password: str) -> str:
    key = derive_key(password)
    return Fernet(key).decrypt(cipher).decode()
