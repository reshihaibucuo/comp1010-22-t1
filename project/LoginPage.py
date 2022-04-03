from datastore import dataset
import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def LoginPage(error=False):
    if not error:
        with open(".\login.html", "r") as fl:
            response = fl.read()
    else:
        with open(".\login.html", "r") as fl:
            contents = fl.readlines()
        contents.insert(53, """<p style="color:red; font-size: 14px;">The email and/or password you specified are not correct.</p>""")
        response = ''.join(contents)
    return response

def RegistrationPage(error=False, message = ""):
    if not error:
        with open(".\RegistrationPage.html", "r") as fl:
         response = fl.read()
    else:
        with open(".\RegistrationPage.html", "r") as fl:
            contents = fl.readlines()
        # message = "E-mail address has been used, please try again."
        contents.insert(59, f"""<p style="color:red; font-size: 14px;">{message}</p>""")
        response = ''.join(contents)
    return response
    
def PasswordReset(error=False):
    if not error:
        with open(".\PasswordReset.html", "r") as fl:
            response = fl.read()
    else: 
        with open(".\PasswordReset.html", "r") as fl:
            contents = fl.readlines()
        message = "E-mail does not exist."
        contents.insert(51, f"""<p style="color:red; font-size: 14px;">{message}</p>""")
        response = ''.join(contents)
    return response

def user_login(email, password, users):
    find = False
    print(users)
    for user in users:
        if email == user['email'] and password == user['password']:
            find = True
            print("finded")
            break
    return not find
def email_repeat(email, users):
    find = False
    for user in users:
        if user['email'] == email:
            find = True
            break
    return find
def send_password(email, user):
    # Reference Python - Send email using Office 365 https://techexpert.tips/python/python-send-email-using-office-365/
    username = "48739@office.mo.cn"
    password = "Woca7753"
    mail_from = "48739@office.mo.cn"
    mail_to = email
    mail_subject = "Password Forget Test- 1010"
    body = "Password  " + user['password']
    mimemsg = MIMEMultipart()
    mimemsg['From']=mail_from
    mimemsg['To']=mail_to
    mimemsg['Subject']=mail_subject
    mimemsg.attach(MIMEText(body, 'plain'))
    connection = smtplib.SMTP(host='smtp.office365.com', port=587)
    connection.starttls()
    connection.login(username,password)
    connection.send_message(mimemsg)
    connection.quit()