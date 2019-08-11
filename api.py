#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 16:39:54 2019

@author: miha
"""

from sqlalchemy.orm.exc import NoResultFound
from db import Function, Call, CallData, session
import scheduler


# Put a new input to start a pipeline
def put(name, data, function_tags={}, call_tags={}):
    assert isinstance(data, dict)
    assert isinstance(function_tags, dict)
    assert isinstance(call_tags, dict)

    outputs = list(data)

    try:
        f = session.query(Function).filter(
            Function.name==name,
            Function.tags==function_tags,
            Function.outputs==outputs
        ).order_by(Function.created.desc()).one()
    except NoResultFound:
        f = Function(name=name, tags=function_tags, outputs=outputs)
        session.add(f)
        session.commit()

    c = Call(function_id=f.id, tags=call_tags)
    c.data = [CallData(is_output=True, key=k, value=v)
              for k, v in data.items()]

    session.add(c)
    session.commit()
    scheduler.notify(c)

    return c


def preview(input_node, output_node):
    pass


def graph():
    pass


def stats():
    '''
    Returns graph and execution stats
    '''
    pass


def prune():
    pass
