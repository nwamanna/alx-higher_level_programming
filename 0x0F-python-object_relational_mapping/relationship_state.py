#!/usr/bin/python3
""" contains the class definition of a State
    and an instance Base = declarative_base()
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.orm import relationship

metadata = MetaData()
Base = declarative_base(metadata=metadata)


class State(Base):
    """ This class links to MySQL table states in our database
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref="states")
