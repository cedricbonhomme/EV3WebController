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

__author__ = "Cedric Bonhomme"
__version__ = "$Revision: 0.5 $"
__date__ = "$Date: 2014/12/15$"
__revision__ = "$Date: 2015/11/08 $"
__copyright__ = "Copyright (c) 2014-2015 Cédric Bonhomme"
__license__ = ""

import time
from flask import render_template, request, session, url_for, redirect

from ev3.ev3dev import Motor

from web.decorators import to_response
from web.lib import movements
from web import app
from web import right_wheel, left_wheel, button, ir_sensor, color_sensor


@app.errorhandler(403)
def authentication_failed(e):
    flash('You do not have enough rights.', 'danger')
    return redirect(url_for('index'))


@app.errorhandler(401)
def authentication_required(e):
    flash('Authenticated required.', 'info')
    return redirect(url_for('index'))


@app.route('/move/<direction>', methods=['GET'])
@app.route('/move/<direction>/<speed>', methods=['GET'])
@to_response
def move(direction="forward", speed=800):
    """
    This endpoint manages the different 'move action': 'forward', 'backward',
    'left', 'right' and 'stop'.
    """
    result = {
                "action": "move",
                "direction": direction,
                "message": "OK"
            }
    return_code = 200

    if direction == 'forward':
        nb_blocks = request.args.get("blocks", None)
        if None is not nb_blocks:
            position = int(nb_blocks) * -1020
            result["message"] = movements.run_position_limited(left_wheel,
                                                        right_wheel, position)
        else:
            left_wheel.run_forever(speed * -1, regulation_mode=False)
            right_wheel.run_forever(speed * -1, regulation_mode=False)

    elif direction == 'backward':
        nb_blocks = request.args.get("blocks", None)
        if None is not nb_blocks:
            position = int(nb_blocks) * 1020
            result["message"] = movements.run_position_limited(left_wheel,
                                                        right_wheel, position)
        else:
            left_wheel.run_forever(speed * 1, regulation_mode=False)
            right_wheel.run_forever(speed * 1, regulation_mode=False)

    elif direction == 'left':
        speed = 600
        forever = request.args.get("forever", None)
        if None is forever:
            movements.rotate(left_wheel, right_wheel, -340, 340, 90, 0)
        else:
            left_wheel.run_forever(speed * -1, regulation_mode=False)
            right_wheel.run_forever(speed, regulation_mode=False)

    elif direction == 'right':
        speed = 600
        forever = request.args.get("forever", None)
        if None is forever:
            movements.rotate(left_wheel, right_wheel, 340, -340, 0, 90)
        else:
            left_wheel.run_forever(speed, regulation_mode=False)
            right_wheel.run_forever(speed * -1, regulation_mode=False)

    elif direction == 'stop':
        left_wheel.stop()
        right_wheel.stop()

    else:
        result["message"], return_code = "Unknown direction", 400


    return result, return_code


@app.route('/sensor/<sensor_name>', methods=['GET'])
@to_response
def sensor(sensor_name=""):
    """
    Returns the value of the selected sensor.
    """
    if sensor_name == "ir_sensor":
        return {"distance": ir_sensor.prox}
    elif sensor_name == "color_sensor":
        return {"rgb": color_sensor.rgb,
                "mode": color_sensor.mode}
    elif sensor_name == "button":
        pass
    else:
        return {"message": "Unknown sensor"}, 400


@app.route('/', methods=['GET'])
def index():
    """
    Graphical Web interface to command the robot.
    """
    return render_template('index.html')
