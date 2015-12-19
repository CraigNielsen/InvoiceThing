from marshmallow import fields

from . import EntitySchema


class UserSchema(EntitySchema):
    id = fields.Integer()
    name = fields.String()
    email = fields.String()
