from os import error
import uuid
import datetime
import hashlib

from src.models.users import UsersModel
from src.schemas.user_schemas import UserGetSchema
from src.services import server_error_obj, not_found_obj, delete_success_obj, email_already_exist_obj, password_wrong_obj, password_change_success_obj

from db import db

user_schema = UserGetSchema()
users_schema = UserGetSchema(many=True)


def save_new_user(user_data):
    try:
        user = UsersModel.query.filter_by(email=user_data['email']).first()
        if user:
            return email_already_exist_obj, 400
        else:
            password = user_data['password']
            new_user = UsersModel(
                id = str(uuid.uuid4()),
                first_name= user_data['first_name'],
                last_name= user_data['last_name'],
                email= user_data['email'],
                username= user_data['username'],
                password_hash= hashlib.md5(password.encode()).hexdigest()
            )
            db.session.add(new_user)
            db.session.commit()
            return user_schema.dump(new_user), 201
    except:
        return server_error_obj, 500

def get_all_users(is_deleted=False, email_confirmed=True):
    try:
        users = UsersModel.query.filter_by(is_deleted=is_deleted, email_confirmed=email_confirmed).all()
        if users:
            return users_schema.dump(users), 200
        else:
            return not_found_obj, 404
    except:
        return server_error_obj, 500

def get_user_id(user_id : str):
    try:
        user = UsersModel.query.get(user_id)
        if user:
            return user_schema.dump(user)
        else:
            return not_found_obj, 404
    except Exception as err:
        return server_error_obj, 500
def get_user(type: str, data: str):
    try:
        if type=="mail":
            user = UsersModel.query.filter_by(email=data).first()
            if user:
                return user_schema.dump(user)
            else:
                return not_found_obj, 404
        else:
            user = UsersModel.query.filter_by(username=data).first()
            if user:
                return user_schema.dump(user)
            else:
                return not_found_obj, 404
    except:
        return server_error_obj, 500

def update_user(user_data, id: str):
    try:
        user = UsersModel.query.get(id)
        if not user:
            return False
        user.first_name = user_data["first_name"]
        user.last_name = user_data["last_name"]
        user.full_name = user_data["first_name"] + " " + user_data["last_name"]
        user.username = user_data["username"]
        user.email = user_data["email"]
        user.updated_at = datetime.datetime.utcnow()
        db.session.commit()
        return user_schema.dump(user)
    except Exception as error:
        return server_error_obj, 500

def edit_user_password(id: str, data):
    try:
        new_password = data["new_password"]
        old_password = data["old_password"]
        user = UsersModel.query.get(id)
        old_pw_hash = hashlib.md5(old_password.encode()).hexdigest()
        if user:
            if user.password != old_pw_hash:
                return password_wrong_obj, 400
            new_pw_hash = hashlib.md5(new_password.encode()).hexdigest()
            user.password = new_pw_hash
            user.updated_at = datetime.datetime.utcnow()
            db.session.commit()
            return password_change_success_obj, 200
        return not_found_obj, 404
    except Exception as error:
        return server_error_obj, 500

def soft_delete_user(user_id: str):
    try:
        user = UsersModel.query.get(user_id)
        if user:
            user.is_deleted = True
            user.updated_at = datetime.datetime.utcnow()
            db.session.commit()
            return delete_success_obj, 200
        return not_found_obj, 404
    except:
        return server_error_obj, 500

def hard_delete_user(user_id: str):
    try:
        user = UsersModel.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return delete_success_obj, 200
        return not_found_obj, 404
    except:
        return server_error_obj, 500
