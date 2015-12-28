from flask_restful import Resource, reqparse

from backend import db
from backend.models import User
from backend.api.v1.schemas import UserSchema


user_schema = UserSchema()

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('email')


class UserCollection(Resource):
    def get(self):
        users = User.query.all()
        return user_schema.dump(users, many=True).data

    def post(self):
        args = parser.parse_args()
        user = User()
        for key, value in args.items():
            setattr(user, key, value)
        db.session.add(user)
        db.session.commit()
        return user_schema.dump(user).data
