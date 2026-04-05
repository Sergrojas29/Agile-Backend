from marshmallow import Schema, fields, validate, ValidationError

class ProjectSchema(Schema):
    title = fields.Str(required=True, validate=validate.Length(min=1, max=50))
    description = fields.Str(validate=validate.Length(max=500), load_default=None)
    start_at = fields.Date(load_default=None)
    end_at = fields.Date(required=True)
    owner_id = fields.UUID(required=True)

class ProjectUpdateSchema(Schema):
    title = fields.Str(validate=validate.Length(min=1, max=50))
    description = fields.Str(validate=validate.Length(max=500))
    start_at = fields.Date()
    end_at = fields.Date()
    owner_id = fields.UUID()