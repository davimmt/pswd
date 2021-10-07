import sys
import json
import generate_password as new
import retrieve_password as get

def complete_strip(string):
    string = string.strip().lower()
    while ' ' in string: string = string.replace(' ', '_')
    return string

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Choose to create a [new] password or [get] an existing one.')
        exit()
    if len(sys.argv) == 2:
        print('Insert the key name.')
        exit()

    try: get.get_passwords()
    except: 
        with open('.pswd', 'w') as file: file.write(json.dumps({'1':'1'}))

    key = complete_strip(sys.argv[2])
    if sys.argv[1] == 'new':
        is_new_key = get.is_new_key(key)
        if is_new_key:
            new.generate_password(key)
        else:
            copy = input('Key already exists; [r]ewrite or [c]opy it to cliboard? ').strip().lower()[0]
            if copy == 'r':
                password = new.generate_password(key)
            if copy == 'c':
                password = get.get_password(key)

    if sys.argv[1] == 'get':
        password = get.get_password(key)
        if not password:
            create = input('Create new key with name? ').strip().lower()
            if create == 'y':
                new.generate_password(key)
