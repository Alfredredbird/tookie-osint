import platform
from configparser import ConfigParser
from cryptography.fernet import Fernet
from modules.configcheck import *
from modules.lang import *

config = ConfigParser()
language_module = language_m
config.read("./config/config.ini")
versionToPass = configC(language_module)


def generate_encryption_key():
    """Generates a random encryption key for Fernet cipher."""
    return Fernet.generate_key()


def create_cipher(key):
    """Creates a Fernet cipher suite using the specified key."""
    return Fernet(key)


def encrypt_text(cipher_suite, text):
    """Encrypts the given text using the Fernet cipher suite."""
    return cipher_suite.encrypt(text.encode())


def decrypt_text(cipher_suite, encrypted_text):
    """Decrypts the encrypted text using the Fernet cipher suite."""
    return cipher_suite.decrypt(encrypted_text).decode()


def print_encrypted_and_decrypted(encrypted_text, ):
    """Prints the encrypted and decrypted versions of the text."""
    print("Encrypted text:", encrypted_text)
    # print("Decrypted text:", decrypted_text)


def save_encryption_info(config, private_key, sys_encrypted_key):
    """Saves the private key and system encrypted key to the configuration file."""
    config.set("main", "privatekey", str(private_key))
    config.set("main", "syscrypt", str(sys_encrypted_key))
    with open("./config/config.ini", "w") as configfile:
        config.write(configfile)


key = generate_encryption_key()

print("Encryption Key:", key.decode())
cipher_suite = create_cipher(key)
sys_info = (
    platform.system()
    + platform.release()
    + "-tookie-osintVer-"
    + versionToPass
    + "-"
    + platform.python_version()
    + "-"
    + config.get("main", "browser")
)
encrypted_sys_info = encrypt_text(cipher_suite, sys_info)
# decrypted_sys_info = decrypt_text(cipher_suite, encrypted_sys_info)
print_encrypted_and_decrypted(encrypted_sys_info.decode())
save_encryption_info(config, key, encrypted_sys_info)
