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

import os
from flask import Flask

from ev3.ev3dev import Motor
#from ev3.lego import LargeMotor
from ev3.lego import TouchSensor
from ev3.lego import InfraredSensor

import conf

# Create Flask application
app = Flask(__name__)
app.debug = True

# Create a random secrey key so we can use sessions
app.config['SECRET_KEY'] = os.urandom(12)

#head = None#Motor(port=Motor.PORT.A)
right_wheel = None
left_wheel  = None
button = None
ir_sensor = None
try:
    right_wheel = Motor(port=Motor.PORT.B)
    left_wheel = Motor(port=Motor.PORT.C)
    button = TouchSensor()
    ir_sensor = InfraredSensor()
except Exception as e:
    pass#raise Exception('You must run the application on the EV3.')

from web import views
