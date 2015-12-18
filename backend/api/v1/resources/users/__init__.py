from flask_restful import Resource, reqparse
from marshmallow import Schema, fields

from backend.api.v1 import v1_api
from backend.models import User
from backend import db


class UserSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    email = fields.String()

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument("email")

class Users_(Resource):

    def get(self):
        user_schema = UserSchema()
        users = User.query.all()
        return user_schema.dump(users, many=True).data

    def post(self):
        args = parser.parse_args()
        tempUser= User()
        tempUser.name= args['name']
        tempUser.email=args['email']
        db.session.add(tempUser)
        db.session.commit()

        # newuser = user
        # print newuser
v1_api.add_resource(Users_, '/users')
