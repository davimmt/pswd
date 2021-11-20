import os
from json import load, decoder
from password_handlers import copy_to_clipboard

def get_passwords():
    '''Return all passwords.

    Reads database file and return all passwords.
    '''
    with open(os.getenv('FILE_PATH'), 'r') as database:
        try:
            return load(database)
        except decoder.JSONDecodeError:
            return {}

def get_password(key):
    '''Return a password.

    Reads database file and return a password.
    '''
    passwords = get_passwords()
    try:
        password = passwords[key]
    except KeyError:
        exit('No such key.')
    copy_to_clipboard(password)
    return password

def show_all():
    '''Print all passwords.

    Reads database file and print all passwords.
    '''
    passwords = get_passwords()
    padding = 0

    for key in passwords: 
        if len(key) > padding and len(key) < 17: 
            padding = len(key)

    for key in passwords: 
        print('%s = %s' % (key.ljust(padding, ' '), passwords[key]))

    return passwords