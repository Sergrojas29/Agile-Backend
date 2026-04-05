from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1, max=50))
    role = fields.Str(validate=validate.Length(max=50), load_default=None)
    is_admin = fields.Bool(load_default=False)
    username = fields.Str(required=True, validate=validate.Length(min=1, max=50))
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.Length(min=8, max=255))

class UserUpdateSchema(Schema):
    name = fields.Str(validate=validate.Length(min=1, max=50))
    role = fields.Str(validate=validate.Length(max=50))
    is_admin = fields.Bool()
    username = fields.Str(validate=validate.Length(min=1, max=50))
    email = fields.Email()
    password = fields.Str(validate=validate.Length(min=8, max=255))