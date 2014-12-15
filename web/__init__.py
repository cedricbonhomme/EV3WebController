#! /usr/bin/env python
# -*- coding: utf-8 -*-

# ***** BEGIN LICENSE BLOCK *****
# This file is part of EV3WebController.
# Copyright (c) 2014 Cédric Bonhomme.
# All rights reserved.
#
#
#
# ***** END LICENSE BLOCK *****

import os
from flask import Flask

#from ev3.ev3dev import Ev3Dev
from ev3.ev3dev import Key, Motor
from ev3.lego import LargeMotor
from ev3.lego import TouchSensor
from ev3.lego import InfraredSensor

import conf

# Create Flask application
app = Flask(__name__)
app.debug = True

# Create a random secrey key so we can use sessions
app.config['SECRET_KEY'] = os.urandom(12)

#Ev3Dev.__init__()
#head = None#Motor(port=Motor.PORT.A)
right_wheel = None#Motor(port=Motor.PORT.B)
left_wheel  = None#Motor(port=Motor.PORT.C)

button = None#TouchSensor()
ir_sensor = None#InfraredSensor()

# Views
#from flask.ext.restful import Api
#api = Api(app, prefix='/api/v1.0')

from web import views
