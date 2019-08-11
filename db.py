#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 03:49:21 2019

@author: miha
"""

import uuid
import datetime

from sqlalchemy import create_engine, ForeignKey, Column
from sqlalchemy import Boolean, Integer, Float, String, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def _ts():
    return datetime.datetime.now()


Base = declarative_base()


class Function(Base):
    __tablename__ = 'functions'
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    created = Column(DateTime, default=datetime.datetime.now)
    name = Column(String)
    tags = Column(JSON)
    
    call = Column(String)
    selectors = Column(JSON)
    inputs = Column(String)  # space separated
    input_format = Column(String)
    group_by = Column(String)  # space separated
    outputs = Column(String)  # space separated
    # schemas = Column(String)  # to another table
    
    trigger = Column(String)
    batching = Column(String)
    timeout = Column(Float)
    backoff_limit = Column(Integer)
    
    def __repr__(self):
        return "Function(name='{}', created='{}')".format(
                self.name, self.version)


class Call(Base):
    __tablename__ = 'calls'
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    function_id = Column(String, ForeignKey("functions.id"))
    call_id = Column(String)
    created = Column(DateTime, default=datetime.datetime.now)
    is_output = Column(Boolean)
    key = Column(String)
    value = Column(String)


engine = create_engine('sqlite:///sqlite.db', echo=True)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

f = Function(name='sin',
             tags={'stage': 'prod'},
             inputs='x',
             outputs='y')

session.add(f)
session.commit()








