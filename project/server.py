# import imp
from flask import Flask, redirect, request, url_for
from pyhtml import html # TODO add imports
import LoginPage 
app = Flask(__name__)
app.config['SECRET_KEY'] = '08ccccb937fa253dfb0462d9289aa05d7ae5d3ada0ce1876f5743b1f3b88bd3e'

@app.route('/', methods=["GET", "POST"])
def homepage():    
    return redirect(url_for('resetpassword'))

@app.route('/login', methods=["GET", "POST"])
def login():
    login_error = False
    if 'password' in request.form and 'email' in request.form:
        login_error = LoginPage.user_login(request.form['email'], request.form['password'])
        # TODO: load user profile form json file into session.
    return LoginPage.LoginPage(login_error)
    
@app.route('/signup', methods=["GET", "POST"])   
def signup():
    sign_uperror=False
    if 'email' in request.form:
        sign_uperror = LoginPage.email_repeat(request.form['email'])

    return LoginPage.RegistrationPage(sign_uperror)

@app.route('/resetpassword', methods=["GET", "POST"])
def resetpassword():
    return LoginPage.PasswordReset()
if __name__ == "__main__":
    app.run(debug=True)