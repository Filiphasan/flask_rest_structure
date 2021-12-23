from flask_restx import Resource, fields, Namespace
from flask import request
from src.schemas.user_schemas import UserSchema
from src.services.user_service import save_new_user, get_all_users, get_user_id, get_user, update_user, soft_delete_user, hard_delete_user

user_ns = Namespace("user", description= "User operations.")
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

user_ns.route("/<id>")
user_ns.param('id','User identity UUID')
class UserResource(Resource):
    @user_ns.doc('Get A User')
    @user_ns.marshal_with(user)
    def get(self, id):
        get_user_id(id)
    
    @user_ns.doc("Update A User")
    @user_ns.expect(user_update)
    def put(self, id):
        req_json = request.get_json()
        data = user_add_or_update_schema.load(req_json)
        update_user(data, id)

user_ns.route("/")
class UserListResource(Resource):
    @user_ns.doc("Get User List")
    def get(self):
        get_all_users()
    
    @user_ns.doc("Create A User")
    @user_ns.expect(user_add)
    def post(self):
        req_json = request.get_json()
        data = user_add_or_update_schema.load(req_json)
        result = save_new_user(data)
        return result

    