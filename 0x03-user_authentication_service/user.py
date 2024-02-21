#!/usr/bin/env python3
"""
User module
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from typing import TypeVar

Base = declarative_base()


class User(Base):
    """
    User class
    """
    __tablename__ = 'users'

    id: int = Column(Integer, primary_key=True)
    email: str = Column(String(250), nullable=False)
    hashed_password: str = Column(String(250), nullable=False)
    session_id: str = Column(String(250), nullable=True)
    reset_token: str = Column(String(250), nullable=True)


def db_init():
    engine = create_engine('sqlite:///users.db', echo=True)
    Base.metadata.create_all(bind=engine)


def create_user(
        email: str,
        hashed_password: str,
        session_id: str = None,
        reset_token: str = None):
    user = User(
        email=email,
        hashed_password=hashed_password,
        session_id=session_id,
        reset_token=reset_token)
    return user


def main():
    print(User.__tablename__)

    for column in User.__table__.columns:
        print("{}: {}".format(column, column.type))


if __name__ == "__main__":
    main()
