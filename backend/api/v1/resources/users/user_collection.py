from flask_restful import Resource, reqparse

from backend import db
from backend.models import User
from backend.api.v1.schemas import UserSchema


parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('email')


class UserCollection(Resource):
    def get(self):
        user_schema = UserSchema()
        users = User.query.all()
        return user_schema.dump(users, many=True).data

    def post(self):
        user_schema = UserSchema()
        args = parser.parse_args()
        user = User()
        user.name = args['name']
        user.email = args['email']
        db.session.add(user)
        db.session.commit()
        return user_schema.dump(user).data
