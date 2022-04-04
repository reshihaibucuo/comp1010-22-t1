# import imp
from datetime import timedelta
from operator import imod
from flask import Flask, redirect, request, url_for, session
from pyhtml import html # TODO add imports
import LoginPage 
from datastore import dataset, jsonread, jsonsave
import helper
import Mainpage
app = Flask(__name__)
app.config['SECRET_KEY'] = '08ccccb937fa253dfb0462d9289aa05d7ae5d3ada0ce1876f5743b1f3b88bd3e'
dataset = jsonread()

@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=10)

@app.route('/', methods=["GET", "POST"])
def homepage():    
    return redirect(url_for('mainpage'))
# Login Pages
@app.route('/login', methods=["GET", "POST"])
def login():
    login_error = False
    if 'user_saved_data' in session:
        return redirect(url_for('mainpage'))
    if 'password' in request.form and 'email' in request.form:  
        login_error = LoginPage.user_login(request.form['email'], request.form['password'], dataset['users'])
        if not login_error:
            session['user_saved_data'] = helper.search_user(dataset['users'], request.form['email'])
            return redirect(url_for('mainpage'))
    return LoginPage.LoginPage(login_error)
    
@app.route('/signup', methods=["GET", "POST"])   
def signup():
    sign_uperror = False
    message = ""
    if 'email' in request.form:
        if request.form['username'] == "":
            message = "Username cannot be empty."
            sign_uperror = True
        elif request.form['password'] =="" or request.form['confirm_password'] =="":
            message = "Password or Confim password cannot be empty."
            sign_uperror = True
        elif request.form['email'] == "":
            message = "E-mail cannot be empty."
            sign_uperror = True
        elif request.form['password'] != request.form['confirm_password']:
            message = "Password and Confirm password password are not the same."
            sign_uperror = True
        else:
            sign_uperror = LoginPage.email_repeat(request.form['email'],dataset['users'])
            message = "E-mail address has existed, please try another one."
        if not sign_uperror:
            dataset['users'].append(helper.new_user(request.form['email'], request.form['password'], request.form['username']))
            jsonsave(dataset)
            return redirect(url_for('login'))
    return LoginPage.RegistrationPage(sign_uperror, message)

@app.route('/resetpassword', methods=["GET", "POST"])
def resetpassword():
    error = False
    if 'email' in request.form:
        error = not LoginPage.email_repeat(request.form['email'], dataset['users'])
        if not error:
            LoginPage.send_password(request.form['email'], helper.search_user(dataset['users'], request.form['email']))
            return redirect(url_for('login'))
    return LoginPage.PasswordReset(error)
# Main Page

@app.route('/mainpage', methods=["GET"])
def mainpage():
    islogin = False
    if 'user_saved_data' in session:
        islogin = True
    return Mainpage.DashBoard(islogin)
    # return f"Here is Main page <br> User = <a href='/'>back</a>{session['user_saved_data']} <br> <a href='/clear'>log out</a>"


@app.route('/clear', methods=["GET"])
def reset():
    session.clear()
    return redirect(url_for('login'))

@app.route('/viewprofile', methods=["GET"])
def viewprofile():
    return "profile "
if __name__ == "__main__":
    app.run(debug=True)


