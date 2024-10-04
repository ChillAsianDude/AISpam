from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

db = SQLAlchemy ()

def create_app ():
    app = Flask (__name__)
    app.config['SECRET_KEY'] = 'BC3415'
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    # externel database link for render
    # format (username, password, host, database name)
    # postgresql://ai_spam_user:SnDrgfmQFOOTEBhCtTrPKPOgS5ByEEnA@dpg-crudpkggph6c73agm96g-a.oregon-postgres.render.com/ai_spam

    # internal database link for render
    # postgresql://ai_spam_user:SnDrgfmQFOOTEBhCtTrPKPOgS5ByEEnA@dpg-crudpkggph6c73agm96g-a/ai_spam    

    db.init_app (app)

    # redirecting the user for when they are not logged in to their account
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)


    from .views import views 
    from .auth import auth

    app.register_blueprint (views, url_prefix='/')
    app.register_blueprint (auth, url_prefix='/')

    from .models import User, Note

    with app.app_context():
        db.create_all()

    @login_manager.user_loader
    def load_user (id):
        return User.query.get (int(id))

    return app
