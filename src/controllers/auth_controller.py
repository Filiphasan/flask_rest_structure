from flask_restx import Resource, fields, Namespace
from flask import request
from src.schemas.auth_schema import AuthSchema
from src.services.auth_service import login

auth_schema = AuthSchema()

auth_ns = Namespace("auth", description="Auth Operation")

login_model = auth_ns.model("Login", {
    "email" : fields.String(),
    "password" : fields.String()
})

login_success = auth_ns.model("Login Success", {
    'access_token': fields.String()
})

@auth_ns.route("/")
class AuthResource(Resource):
    @auth_ns.doc("Login")
    @auth_ns.expect(login_model)
    @auth_ns.response(200, "Login Success", login_success)
    def post(self):
        req_json = request.get_json()
        data = auth_schema.load(req_json)
        return login(data=data)
