from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding

def check_pub_key(pubk_path):
    try:
        with open(pubk_path, "rb") as key_file:
            public_key = serialization.load_pem_public_key(
                key_file.read(),
                backend=default_backend()
            )
    except FileNotFoundError:
        exit(print(f"Public key file not found at {pubk_path}"))
    except IsADirectoryError:
        exit(print(f"You gave me a directory ({pubk_path}) path, I need a file path."))
    return public_key

def check_pri_key(prik_path):
    try:
        with open(prik_path, "rb") as key_file:
            try:
                private_key = serialization.load_pem_private_key(
                    key_file.read(),
                    password=None,
                    backend=default_backend()
                )
            except ValueError:
                exit(print('Wrong private key.'))
    except FileNotFoundError:
        exit(print(f"Private key file not found at {prik_path}"))
    except IsADirectoryError:
        exit(print(f"You gave me a directory ({prik_path}) path, I need a file path."))
    return private_key

def validate_key_pair_matching(public_key, private_key):
    value = b'1'
    encrypted_value = public_key.encrypt(
        value,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    try:
        private_key.decrypt(
            encrypted_value,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
    except ValueError:
        warning = input("[WARNING] Key pair does not match. Continue (y/n)? ").lower().strip()
        if warning[0] != "y": exit(print('Operation canceled'))
    return True