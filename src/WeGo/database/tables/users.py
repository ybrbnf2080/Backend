import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    userID = sa.Column(sa.Integer, primary_key=True)
    userName = sa.Column(sa.String)
    email = sa.Column(sa.String)
    password = sa.Column(sa.String)
    passwordSalt = sa.Column(sa.String)
    dateRegistered = sa.Column(sa.DateTime)
    userType = sa.Column(sa.String)
    accountStatus = sa.Column(sa.String)
