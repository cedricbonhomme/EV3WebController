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

__author__ = "Cedric Bonhomme"
__version__ = "$Revision: 0.1 $"
__date__ = "$Date: 2013/04/15$"
__revision__ = "$Date: 2013/04/15 $"
__copyright__ = "Copyright (c) 2013 Cédric BOnhomme"
__license__ = ""


from flask import render_template, current_app, request, flash, session, \
    url_for, redirect, g, send_from_directory, make_response, abort, Markup
from flask.ext.login import LoginManager, login_user, logout_user, \
    login_required, current_user, AnonymousUserMixin
from flask.ext.principal import Principal, Identity, AnonymousIdentity, \
    identity_changed, identity_loaded, Permission, RoleNeed, UserNeed

import conf
from web.decorators import to_response
from web import app
from web import right_wheel, left_wheel, button, ir_sensor

#
# Default errors
#
@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404

@app.errorhandler(405)
def method_not_allowed(e):
    return render_template('errors/405.html'), 405

@app.errorhandler(500)
def page_not_found(e):
    return render_template('errors/500.html'), 500


def redirect_url(default='profile'):
    return request.args.get('next') or \
           request.referrer or \
           url_for(default)

#
# Management of the permissions
#
principals = Principal(app)

# Create a permission with an admin role's need
admin_permission = Permission(RoleNeed('admin'))

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Please log in to access this page.'
login_manager.login_message_category = 'danger'


@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
    # Set the identity user object
    g.user = current_user
    identity.user = current_user

    # Add the UserNeed to the identity
    if hasattr(current_user, 'id'):
        identity.provides.add(UserNeed(current_user.id))

    # Assuming the User model has a list of roles, update the
    # identity with the roles that the user provides
    if hasattr(current_user, 'roles'):
        for role in current_user.roles:
            identity.provides.add(RoleNeed(role.name))


@app.errorhandler(403)
def authentication_failed(e):
    flash('You do not have enough rights.', 'danger')
    return redirect(url_for('login'))


@app.errorhandler(401)
def authentication_required(e):
    flash('Authenticated required.', 'info')
    return redirect(url_for('login'))


@login_manager.user_loader
def load_user(id):
    # Return an instance of the User model
    return models.User.objects(id=id).first()


@app.before_request
def before_request():
    g.user = current_user

def log_user(user):
    """
    Effectively log the user and update the identity with Flask-Principal.
    """
    login_user(user)
    g.user = user
    session['id'] = str(user.id)

    # Tell Flask-Principal the identity changed
    identity_changed.send(current_app._get_current_object(),
                          identity=Identity(str(user.id)))



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
        pass#left_wheel.run_forever(speed * -1, regulation_mode=False)
        #right_wheel.run_forever(speed * -1, regulation_mode=False)

    elif direction == 'backward':
        try:
            left_wheel.run_forever(speed, regulation_mode=False)
            right_wheel.run_forever(speed, regulation_mode=False)
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


@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')
