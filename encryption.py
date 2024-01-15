import rsa
from cryptography.fernet import Fernet
import base64
from keycreation import generate_admin_keys, generate_user_keys

def encrypt(message, user_type):
    if user_type == 'admin':
        generate_admin_keys()
        public_key_filename = 'admin_public_key.key'
        encrypted_filename = 'admin_encrypted_data.bin'
    elif user_type == 'user':
        generate_user_keys()
        public_key_filename = 'user_public_key.key'
        encrypted_filename = 'user_encrypted_data.bin'
    else:
        print("Invalid user type")
        return False

    # Encode the message as bytes using UTF-8 encoding
    message_bytes = message.encode('utf-8')

    # Load the user's/public key
    with open(public_key_filename, 'rb') as public_key_file:
        public_key = rsa.PublicKey.load_pkcs1(public_key_file.read())

    # Encrypt the message using the user's/public key
    encrypted_data = rsa.encrypt(message_bytes, public_key)

    # Write the encrypted data to a file
    with open(encrypted_filename, "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)

    print("Message encrypted and saved.")
    return True



encrypt("message", "admin")