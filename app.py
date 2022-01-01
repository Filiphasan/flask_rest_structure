from flask import Flask, jsonify, Blueprint
from dotenv import load_dotenv
from flask_migrate import Migrate
from marshmallow import ValidationError
from werkzeug.exceptions import HTTPException
from flask_restx import Api

from db import db
from ma import ma
import os

from src.utils.data_seed import seed_data
from src.controllers.user_controller import UserResource, UserListResource, user_ns
from src.controllers.auth_controller import AuthResource, auth_ns

app = Flask(__name__)

@app.route("/")
def server():
    return "Server is Working!"

blueprint = Blueprint("api", __name__, url_prefix="/api")
api = Api(blueprint, doc='/doc', title='Flask Rest Structure')
app.register_blueprint(blueprint)

load_dotenv(".env")
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URI", 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
app.secret_key = os.environ.get("SECRET_KEY", 'application_secret_key') #Example: c094b11d-8eb1-450b-949a-f83d9564c923
db.init_app(app)
ma.init_app(app)
migrate = Migrate(app, db)

# Implement Namespace In Api right below
api.add_namespace(user_ns)
api.add_namespace(auth_ns)

#Implement Resource In NameSpace right below
user_ns.add_resource(UserResource, '/<id>')
user_ns.add_resource(UserListResource, '/')
auth_ns.add_resource(AuthResource, '/')

@app.before_first_request
def create_table():
    # If you use flask migrate with alembic, don't need this method. We create and edit table with flask-migrate.
    # db.create_all()
    seed_data()

# If Marshmallow load data not successful, Marshmallow return ValidationError and error descriptions.
@app.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify(error.messages), 400

# Global Error Handling
@app.errorhandler(Exception)
def handler_global_error(error):
    code = 500
    if isinstance(error, HTTPException):
        code = error.code
    return jsonify({"status":"error","message":str(error)}), code

if __name__ == "__main__":
    # db.init_app(app)
    # ma.init_app(app)
    app.run(port=5000, debug=True)