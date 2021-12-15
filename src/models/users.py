from db import db
# from ...bcrypt import flask_bcyrpt
from bcrypt import flask_bcyrpt
from .base import BaseModel


class UsersModel(BaseModel, db.Model):
    __tablename__ = "users"

    # id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id = db.Column(db.String(128), primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    full_name = db.Column(db.String(60), nullable=False)
    username = db.Column(db.String(35), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email_confirmed = db.Column(db.Boolean, default=False, nullable=False)
    status = db.Column(db.Booelan, default=False, nullable=False)

    @property
    def password(self):
        raise AttributeError('password: write-only field')
    
    def check_password(self, password: str):
        return flask_bcyrpt.generate_password_hash(password).decode('utf-8')

    def __repr__(self):
        return "<User '{}'>".format(self.username)