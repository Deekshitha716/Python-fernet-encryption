import os
import pwinput
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def get_key(user_pwd, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt, 
        iterations=600000,
    )
    return base64.urlsafe_b64encode(kdf.derive(user_pwd.encode()))


#LOCKING

password = pwinput.pwinput(prompt="Set the master password: ", mask="*")
secret_message = b"This is the secret message"

salt = os.urandom(16)
cipher_lock = Fernet(get_key(password, salt))
encrypted_data = cipher_lock.encrypt(secret_message)

final_encrypted_data = salt + encrypted_data

with open("vault.dat", "wb") as f:
    f.write(final_encrypted_data)

print("Data locked inside 'vault.dat'.")


#UNLOCKING

pwd2 = pwinput.pwinput(prompt="Enter password to try and unlock: ", mask="*")
with open("vault.dat", "rb") as f:
    loaded_data = f.read()

extracted_salt = loaded_data[:16]
extracted_msg = loaded_data[16:]

try:
    cipher_unlock = Fernet(get_key(pwd2, extracted_salt))
    result = cipher_unlock.decrypt(extracted_msg).decode()
    print(f"Success: {result}")
except Exception:
    print("Access Denied: The keys do not match!")





