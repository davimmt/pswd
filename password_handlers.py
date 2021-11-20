from os import getenv
from json import dumps
from random import choice
from pandas import DataFrame
from datetime import datetime
from string import punctuation, ascii_letters, digits

def generate_password(size=16, chars=punctuation + ascii_letters + digits):
    '''Generates random string.

    Generate a random string with the expecified size and character types.
    '''
    return ''.join(choice(chars) for char in range(size))

def store_password(passwords):
    '''Write to database file.

    Takes the passwords json and dumps it
    in the database file.
    '''
    with open(getenv('FILE_PATH'), 'w') as file:
        file.write(dumps(passwords))
    return True

def copy_to_clipboard(password):
    '''Copies a string to clipboard.

    Takes the password and copy it to the clipboard.
    '''
    to_clipboard = DataFrame([password])
    to_clipboard.to_clipboard(index=False, header=False, excel=False)

def log_change(action, key, passwords):
    '''Log a change.

    Log a change in the database file, storing a backup.
    '''
    FILE_BKP_PATH = getenv('FILE_PATH') + '.bkp'
    try:
        with open(FILE_BKP_PATH, "x") as database_bkp: pass
    except FileExistsError:
        pass
    today = datetime.today().isoformat()
    with open(FILE_BKP_PATH, 'a') as file: 
        file.write(f'{today} -- {action} [{key}] -- {dumps(passwords)}\n')

def man():
    '''Manual.

    Return the manual, contaning operations description and arguments.
    '''
    return {
        'create': {'description': 'create a password with random value', 'args' : ['--create', '-c']},
        'insert': {'description': 'create or update a password with predefined value', 'args' : ['--insert', '-i']},
        'show': {'description': 'list all passwords', 'args' : ['--show-all', '-s']},
        'update': {'description': 'update or create a password with random value', 'args' : ['--update', '-u']},
        'delete': {'description': 'delete a password', 'args' : ['--delete', '-d']},
        'select': {'description': 'copy choosen password to clipboard', 'args' : []}
    }

def show_man():
    '''Print manual.

    Print the manual, contaning operations description and arguments.
    '''
    operations = man()
    for operation in operations: 
        print(f"{operation} : {operations[operation]['description']} => {operations[operation]['args']}")
    return True

def man_all_arguments():
    '''Return arguments.

    Return all possible arguments.
    '''
    operations = man()
    arguments = []
    for operation in operations: 
        arguments += operations[operation]['args']
    return list(filter(None, arguments))
