from cryptography.fernet import Fernet
lol = True
# Function to get the encryption key from the user
def get_encryption_key():
    key = input("Enter the encryption key: ")
    return key.encode()

# Function to get the encrypted text from the user
def get_encrypted_text():
    encrypted_text = input("Enter the encrypted text: ")
    return encrypted_text.encode()

# Function to decrypt the text
def decrypt_text(key, encrypted_text):
    cipher_suite = Fernet(key)
    try:
        decrypted_text = cipher_suite.decrypt(encrypted_text).decode()
        return decrypted_text
    except Exception as e:
        print(f"Decryption failed: {str(e)}")
        return None

if lol == True:
    key = get_encryption_key()
    encrypted_text = get_encrypted_text()

    print("Key:", key)  # Add this line to print the key
    print("Encrypted Text:", encrypted_text)  # Add this line to print the encrypted text

    decrypted_text = decrypt_text(key, encrypted_text)

    if decrypted_text:
        print("Decrypted text:", decrypted_text)
    else:
        print("Failed to decrypt the text.")
