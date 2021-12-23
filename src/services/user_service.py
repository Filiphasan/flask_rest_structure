import uuid
import datetime

from db import db
from flask_restx import fields, Namespace
from src.models.users import UsersModel
from schemas.user import UserSchema, UserGetSchema
from services import server_error_obj, not_found_obj, delete_success_obj

user_schema = UserGetSchema()
users_schema = UserGetSchema(many=True)

user_ns = Namespace("user", description= "User operations.")
user = user_ns.model("User", {
    'id': fields.String(),
    'first_name': fields.String(),
    'last_name': fields.String(),
    'username': fields.String(),
    'email': fields.String()
})

USER_ALREADY_EXIST = "Girilen mail bilgisi sistemde bulunmaktadır!"

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
            return user_schema.dump(new_user), 201
        else:
            return {'message':USER_ALREADY_EXIST}, 404
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

def get_user_id(id : str):
    try:
        user = UsersModel.find_by_id(id)
        if user:
            return user_schema.dump(user)
        else:
            return not_found_obj, 404
    except:
        return server_error_obj, 500
def get_user(type: str, data):
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
    try:
        pass
    except Exception as error:
        return server_error_obj, 500
