import os
from sys import argv
from pathlib import Path
from os import path, environ, getenv
from password_create import create_password
from password_insert import insert_password
from password_update import update_password
from password_delete import delete_password
from password_select import show_all, get_password
from password_handlers import man, show_man, man_all_arguments

if __name__ == "__main__":
    environ['FILE_PATH'] = os.getenv('PSWD_PATH_FILE', f"{str(Path.home())}/.pswd").replace("~", str(Path.home()))
    environ['PUBK_PATH'] = os.getenv('PSWD_PATH_PUBK', f"{str(Path.home())}/.rsa_keys/pswd.pub").replace("~", str(Path.home()))
    environ['PRIK_PATH'] = os.getenv('PSWD_PATH_PRIK', f"{str(Path.home())}/.rsa_keys/pswd").replace("~", str(Path.home()))
    FILE_PATH = getenv('FILE_PATH')

    # Tries to create database file, ignore if already exists
    try:
        with open(os.open(FILE_PATH, os.O_CREAT | os.O_WRONLY, 0o600), "x") as database: pass
    except FileExistsError:
        pass

    arguments = {}
    # Use case for try statement: no arguments will print help
    try:
        arguments['mode_or_key'] = argv[1]
    except IndexError:
        exit(show_man())
    # Use case for try statement: one argument only is a shorthand for select mode
    try:
        arguments['key'] = argv[2]
    except IndexError:
        pass
    # Use case: insert key with defined value
    try:
        arguments['value'] = argv[3]
    except IndexError:
        pass

    if arguments['mode_or_key'].startswith('-'):
        man = man()
        mode = arguments['mode_or_key']

        # Invalid mode
        if mode not in man_all_arguments():
            print('Possible options:')
            exit(show_man())
        # Insert requires password name and value
        elif mode in man['insert']['args'] and len(arguments) < 3:
            exit('I need the password name and its value.')
        # Other methods (except for 'show') requires password name
        elif mode not in man['show']['args'] and len(arguments) < 2:
            exit('I need the password name.')
            
        if mode in man['create']['args']:
            create_password(arguments['key'])
        elif mode in man['insert']['args']:
            insert_password(arguments['key'], arguments['value'])
        elif mode in man['show']['args']:
            show_all()
        elif mode in man['update']['args']:
            update_password(arguments['key'])
        elif mode in man['delete']['args']:
            delete_password(arguments['key'])
        else:
            exit(show_man())
    else:
        key = arguments['mode_or_key']
        get_password(key)