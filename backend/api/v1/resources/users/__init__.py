
from marshmallow import Schema, fields

from backend.api.v1 import v1_api
from .user_collection import UserCollection
from .user_singleton import UserSingleton
from .user_delete import Users_delete


v1_api.add_resource(UserCollection, '/users')
v1_api.add_resource(UserSingleton, '/users/<int:user_id>')
v1_api.add_resource(Users_delete, '/users/delete')


class UserSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    email = fields.String()
