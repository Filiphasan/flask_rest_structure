from flask import Flask, json, jsonify
from dotenv import load_dotenv
from flask_migrate import Migrate
from marshmallow import ValidationError
from werkzeug.exceptions import HTTPException

from db import db
from ma import ma
from bcrypt import flask_bcyrpt
import os

from src.models.users import UsersModel

app = Flask(__name__)
load_dotenv(".env")
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URI", 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
app.secret_key = 'secret_key'
db.init_app(app)
ma.init_app(app)
flask_bcyrpt.init_app(app)
migrate = Migrate(app, db)


@app.before_first_request
def create_table():
    db.create_all()

@app.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify(error.messages), 400

@app.errorhandler(Exception)
def handler_global_error(error):
    code = 500
    if isinstance(error, HTTPException):
        code = error.code
        return jsonify({"error":str(error)}), code
    return jsonify({"error":"Internal Server Error!"}), code
    

@app.route("/")
def hello():
    return "hello"


if __name__ == "__main__":
    # db.init_app(app)
    # ma.init_app(app)
    app.run(port=5000, debug=True)