#! /usr/bin/env python
#-*- coding: utf-8 -*-

# ***** BEGIN LICENSE BLOCK *****
# This file is part of EV3WebController.
# Copyright (c) 2014-2015 Cédric Bonhomme.
# All rights reserved.
#
#
#
# ***** END LICENSE BLOCK *****

""" Program variables.

This file contain the variables used by the application.
"""

import os, sys

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
PATH = os.path.abspath(".")

DEFAULTS = {"robot_external_address": "http://0.0.0.0:5000",
            "host": "0.0.0.0",
            "port": "5000",
            "https": "false",
            "debug": "true"
            }

try:
    import configparser as confparser
except:
    import ConfigParser as confparser

config = confparser.SafeConfigParser(defaults=DEFAULTS)
config.read(os.path.join(BASE_DIR, "conf/conf.cfg"))

ROBOT_EXTERNAL_ADDRESS = config.get('misc', 'robot_external_address')

WEBSERVER_DEBUG = config.getboolean('webserver', 'debug')
WEBSERVER_HOST = config.get('webserver', 'host')
WEBSERVER_PORT = config.getint('webserver', 'port')
WEBSERVER_HTTPS = config.getboolean('webserver', 'https')
