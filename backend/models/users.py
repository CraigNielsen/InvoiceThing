from sqlalchemy import Column, Integer, String

from backend import db


class User(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

    # def __init__(self, name, email):
    #     self.name = name
    #     self.email = email

    def __repr__(self):
        return '<Name: %r ._. email: %r > ' % (self.name, self.email)
