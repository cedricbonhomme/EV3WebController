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
from ev3.lego import ColorSensor
from ev3.lego import InfraredSensor

import conf

# Create Flask application
app = Flask(__name__)
app.debug = True

# Create a random secrey key so we can use sessions
app.config['SECRET_KEY'] = os.urandom(12)

from ev3.ev3dev import Tone
alarm = Tone()

#head = None#Motor(port=Motor.PORT.A)
right_wheel = None
left_wheel  = None
button = None
ir_sensor = None
color_sensor = None
try:
    right_wheel = Motor(port=Motor.PORT.B)
    left_wheel = Motor(port=Motor.PORT.C)
    button = TouchSensor()
    #ir_sensor = InfraredSensor()
    color_sensor = ColorSensor()
    alarm.play(200)
except Exception as e:
    alarm.play(200)
    alarm.play(200)
    raise e


right_wheel.position = 0
left_wheel.position = 0
right_wheel.reset()
left_wheel.reset()

from web import views
