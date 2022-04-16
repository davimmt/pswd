from password_handlers import copy_to_clipboard, store_password, generate_password, log_change
from password_select import get_passwords

def update_password(key):
    '''Creates or updates a password.

    Takes the password name as key, generates a random value,
    store it in the database file and copy the generated
    value to the clipboard. Creates if it does not exist.
    '''
    passwords = get_passwords()
    if key not in passwords: 
        print('New.')
        passwords_old = False
    else:
        passwords_old = get_passwords()
    value = generate_password()
    store_password(key, value, passwords)
    if passwords_old:
        log_change('update', key, passwords_old)
    copy_to_clipboard(key, passwords)
    return True