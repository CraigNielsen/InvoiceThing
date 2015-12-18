from flask_restful import Resource
from marshmallow import Schema, fields

from backend.api.v1 import v1_api
from backend.models import User


class UserSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    email = fields.String()


class Users_(Resource):

    def get(self):
        user_schema = UserSchema()
        users = User.query.all()
        return user_schema.dump(users, many=True).data
v1_api.add_resource(Users_, '/users')
