from flask_restx import Resource, fields, Namespace
from src.services.user_service import save_new_user, get_all_users, get_user_id, get_user, update_user, soft_delete_user, hard_delete_user

user_ns = Namespace("user", description= "User operations.")
user = user_ns.model("User", {
    'id': fields.String(),
    'first_name': fields.String(),
    'last_name': fields.String(),
    'username': fields.String(),
    'email': fields.String()
})

user_ns.route("/<id>")
user_ns.param('id','User identity UUID')
class UserResource(Resource):
    @user_ns.doc('Get A User')
    @user_ns.marshal_with(user)
    def get(self, id):
        return "SA SA SA"