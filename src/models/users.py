from db import db


class UsersModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(128), unique=True, nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    full_name = db.Column(db.String(60), nullable=False)
    username = db.Column(db.String(35), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    @property
    def password(self):
        raise AttributeError('password: write-only field')
    
    def check_password(self, password: str):
        return 