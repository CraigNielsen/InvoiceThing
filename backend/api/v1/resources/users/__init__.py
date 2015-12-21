<<<<<<< HEAD
from flask_restful import Resource, reqparse
from marshmallow import Schema, fields
import json
from backend.api.v1 import v1_api
from backend.models import User
from backend import db
from backend.api.v1 import v1_api
from .user_collection import UserCollection
from .user_singleton import UserSingleton


v1_api.add_resource(UserCollection, '/users')
v1_api.add_resource(UserSingleton, '/users/<int:user_id>')


class UserSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    email = fields.String()

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument("email")
parser.add_argument('data')


class Users_(Resource):

    def get(self):
        user_schema = UserSchema()
        users = User.query.all()
        return user_schema.dump(users, many=True).data

    def post(self):
        args = parser.parse_args()
        tempUser = User()
        tempUser.name = args['name']
        tempUser.email = args['email']
        db.session.add(tempUser)
        db.session.commit()

        # newuser = user
        # print newuser
v1_api.add_resource(Users_, '/users')


class Users_delete(Resource):
    def post(self):
        args = parser.parse_args()
        # pdb.set_trace()
        di = json.loads(args.data)
        for n, v in di.iteritems():
            temp = User.query.filter(User.id == n).one()
            db.session.delete(temp)
        db.session.commit()
        # print json.loads(args.data)
v1_api.add_resource(Users_delete, '/users/delete')

