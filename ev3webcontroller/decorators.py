#! /usr/bin/env python
# -*- coding: utf-8 -*-

# ***** BEGIN LICENSE BLOCK *****
# This file is part of EV3WebController.
# Copyright (c) 2014-2015 Cédric Bonhomme.
# All rights reserved.
#
#
#
# ***** END LICENSE BLOCK *****

import json
from functools import wraps
from threading import Thread
from flask import Response
from web.lib.utils import default_handler

def async(f):
    """
    This decorator enables to send email in a new thread.
    This prevent the server to freeze.
    """
    def wrapper(*args, **kwargs):
        thr = Thread(target = f, args = args, kwargs = kwargs)
        thr.start()
    return wrapper

def to_response(func):
    """
    Cast results of func as a result, and try to extract
    a status_code for the Response object.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        status_code = 200
        result = func(*args, **kwargs)
        if isinstance(result, Response):
            return result
        elif isinstance(result, tuple):
            result, status_code = result
        return Response(json.dumps(result, default=default_handler),
                        status=status_code)
    return wrapper
