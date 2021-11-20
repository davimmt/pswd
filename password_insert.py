from password_handlers import copy_to_clipboard, store_password, log_change
from password_select import get_passwords

def insert_password(key, value):
    '''Creates or updates a password.

    Takes the password name as key and defined its value,
    store it in the database file and copy the value to the clipboard. 
    Creates if it does not exist.
    '''
    passwords = get_passwords()
    if key in passwords: log_change('change', key, passwords)
    passwords[key] = value
    store_password(passwords)
    copy_to_clipboard(value)
    return True