from password_handlers import copy_to_clipboard, store_password, generate_password
from password_select import get_passwords

def create_password(key):
    '''Creates a password.

    Takes the password name as key, generate a random value,
    store it in the database file and copy the generated
    value to the clipboard.
    '''
    passwords = get_passwords()
    if key in passwords: exit('Password exists.')
    value = generate_password()
    passwords[key] = value
    store_password(passwords)
    copy_to_clipboard(value)
    return True