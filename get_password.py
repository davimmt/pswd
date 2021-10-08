import os
import ast
import update_password as update

FILE_PATH = os.path.dirname(os.path.abspath(__file__)) + '/.pswd'

def get_passwords():
    file = open(FILE_PATH, 'r')
    contents = file.read()
    file.close()
    passwords = ast.literal_eval(contents)
    return passwords

def get_password(key):
    file = open(FILE_PATH, 'r')
    contents = file.read()
    file.close()
    passwords = ast.literal_eval(contents)
    password = passwords[key]
    update.copy_to_clipboard(password)
    return password

def show_all():
    passwords = get_passwords()
    passwords.pop('1')
    padding = 0
    for key in passwords: 
        if len(key) > padding and len(key) < 17: padding = len(key)

    for key in passwords: print('%s = %s' % (key.ljust(padding, ' '), passwords[key]))
