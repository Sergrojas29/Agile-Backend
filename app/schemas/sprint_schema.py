from marshmallow import Schema, fields, validate

class SprintSchema(Schema):
    title = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    start_at = fields.Date(load_default=None)
    end_at = fields.Date(required=True)
    project_id = fields.UUID(required=True)

class SprintUpdateSchema(Schema):
    title = fields.Str(validate=validate.Length(min=1, max=100))
    start_at = fields.Date()
    end_at = fields.Date()
    project_id = fields.UUID()