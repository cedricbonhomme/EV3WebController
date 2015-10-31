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
__version__ = "$Revision: 0.3 $"
__date__ = "$Date: 2014/12/15$"
__revision__ = "$Date: 2015/10/31 $"
__copyright__ = "Copyright (c) 2014-2015 Cédric BOnhomme"
__license__ = ""

from flask import render_template, current_app, request, session, \
    url_for, redirect, g, send_from_directory, make_response, abort, Markup
from flask.ext.login import LoginManager, login_user, logout_user, \
    login_required, current_user, AnonymousUserMixin

import conf
from web.decorators import to_response
from web import app
from web import right_wheel, left_wheel, button, ir_sensor

login_manager = LoginManager(app)
login_manager.login_view = 'index'
login_manager.login_message = 'Please log in to access this page.'
login_manager.login_message_category = 'danger'

@app.errorhandler(403)
def authentication_failed(e):
    flash('You do not have enough rights.', 'danger')
    return redirect(url_for('index'))

@app.errorhandler(401)
def authentication_required(e):
    flash('Authenticated required.', 'info')
    return redirect(url_for('index'))

@login_manager.user_loader
def load_user(id):
    # Return an instance of the User model
    return models.User.objects(id=id).first()


@app.route('/move/<direction>', methods=['GET'])
@app.route('/move/<direction>/<speed>', methods=['GET'])
@to_response
def move(direction="forward", speed=60):
    """
    """
    result = {
                "action": "move",
                "direction": direction,
                "message": "OK"
            }
    return_code = 200

    if direction == 'forward':
        left_wheel.run_forever(speed * 1, regulation_mode=False)
        right_wheel.run_forever(speed * 1, regulation_mode=False)

    elif direction == 'backward':
        try:
            left_wheel.run_forever(speed * -1, regulation_mode=False)
            right_wheel.run_forever(speed * -1, regulation_mode=False)
        except Exception as e:
            result["message"], return_code = "error", 400

    elif direction == 'left':
        left_wheel.run_forever(speed, regulation_mode=False)
        right_wheel.run_forever(speed * -1, regulation_mode=False)

    elif direction == 'right':
        left_wheel.run_forever(speed * -1, regulation_mode=False)
        right_wheel.run_forever(speed, regulation_mode=False)

    elif direction == 'stop':
        left_wheel.stop()
        right_wheel.stop()

    else:
        result["message"], return_code = "Unknown direction", 400


    return result, return_code


@app.route('/sensor/<sensor_name>', methods=['GET'])
def sensor(sensor_name=""):
    """
    """
    if sensor_name == "ir_sensor":
        return {"distance": ir_sensor.prox}
    elif sensor_name == "button":
        pass
    else:
        return {"message": "Unknown sensor"}, 400


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
