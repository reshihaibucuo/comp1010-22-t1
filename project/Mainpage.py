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
    

def Login_nvabar():
    return """
        <div class="navbar_right_container">
            <div class="navbar_item">
                <a href="login" class="navbar_item_content"> My Profile </a>
            </div>
            <div class="navbar_item">
                <a href="login" class="navbar_item_content"> My Setting </a>
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
            <h4><small>Post by <a href="">{username}</a>.</small></h4>
            <p>{message}</p>
        </li>
    """
    # return str(new)
def Users(name):
    return f"""
        <li class="list_group_item"><a >{name}</a></li>
    """
    # return str(new)
def DashBoard(login):
    with open("./MainPage.html", "r") as fl:
        contents = fl.readlines()
    contents.insert(72, newpost("Test User", "email@email", "TEST", "This is a test post"))
    contents.insert(47, Users("Test name"))
    if login:
        contents.insert(28, Login_nvabar())
    else:
        contents.insert(28, No_login_nvabar())

    response = ''.join(contents)
    return response
