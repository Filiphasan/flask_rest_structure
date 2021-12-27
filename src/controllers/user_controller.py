from flask_restx import Resource, fields, Namespace
from flask import request
from src.schemas.user_schemas import UserSchema
from src.services.user_service import save_new_user, get_all_users, get_user_id, get_user, update_user, soft_delete_user, hard_delete_user
from src.utils.decorator import token_required

user_ns = Namespace("api/user", description= "User operations.")
user = user_ns.model("User", {
    'id': fields.String(),
    'first_name': fields.String(),
    'last_name': fields.String(),
    'username': fields.String(),
    'email': fields.String()
})

user_update = user_ns.model("UserUpdate", {
    'id': fields.String(),
    'first_name': fields.String(),
    'last_name': fields.String(),
    'username': fields.String(),
    'email': fields.String(),
    'password': fields.String()
})

user_add= user_ns.model("UserCreate", {
    'first_name': fields.String(),
    'last_name': fields.String(),
    'username': fields.String(),
    'email': fields.String(),
    'password': fields.String()
})

user_add_or_update_schema = UserSchema()


@user_ns.route("/<id>")
@user_ns.param('id','User identity UUID')
class UserResource(Resource):
    @user_ns.doc('Get A User')
    @user_ns.response(200,"Get Success",model= user)
    def get(self, id):
        result = get_user_id(id)
        return result
    
    @user_ns.doc("Update A User")
    @user_ns.response(200,"Update Success.",model= user)
    @user_ns.expect(user_update)
    def put(self, id):
        req_json = request.get_json()
        data = user_add_or_update_schema.load(req_json)
        result = update_user(data, id)
        return result
    
    @user_ns.doc("Delete A User")
    def delete(self, id):
        result = soft_delete_user(id)
        return result

@user_ns.route("/")
class UserListResource(Resource):
    @user_ns.doc("Get User List")
    @user_ns.response(200,"Get Success",model= [user])
    def get(self):
        result = get_all_users(email_confirmed=False)
        return result
    
    @user_ns.doc("Create A User")
    @user_ns.response(201,"Add Success.",model= user)
    @user_ns.expect(user_add)
    def post(self):
        req_json = request.get_json()
        data = user_add_or_update_schema.load(req_json)
        result = save_new_user(data)
        return result

    