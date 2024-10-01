from flask import Blueprint, render_template

auth = Blueprint ('auth', __name__)

@auth.route ('/login', methods = ['GET'])
def login ():
    return render_template ("login.html")

@auth.route ('/logout', methods = ['GET'])
def logout ():
    return "<p>logout</p>"

@auth.route ('/sign-up', methods = ['GET'])
def sign_up ():
    return render_template ("sign_up.html")