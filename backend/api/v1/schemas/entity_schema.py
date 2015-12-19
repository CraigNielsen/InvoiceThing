from marshmallow import Schema, fields


class EntitySchema(Schema):
    id = fields.Integer()
    created_on = fields.DateTime()
