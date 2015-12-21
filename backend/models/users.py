from sqlalchemy import Column, String

from backend import db
from backend.models import Entity


class User(db.Model, Entity):
    name = Column(String)
    email = Column(String)

    # def __init__(self, name, email):
    #     self.name = name
    #     self.email = email

    def __repr__(self):
        return '<Name: %r ._. email: %r > ' % (self.name, self.email)
