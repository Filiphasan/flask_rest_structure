from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    id = fields.Int()
    