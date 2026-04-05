from marshmallow import Schema, fields, validate

class TaskSchema(Schema):
    title = fields.Str(required=True, validate=validate.Length(min=1, max=50))
    description = fields.Str(validate=validate.Length(max=500), load_default=None)
    start_at = fields.Date(load_default=None)
    due_at = fields.Date(required=True)
    value = fields.Int(required=True, validate=validate.Range(min=0))
    user_id = fields.UUID(required=True)
    sprint_id = fields.UUID(required=True)

class TaskUpdateSchema(Schema):
    title = fields.Str(validate=validate.Length(min=1, max=50))
    description = fields.Str(validate=validate.Length(max=500))
    start_at = fields.Date()
    due_at = fields.Date()
    value = fields.Int(validate=validate.Range(min=0))
    user_id = fields.UUID()
    sprint_id = fields.UUID()