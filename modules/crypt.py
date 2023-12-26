import platform
from configparser import ConfigParser

from cryptography.fernet import Fernet

from modules.configcheck import *
from modules.lang import *

config = ConfigParser()


language_module = language_m


def print_encrypted_and_decrypted_text(decrypted_text):
    print("Decrypted text:", decrypted_text)


def saveInfo(config, syskey):
    config.read("./config/config.ini")
    config.set("main", "privatekey", str(key))
    config.set("main", "syscrypt", str(syskey))
    with open("./config/config.ini", "w") as f:
        config.write(f)


# Generate a random key
key = Fernet.generate_key()
print("Encryption Key:", key.decode())  # Convert the key to a string for printing

# Create a Fernet object with the key
cipher_suite = Fernet(key)

def encrypt(text):
    encrypted_text = cipher_suite.encrypt(text.encode())
    return encrypted_text

def decrypt(encrypted_text):
    decrypted_text = cipher_suite.decrypt(encrypted_text).decode()
    return decrypted_text


versionToPass = configC(language_module)

config.read("./config/config.ini")
browser = config.get("main", "browser")
syskey = (
    platform.system()
    + platform.release()
    + "-AlfredVer-"
    + versionToPass
    + "-"
    + platform.python_version()
    + "-"
    + browser
)

encrypted_text = encrypt(syskey)
decrypted_text = decrypt(encrypted_text)