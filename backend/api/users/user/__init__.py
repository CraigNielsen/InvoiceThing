from flask import Blueprint, jsonify
from marshmallow import Schema, fields

from backend.models import User



bp_user = Blueprint('api/users', __name__)

class UserSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    email = fields.String()


@bp_user.route('/<userID>')
def get_user(userID):
    user_schema = UserSchema()
    user = User.query.filter(User.id == userID).one()
    return user_schema.dumps(user).data