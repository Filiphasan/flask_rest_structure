from functools import wraps
from flask import request
import jwt
import os

from src.utils import token_not_found_obj, invalid_token_obj

secret_key = os.environ.get("SECRET_KEY", 'application_secret_key')

def token_required(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        if 'Authorization' in request.headers:
            bearer_token = request.headers['Authorization']
            tokenArr = bearer_token.split(" ")
            token = tokenArr[1]
            if not token:
                return token_not_found_obj, 401
            try:
                data = jwt.decode(
                    token, secret_key, algorithms="HS256")
            except:
                return invalid_token_obj, 403
        else:
            return token_not_found_obj, 401
        return func(*args, **kwargs)
    return wrapped