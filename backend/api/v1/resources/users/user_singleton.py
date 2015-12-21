from flask_restful import Resource

from backend.models import User
from backend.api.v1.schemas import UserSchema


class UserSingleton(Resource):
    def get(self, user_id):
        user_schema = UserSchema()
        user = User.query.filter(User.id == user_id).first()
        return user_schema.dump(user).data
