from typing import Dict
import jwt
import datetime
import hashlib
import os

from src.models.users import UsersModel
from src.services import not_found_obj, email_not_confirmed_obj, server_error_obj

secret_key = os.environ.get("SECRET_KEY", 'application_secret_key')

def token_obj(token: str) -> Dict:
    return {
        'status':'success',
        'token':token
    }

def login(data):
    try:
        email = data['email']
        password = data["password"]
        password_hash = hashlib.md5(password.encode()).hexdigest()
        user = UsersModel.query.filter_by(email=email, password=password_hash).first()
        if user:
            if not user.email_confirmed:
                return email_not_confirmed_obj, 401
            else:
                token = create_token(user=user, role="user")
                return token_obj(token=token), 200
        else:
            return not_found_obj, 404
    except Exception as error:
        return server_error_obj, 500

def create_token(user: UsersModel, role: str):
    token = jwt.encode({
        'sub': user.id,
        'exp': datetime.datetime.now()+datetime.timedelta(minutes=120),
        'iat': datetime.datetime.now(),
        'roles': [role]
    },secret_key, algorithm='HS256')
    return token

