from email import message
from pyhtml import p
# from LoginPage import dataset

def LoginPage(error=False):
    if not error:
        with open(".\login.html", "r") as fl:
            response = fl.read()
    else:
        with open(".\login.html", "r") as fl:
            contents = fl.readlines()
        contents.insert(25, """<p style="color:red; font-size: 14px;">The email and/or password you specified are not correct.</p>""")
        response = ''.join(contents)
    return response

def RegistrationPage(error=False):
    if not error:
        with open(".\RegistrationPage.html", "r") as fl:
         response = fl.read()
    else:
        with open(".\RegistrationPage.html", "r") as fl:
            contents = fl.readlines()
        message = "E-mail address has been used, please try again."
        contents.insert(34, f"""<p style="color:red; font-size: 14px;">{message}</p>""")
        response = ''.join(contents)
    return response
    
def PasswordReset():
    with open(".\PasswordReset.html", "r") as fl:
         response = fl.read()
    return response

def user_login(email, password):
    return True
def email_repeat(email):
    return True
def check_email(email):
    return True