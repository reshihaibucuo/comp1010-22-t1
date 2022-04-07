from bisect import insort
from pyhtml import div, a, li,h4,label, p

def No_login_nvabar():
    return """
        <div class="navbar_right_container">
            <div class="navbar_item">
                <a href="login" class="navbar_item_content"> Sign in </a>
            </div>
            <div class="navbar_item">
                <a href="signup" class="navbar_item_content"> Sign up </a>
            </div>
        </div>
    """
    

def Login_nvabar(email):
    return f"""
        <div class="navbar_right_container">
            <div class="navbar_item">
                <a href="viewprofile?email={email}" class="navbar_item_content"> My Profile </a>
            </div>
            <div class="navbar_item">
                <a class="navbar_item_content" href="mysetting?email={email}"> My Setting </a>
            </div>
            <div class="navbar_item">
                <a href="clear" class="navbar_item_content"> Log out </a>
            </div>
        </div>
    """
def newpost(username, email, head, message):
    return f"""
        <li class="list_group_item">
            <h4>{head}</h4>
            <h4><small>Post by <a href="viewprofile?email={email}">{username}</a>.</small></h4>
            <p>{message}</p>
        </li>
    """
    # return str(new)
def User(name, email):
    return f"""
        <li class="list_group_item"><a href="viewprofile?email={email}">{name}</a></li>
    """
def Users(users):
    content = ""
    for user in users:
        content += User(user['username'], user['email'])
    return content

def DashBoard(login, user, users):
    with open("./MainPage.html", "r") as fl:
        contents = fl.readlines()
    # TODO: JUST A EXAMPLE
    contents.insert(71, newpost("Jack", "2@abc.com", "TEST", "This is a test post"))
    contents.insert(47, Users(users))
    if login:
        contents.insert(28, Login_nvabar(user['email']))
    else:
        contents.insert(28, No_login_nvabar())

    response = ''.join(contents)
    return response
