def search_user(users, email):
    for user in users:
        if email == user['email']:
            return user
    return None

def new_user(email, password, username):
    return {
        'email' : email,
        'password' : password,
        'username' : username
    }