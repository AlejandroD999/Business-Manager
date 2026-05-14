from .auth_db import add_user, user_exists

def register(username, password):
    # Manage user registration

    if not user_exists(username):
        # Take to sign_in page
        return
    
    
    



def sign_in():
    pass