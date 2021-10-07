import os
import json
import random
import string
import pyperclip
from datetime import datetime
import get_password as get

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
    if key in passwords:
        today = datetime.today().isoformat()
        with open(FILE_PATH + '.bkp', 'a') as file: file.write('%s -- change [%s] -- %s\n' % (today, key, json.dumps(passwords)))
    passwords[key] = value
    with open(FILE_PATH, 'w') as file: file.write(json.dumps(passwords))

def delete_password(key):
    passwords = get.get_passwords()
    if key in passwords:
        today = datetime.today().isoformat()
        with open(FILE_PATH + '.bkp', 'a') as file: file.write('%s -- delete [%s] -- %s\n' % (today, key, json.dumps(passwords)))
    passwords.pop(key)
    with open(FILE_PATH, 'w') as file: file.write(json.dumps(passwords))