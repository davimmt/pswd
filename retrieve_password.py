import os
import ast
import generate_password as new

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
    try:
        passwords = ast.literal_eval(contents)
        password = passwords[key]
        new.copy_to_clipboard(password)
        return password
    except:
        print('No such key.')
        return False

def is_new_key(key): return False if key in get_passwords() else True
