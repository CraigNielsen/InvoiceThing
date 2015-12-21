import datetime
from sqlalchemy import Column, Integer
from sqlalchemy import DateTime

from backend import db


class Entity(object):
    id = Column(Integer, primary_key=True)
    created_on = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        nullable=False,
    )
    last_updated_on = db.Column(
        db.DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
        nullable=False,
    )


from .users import User
