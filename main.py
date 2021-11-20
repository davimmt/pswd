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

    # Listing all, return existing or create new
    key = sys.argv[1]
    if len(sys.argv) == 2:
        show_all_operator = ['s', 'show', 'all', 'show-all', 'sa']

        if key in show_all_operator:
            get.show_all()
        else:
            try:
                password = get.get_password(key)
            except:
                update.generate_password(key)
                print('New.')
    # Remove or manually insert key value
    else:
        operator = sys.argv[2]
        remove_operator = ['r', 'd', 'rm', 'del', 'remove', 'delete']

        if operator in remove_operator:
            update.delete_password(key)
        else:
            update.generate_password(key, operator)
