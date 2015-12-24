from flask_restful import Resource

from backend.models import User
from backend.api.v1.schemas import UserSchema


user_schema = UserSchema()


class UserSingleton(Resource):
    def get(self, user_id):
        user = User.query.filter(User.id == user_id).first()
        if not user:
            # TODO: 404
            raise Exception('User with id: {0} not found.'.format(user_id))
        return user_schema.dump(user).data
