from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint ('views', __name__)

@views.route ('/', methods = ['GET'])
@login_required
def home ():
    return render_template ("home.html", user=current_user)

@views.route ('/about', methods = ['GET'])
def about ():
    return render_template ("about.html",user=current_user)

@views.route ('/learning', methods = ['GET'])
def learning ():
    return render_template ("learning.html",user=current_user)

@views.route ('/explore', methods = ['GET'])
def explore ():
    return render_template ("explore.html",user=current_user)

@views.route ('/more', methods = ['GET'])
def more ():
    return render_template ("more.html", user=current_user)

@views.route ('/challenge', methods = ['GET'])
def challenge ():
    return render_template ("challenge.html", user=current_user)

@views.route ('/profile', methods = ['GET'])
def profile ():
    return render_template ("profile.html", user=current_user)

@views.route ('/settings', methods = ['GET'])
def settings ():
    return render_template ("settings.html", user=current_user)