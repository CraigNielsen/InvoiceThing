from flask import Blueprint
from marshmallow import Schema, fields

from backend.models import User


bp = Blueprint('api', __name__)


class UserSchema(Schema):
    id = fields.Integer()
    name = fields.String()


@bp.route('/users')
def get_users():
    user_schema = UserSchema()
    users = User.query.all()
    return user_schema.dumps(users, many=True).data
