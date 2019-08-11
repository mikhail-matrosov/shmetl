#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 03:49:21 2019

@author: miha
"""

from uuid import uuid4
import datetime

from sqlalchemy import create_engine, ForeignKey, Column
from sqlalchemy import Boolean, Integer, Float, String, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


# from uuid import uuid4, UUID
#import pickle
#from hashlib import sha256
#salt = 'gkauw65w1'
#def gen_uuid(o):
#    return str(UUID(bytes=sha256(pickle.dumps((o, salt))).digest()[:16]))


Base = declarative_base()


class Function(Base):
    __tablename__ = 'functions'
    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    created = Column(DateTime, default=datetime.datetime.now)
    name = Column(String)
    tags = Column(JSON)

    call = Column(String)
    selectors = Column(JSON)
    inputs = Column(JSON)
    input_format = Column(String)
    group_by = Column(JSON)
    outputs = Column(JSON)
    # schemas = Column(String)  # to another table

    trigger = Column(String)
    batching = Column(String)
    timeout = Column(Float)
    backoff_limit = Column(Integer)

    calls = relationship("Call")

    def __repr__(self):
        return "Function(id='{}', name='{}')".format(self.id, self.name)


class Call(Base):
    __tablename__ = 'calls'
    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    function_id = Column(String, ForeignKey("functions.id"))
    created = Column(DateTime, default=datetime.datetime.now)
    tags = Column(JSON)
    data = relationship("CallData")

    def __repr__(self):
        return "Call(id='{}', function_id='{}')".format(self.id, self.function_id)


class CallData(Base):
    __tablename__ = 'calls_data'
    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    call_id = Column(String, ForeignKey("calls.id"))
    created = Column(DateTime, default=datetime.datetime.now)
    is_output = Column(Boolean)
    key = Column(String)
    value = Column(String)


engine = create_engine('sqlite:///sqlite.db', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
