import rsa

def generate_admin_keys(key_size=2048):
    # Create a new key pair for admin
    (admin_pubkey, admin_privkey) = rsa.newkeys(key_size)

    # Write the admin's public key to a file
    with open('admin_public_key.key', 'wb') as admin_public_key_file:
        admin_public_key_file.write(admin_pubkey.save_pkcs1('PEM'))

    # Write the admin's private key to a file
    with open('admin_private_key.key', 'wb') as admin_private_key_file:
        admin_private_key_file.write(admin_privkey.save_pkcs1('PEM'))

def generate_user_keys(key_size=2048):
    # Create a new key pair for user
    (user_pubkey, user_privkey) = rsa.newkeys(key_size)

    # Write the user's public key to a file
    with open('user_public_key.key', 'wb') as user_public_key_file:
        user_public_key_file.write(user_pubkey.save_pkcs1('PEM'))

    # Write the user's private key to a file
    with open('user_private_key.key', 'wb') as user_private_key_file:
        user_private_key_file.write(user_privkey.save_pkcs1('PEM'))

# Generate keys for an admin
#generate_admin_keys()

# Generate keys for a user
#generate_user_keys()
