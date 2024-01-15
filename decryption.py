import rsa

def decrypt(user_role):
    try:
        print("user is",user_role)
        # Load the private key based on the user's role
        key_file_path = f'{user_role}_private_key.key'  # Adjust the file naming convention as needed
        with open(key_file_path, 'rb') as private_key_file:
            prikey = rsa.PrivateKey.load_pkcs1(private_key_file.read())

        # Read the encrypted data
        encrypted_data_path = f'{user_role}_encrypted_data.bin'  # Adjust the file naming convention as needed
        with open(encrypted_data_path, 'rb') as encrypted_data_file:
            edata = encrypted_data_file.read()

        # Decrypt the data
        decrypted_message = rsa.decrypt(edata, prikey)
        print(decrypted_message)
        return decrypted_message.decode()
       
    
    except Exception as e:
        print(f"Decryption failed for user role {user_role}: {str(e)}")
        return None


#decrypt("admin")