from sqlalchemy.orm import Mapped, mapped_column
from . .extensions import db


class Users(db.Model):
    __table__ = db.metadata.tables['users']
