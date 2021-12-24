import uuid
import datetime
import hashlib
import jwt

from src.models.users import UsersModel
from src.schemas.user_schemas import UserGetSchema
from src.services import server_error_obj, not_found_obj, delete_success_obj, email_already_exist_obj

from db import db
from app import app

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
    except Exception as error:
        return server_error_obj, 500

def get_all_users():
    try:
        users = UsersModel.query.filter_by(is_deleted=False).all()
        if users:
            return users_schema.dump(users)
        else:
            return not_found_obj, 404
    except Exception as error:
        return server_error_obj, 500

def get_user_id(user_id : str):
    try:
        user = UsersModel.find_by_id(user_id)
        if user:
            return user_schema.dump(user)
        else:
            return not_found_obj, 404
    except:
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
    except Exception as error:
        return server_error_obj, 500

def update_user(user_data, id: str):
    try:
        user = UsersModel.find_by_id(id)
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

def soft_delete_user(user_id: str):
    try:
        user = UsersModel.query.get(user_id)
        if user:
            user.is_deleted = True
            user.updated_at = datetime.datetime.utcnow()
            db.session.commit()
            return delete_success_obj, 200
        return not_found_obj, 404
    except Exception as error:
        return server_error_obj, 500

def hard_delete_user(user_id: str):
    try:
        user = UsersModel.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return delete_success_obj, 200
        return not_found_obj, 404
    except Exception as error:
        return server_error_obj, 500

def create_token(user: UsersModel):
    token = jwt.encode({
        'sub': user.email,
        'exp':  datetime.utcnow()+datetime.timedelta(minutes=10),
        'iat': datetime.utcnow()
    },app.secret_key, algorithm='HS256')
    return token
