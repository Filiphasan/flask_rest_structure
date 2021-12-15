from copy import error
import uuid
import datetime

from db import db
from src.models.users import UsersModel
from typing import Dict, Tuple, List
from schemas.user import UserSchema
from services import server_error_obj

def save_new_user(user_data : UserSchema):
    try:
        user = UsersModel.query.filter_by(email=user_data.email).first()
        if not user:
            new_user = UsersModel(
                id = str(uuid.uuid4()),
                first_name = user_data.first_name,
                last_name = user_data.last_name,
                full_name = user_data.first_name + " " + user_data.last_name,
                username = user_data.username,
                email = user_data.email,
                password = user_data.password,
                email_confirmed = False,
                status = False
            )
            db.session.add(new_user)
            db.session.commit()
            return True
        else:
            return False
    except Exception as error:
        return server_error_obj, 500

def get_all_users():
    try:
        return UsersModel.query.filter_by(is_deleted=False).all()
    except Exception as error:
        return server_error_obj, 500

def get_user(type: str, data):
    try:
        if type=="mail":
            return UsersModel.query.filter_by(email=data).first()
        elif type=="username":
            return UsersModel.query.filter_by(username=data).first()
        else:
            return UsersModel.query.filter_by(id=data).first()
    except Exception as error:
        return server_error_obj, 500

def update_user(user_data:UserSchema):
    try:
        user = UsersModel.query.get(user_data.id)
        if not user:
            return False
        user.first_name = user_data.first_name
        user.last_name = user_data.last_name
        user.full_name = user_data.first_name + " " + user_data.last_name
        user.username = user_data.username
        user.email = user_data.email
        db.session.commit()
        return True
    except Exception as error:
        return server_error_obj, 500

def soft_delete_user(user_id: str):
    try:
        user = UsersModel.query.get(user_id)
        if user:
            user.is_deleted = True
            db.session.commit()
            return True
        return False
    except Exception as error:
        return server_error_obj, 500

def hard_delete_user(user_id: str):
    try:
        user = UsersModel.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False
    except Exception as error:
        return server_error_obj, 500

def create_token(user: UsersModel):
    try:
        pass
    except Exception as error:
        return server_error_obj, 500
