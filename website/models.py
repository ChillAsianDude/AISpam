from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # notes data, string max  = 100000 characters
    data = db.Column(db.String (100000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # one-to-many relationship with User table
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    # unique = true means there would be no duplicate user
    # db.string (n) = database type, n refers to the max number of characters 
    email = db.Column(db.String (150), unique=True)
    password = db.Column(db.String (150))
    first_name = db.Column(db.String (150))
    note = db.relationship('Note')
