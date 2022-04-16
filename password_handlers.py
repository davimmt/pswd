import base64
import cryptography
from os import getenv
from json import dumps
from random import choice
from pandas import DataFrame
from datetime import datetime
from cryptography.hazmat.primitives import hashes
from string import punctuation, ascii_letters, digits
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding

ENCODING = 'ISO-8859-1'

def generate_password(size=16, chars=punctuation + ascii_letters + digits):
    '''Generates random string.

    Generate a random string with the expecified size and character types.
    '''
    return ''.join(choice(chars) for char in range(size))

def store_password(key, value, passwords):
    '''Write to database file.

    Takes the new secret, encrypts it, merge with all the passwords and dumps it
    in the database file.
    '''
    value = value.encode(ENCODING)
    with open(getenv('PUBK_PATH'), "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )
    encrypted_value = public_key.encrypt(
        value,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    with open(getenv('FILE_PATH'), 'w') as file:
        passwords[key] = encrypted_value.decode(ENCODING)
        file.write(dumps(passwords))
    return True

def copy_to_clipboard(key, passwords):
    '''Copies a string to clipboard.

    Takes the password name and copy its decrypted value to the clipboard.
    '''
    decrypted_value = decrypt_password(passwords[key])
    to_clipboard = DataFrame([decrypted_value])
    to_clipboard.to_clipboard(index=False, header=False, excel=False)

def decrypt_password(value):
    value = value.encode(ENCODING)
    try:
        with open(getenv('PRIK_PATH'), "rb") as key_file:
            try:
                private_key = serialization.load_pem_private_key(
                    key_file.read(),
                    password=None,
                    backend=default_backend()
                )
            except ValueError:
                print('Wrong private key.')
                exit()
    except FileNotFoundError:
        print('Private key file not found.')
        exit()
    decrypted_value = private_key.decrypt(
        value,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted_value.decode(ENCODING)

def log_change(action, key, passwords):
    '''Log a change.

    Log a change in the database file, storing a backup.
    '''
    FILE_BKP_PATH = getenv('FILE_PATH') + '.bkp'
    try:
        with open(FILE_BKP_PATH, "x") as database_bkp: pass
    except FileExistsError:
        pass
    today = datetime.today().isoformat()
    with open(FILE_BKP_PATH, 'a') as file: 
        file.write(f'{today} -- {action} [{key}] -- {dumps(passwords)}\n')

def man():
    '''Manual.

    Return the manual, contaning operations description and arguments.
    '''
    return {
        'create': {'description': 'create a password with random value', 'args' : ['--create', '-c']},
        'insert': {'description': 'create or update a password with predefined value', 'args' : ['--insert', '-i']},
        'show': {'description': 'list all passwords', 'args' : ['--show-all', '-s']},
        'update': {'description': 'update or create a password with random value', 'args' : ['--update', '-u']},
        'delete': {'description': 'delete a password', 'args' : ['--delete', '-d']},
        'select': {'description': 'copy choosen password to clipboard', 'args' : []}
    }

def show_man():
    '''Print manual.

    Print the manual, contaning operations description and arguments.
    '''
    operations = man()
    for operation in operations: 
        print(f"{operation} : {operations[operation]['description']} => {operations[operation]['args']}")
    return True

def man_all_arguments():
    '''Return arguments.

    Return all possible arguments.
    '''
    operations = man()
    arguments = []
    for operation in operations: 
        arguments += operations[operation]['args']
    return list(filter(None, arguments))
