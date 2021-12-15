from datetime import datetime
from db import db
# from ...bcrypt import flask_bcyrpt
from bcrypt import flask_bcyrpt
from .base import BaseModel


class UsersModel(BaseModel, db.Model):
    __tablename__ = "users"

    # id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id = db.Column(db.String(128), primary_key=True) #User Id best practices, i think
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    full_name = db.Column(db.String(60), nullable=False)
    username = db.Column(db.String(35), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email_confirmed = db.Column(db.Boolean, default=False, nullable=False)
    status = db.Column(db.Booelan, default=False, nullable=False)

    # def __init(self, id, first_name, last_name, full_name, username, email, password_hash):
    #     self.id = id
    #     self.first_name = first_name
    #     self.last_name = last_name
    #     self.full_name = first_name + " " + last_name
    #     self.username = username
    #     self.email = email
    #     self.password = password_hash
    #     self.email_confirmed = False
    #     self.status = False

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password = flask_bcyrpt.generate_password_hash(password).decode("utf-8")
    
    def check_password(self, password: str):
        return flask_bcyrpt.check_password_hash(self.password, password)

    def __repr__(self):
        return "<User '{}'>".format(self.username)