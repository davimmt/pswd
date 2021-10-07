import sys
import json
import update_password as update
import get_password as get

def complete_strip(string):
    string = string.strip().lower()
    while ' ' in string: string = string.replace(' ', '_')
    return string

if __name__ == "__main__":
    # Check if file exists
    try: get.get_passwords()
    except: 
        with open('.pswd', 'w') as file: file.write(json.dumps({'1':'1'}))

    key = complete_strip(sys.argv[1])
    # New
    if len(sys.argv) == 3:
        if sys.argv[2][0].strip().lower() != 'r':
            is_new_key = get.is_new_key(key)
            if is_new_key: update.generate_password(key)
            else:
                copy = input('Key already exists; [r]ewrite or [c]opy it to cliboard? ').strip().lower()[0]
                if copy == 'r':
                    password = update.generate_password(key)
                if copy == 'c':
                    password = get.get_password(key)
        else:
            update.delete_password(key)
    # Returning existing
    else:
        password = get.get_password(key)
        if not password:
            create = input('Create new key with name? ').strip().lower()
            if create == 'y':
                update.generate_password(key)