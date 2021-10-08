import os
import sys
import json
import update_password as update
import get_password as get

FILE_PATH = os.path.dirname(os.path.abspath(__file__)) + '/.pswd'

if __name__ == "__main__":
    # Check if file exists
    try:  get.get_passwords()
    except: 
        with open(FILE_PATH, 'w') as file: file.write(json.dumps({'1':'1'}))

    key = sys.argv[1]
    # Return existing or create new
    if len(sys.argv) == 2:
        password = get.get_password(key)
        if not password:
            update.generate_password(key)
    # Remove or manually insert key value
    else:
        if sys.argv[2] == 'rm':
            update.delete_password(key)
        else:
            update.generate_password(key, sys.argv[2])
