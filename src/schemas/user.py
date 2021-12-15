from marshmallow import Schema, fields, validate
from .messages.user import UserMessages

class UserSchema(Schema):
    id = fields.String()
    first_name = fields.String(required=True, 
        validate=validate.Length(1,30,error=UserMessages.FIRST_NAME_LEN_MSG), 
        error_messages={"required":UserMessages.FIRST_NAME_REQ_MSG})
    last_name = fields.String(required=True, 
        validate=validate.Length(1,30,error=UserMessages.LAST_NAME_LEN_MSG), 
        error_messages={"required":UserMessages.LAST_NAME_REQ_MSG})
    username = fields.String(required=True, 
        validate=validate.Length(1, 35, error="Kullanıcı adı alanı en fazla 35 karakter olmalıdır!"), 
        error_messages={"required":"Kullanıcı adı alanı zorunludur!"})
    email = fields.String(
        required=True, 
        validate=[validate.Regexp("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", error=UserMessages.MAIL_REGEX_MSG),
            validate.Length(10,100,error="")], 
        error_messages={"required":UserMessages.MAIL_REQ_MSG})
    password = fields.String(required=True, 
        validate=[validate.Length(6, 30, error=UserMessages.PASSWORD_LEN_MSG),
            validate.Regexp("[A-Za-z0-9@#$%^&+=]{6,30}",error=UserMessages.PASSWORD_FORMAT_MSG)],
        error_messages={"required":UserMessages.PASSWORD_REQ_MSG})
