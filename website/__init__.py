from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
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

    from .views import views 
    from .auth import auth

    app.register_blueprint (views, url_prefix='/')
    app.register_blueprint (auth, url_prefix='/')

    return app
