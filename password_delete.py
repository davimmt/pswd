from password_handlers import store_password, log_change
from password_select import get_passwords

def delete_password(key):
    '''Deletes a password.

    Takes the password name as key, and deletes it
    from the database file.
    '''
    passwords = get_passwords()
    passwords_bkp = get_passwords()
    try:
        passwords.pop(key)
    except KeyError:
        exit('No such key.')
    log_change('delete', key, passwords_bkp)
    store_password(passwords)