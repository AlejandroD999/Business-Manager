import string

def valid_username(username):  
    MIN_LEN = 5
    MAX_LEN = 32

    # Length Requirements
    if not MIN_LEN <= len(username) <= MAX_LEN:
        return False

    # TODO Allowed Characters

    return True

def valid_password(password):
    MIN_LEN = 6
    MAX_LEN = 32
    VERIFIED_SYMBOLS = False

    if not MIN_LEN <= len(password) <= MAX_LEN:
        return False



    return True
