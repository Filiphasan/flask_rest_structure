from marshmallow import Schema, fields, validate
from .messages.user import UserMessages

class UserSchema(Schema):
    id = fields.String(required=False)
    first_name = fields.String(required=True, 
        validate=validate.Length(2,30,error=UserMessages.FIRST_NAME_LEN_MSG), 
        error_messages={"required":UserMessages.FIRST_NAME_REQ_MSG})
    last_name = fields.String(required=True, 
        validate=validate.Length(2,30,error=UserMessages.LAST_NAME_LEN_MSG), 
        error_messages={"required":UserMessages.LAST_NAME_REQ_MSG})
    username = fields.String(required=True, 
        validate=validate.Length(4, 35, error=UserMessages.USERNAME_LEN_MSG), 
        error_messages={"required":UserMessages.USERNAME_REQ_MSG})
    email = fields.String(
        required=True, 
        validate=[validate.Regexp("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", error=UserMessages.MAIL_REGEX_MSG),
            validate.Length(10,100,error=UserMessages.MAIL_LEN_MSG)], 
        error_messages={"required":UserMessages.MAIL_REQ_MSG})
    password = fields.String(required=True, 
        validate=[validate.Length(6, 30, error=UserMessages.PASSWORD_LEN_MSG),
            validate.Regexp("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]",error=UserMessages.PASSWORD_FORMAT_MSG)],
        error_messages={"required":UserMessages.PASSWORD_REQ_MSG})

class UserPwSchema(Schema):
    old_password = fields.String(required=True, error_messages={"required":"Old Password field is required!"})
    new_password = fields.String(required=True, 
        validate=[validate.Length(6, 30, error=UserMessages.PASSWORD_LEN_MSG),
            validate.Regexp("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]",error=UserMessages.PASSWORD_FORMAT_MSG)],
        error_messages={"required":UserMessages.PASSWORD_REQ_MSG})

class UserGetSchema(Schema):
    id = fields.String()
    first_name = fields.String()
    last_name = fields.String()
    username = fields.String()
    email = fields.String()
    email_confirmed = fields.Boolean()
    

