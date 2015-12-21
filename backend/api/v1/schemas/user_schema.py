from marshmallow import fields

from . import EntitySchema


class UserSchema(EntitySchema):
    name = fields.String()
    email = fields.String()
