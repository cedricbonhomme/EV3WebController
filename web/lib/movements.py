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
__date__ = "$Date: 2015/11/05$"
__revision__ = "$Date: 2015/11/10 $"
__copyright__ = "Copyright (c) 2014-2015 Cédric Bonhomme"
__license__ = ""

import time
from ev3.ev3dev import Motor

from web import button, color_sensor

def stop(motorA, motorB):
    """
    Stop the motors.
    """
    motorA.stop()
    motorB.stop()
    time.sleep(0.6)

def check_stop_condition(motorA, motorB):
    """
    Wait for the completion of the command before sending the result.
    """
    result_message = []
    while "running" in motorA.state.split(" ") and \
                        "running" in motorB.state.split(" "):
        time.sleep(0.1)
        if button.is_pushed:
            # stop the motor
            stop(motorA, motorB)
            # go a few centimers backward
            motorA.position = 0
            motorA.run_position_limited(position_sp=180, speed_sp=500,
                   stop_mode=Motor.STOP_MODE.BRAKE, ramp_up_sp=1000,
                   ramp_down_sp=1000)
            motorB.position = 0
            motorB.run_position_limited(position_sp=180, speed_sp=500,
                   stop_mode=Motor.STOP_MODE.BRAKE, ramp_up_sp=1000,
                   amp_down_sp=1000)
            while "running" in motorA.state.split(" ") and \
                                "running" in motorB.state.split(" "):
                time.sleep(0.1)
            result_message.append("hit_wall")
        if color_sensor.colors[color_sensor.color] == "red":
            stop(motorA, motorB)
            result_message.append("in_target")
    else:
        time.sleep(0.5)
    return ";".join(result_message) if len(result_message) != 0 else "OK"


def run_position_limited(motorA, motorB, position):
    """
    Run for a limitied position.
    """
    motorA.position = 0
    motorA.run_position_limited(position_sp=position, speed_sp=500,
                   stop_mode=Motor.STOP_MODE.BRAKE, ramp_up_sp=1000,
                   ramp_down_sp=1000)
    motorB.position = 0
    motorB.run_position_limited(position_sp=position, speed_sp=500,
                   stop_mode=Motor.STOP_MODE.BRAKE, ramp_up_sp=1000,
                   amp_down_sp=1000)
    return check_stop_condition(motorA, motorB)

def rotate(motorA, motorB, position1, position2, initial_position1, initial_position2):
    """
    Rotate.
    """
    motorA.position = initial_position1
    motorA.run_position_limited(position_sp=position1, speed_sp=600,
                   stop_mode=Motor.STOP_MODE.BRAKE, ramp_up_sp=1000,
                   ramp_down_sp=1000)
    motorB.position= initial_position2
    motorB.run_position_limited(position_sp=position2, speed_sp=600,
                   stop_mode=Motor.STOP_MODE.BRAKE, ramp_up_sp=1000,
                   amp_down_sp=1000)
    return check_stop_condition(motorA, motorB)
