from marshmallow import Schema, fields, validate

class AuthSchema(Schema):
    email = fields.String(required=True, 
        validate=validate.Regexp("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", error='Email is wrong!'),
        error_messages={'required':'Email field is required!'})
    password = fields.String(required=True, error_messages={'required':'Password field is required!'})