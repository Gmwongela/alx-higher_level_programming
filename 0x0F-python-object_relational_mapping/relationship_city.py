#!/usr/bin/python3
"""
Module that defines the State class.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from model_city import Base, City

class State(Base):
    """State class to represent the states table."""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
