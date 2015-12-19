from flask_restful import Resource
from marshmallow import Schema, fields

from backend.models import User
from backend.api.v1 import v1_api


# bp_user = Blueprint('api/users', __name__)

class UserSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    email = fields.String()


class User_(Resource):

    def get(self, userID):
        user_schema = UserSchema()
        user = User.query.filter(User.id == userID).one()
        return user_schema.dump(user).data


v1_api.add_resource(User_, '/users/<int:userID>')
