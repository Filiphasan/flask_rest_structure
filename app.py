from flask import Flask, jsonify
from dotenv import load_dotenv
from flask_migrate import Migrate
from marshmallow import ValidationError
from werkzeug.exceptions import HTTPException
from flask_restx import Api

from db import db
from ma import ma
import os

from src.controllers.user_controller import UserResource, UserListResource, user_ns
from src.controllers.auth_controller import AuthResource, auth_ns

app = Flask(__name__)
api = Api(app, doc='/doc', title='Flask Rest Structure')

load_dotenv(".env")
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URI", 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
app.secret_key = os.environ.get("SECRET_KEY", 'application_secret_key') #Example: c094b11d-8eb1-450b-949a-f83d9564c923
db.init_app(app)
ma.init_app(app)
migrate = Migrate(app, db)

api.add_namespace(user_ns)
api.add_namespace(auth_ns)

user_ns.add_resource(UserResource, '/<id>')
user_ns.add_resource(UserListResource, '/')
auth_ns.add_resource(AuthResource, '/')

# If you use flask migrate with alembic, don't need this method.
# @app.before_first_request
# def create_table():
#     db.create_all()

@app.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify(error.messages), 400

@app.errorhandler(Exception)
def handler_global_error(error):
    code = 500
    return jsonify({"error":str(error)}), code
    

@app.route("/")
def hello():
    return "hello"


if __name__ == "__main__":
    # db.init_app(app)
    # ma.init_app(app)
    app.run(port=5000, debug=True)