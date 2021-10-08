import os
import sys
import json
import update_password as update
import get_password as get

FILE_PATH = os.path.dirname(os.path.abspath(__file__)) + '/.pswd'

def complete_strip(string):
    string = string.strip().lower()
    while ' ' in string: string = string.replace(' ', '_')
    return string

if __name__ == "__main__":
    # Check if file exists
    try:  get.get_passwords()
    except: 
        with open(FILE_PATH, 'w') as file: file.write(json.dumps({'1':'1'}))

    key = complete_strip(sys.argv[1])
    # Return existing or create new
    if len(sys.argv) == 2:
        password = get.get_password(key)
        if not password:
            update.generate_password(key)
    # Create, update or remove
    else:
        operantion = sys.argv[2][0].strip().lower()
        if operantion != 'r' or operantion != 'd':
            is_new_key = get.is_new_key(key)
            if is_new_key: update.generate_password(key)
            else:
                copy = input('Overwrite password? ').strip().lower()[0]
                if copy == 'y':
                    password = update.generate_password(key)
        else:
            update.delete_password(key)