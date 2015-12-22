from flask_restful import Resource, reqparse
import json

from backend import db
from backend.models import User


parser = reqparse.RequestParser()
parser.add_argument('data')


class Users_delete(Resource):
    def post(self):
        args = parser.parse_args()
        di = json.loads(args.data)
        for n, v in di.iteritems():
            temp = User.query.filter(User.id == n).one()
            db.session.delete(temp)
        db.session.commit()
