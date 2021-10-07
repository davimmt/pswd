import os
import json
import random
import string
import pyperclip
import retrieve_password as get

FILE_PATH = os.path.dirname(os.path.abspath(__file__)) + '/.pswd'

def generate_password(key):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(16))
    print('Password is: [%s]' % password)

    store = input('\nDo you wish to store it? ').lower()[0]
    if store == 'y':
        store_password(key, password)
        copy_to_clipboard(password)

def copy_to_clipboard(string):
    pyperclip.copy(string)
    paste = pyperclip.paste()

def store_password(key, value):
    passwords = get.get_passwords()
    passwords[key] = value
    with open(FILE_PATH, 'w') as file: file.write(json.dumps(passwords))
