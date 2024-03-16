#!/usr/bin/python3

"""
define class  state


"""
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


class State(Base):
    """
    creating a class state
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
