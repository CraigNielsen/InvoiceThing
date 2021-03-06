from backend.api.v1 import v1_api
from .user_collection import UserCollection
from .user_singleton import UserSingleton


v1_api.add_resource(UserCollection,
                    '/users')

v1_api.add_resource(UserSingleton,
                    '/users/<int:user_id>')
