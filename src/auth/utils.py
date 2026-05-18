
def valid_username(username):  
    MIN_LEN = 5
    MAX_LEN = 32

    # Length Requirements
    if not MIN_LEN <= len(username) <= MAX_LEN:
        return False

    # TODO Allowed Characters

    return True

