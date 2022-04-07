def search_user(users, email):
    for user in users:
        if email == user['email']:
            return user
    return None

def new_user(email, password, username):
    return {
        'email' : email,
        'password' : password,
        'username' : username,
        'WAM': 0,
        'WAM_perfered': 0,
        'perference': [],
        'good_at':[],
        'icon_link': "https://www.unsw.edu.au/etc/clientlibs/unsw-common/unsw-assets/img/social/UNSWlogo-opengraph-squaresafe.png",
        'introduction': ""
    }
def update_user(users, new):
    new_users = []
    for user in users:
        if user['email'] == new['email']:
            new_users.append(new) 
        else:
            new_users.append(user)
    return new_users