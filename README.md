EV3WebController
================

# Presentation

This application based on the [Flask](http://flask.pocoo.org/)
microframework provides an interface in order to control the EV3 robot.

Tested with Python 3.4 and Python 2.7.

# How to use the interface

## Move the robot

    $ GET http://192.168.1.10:5000/move/<direction>/<speed=60>

The value of *speed* is optional. Default is 60.

Acceptable values for *direction*:

* forward;
* backward;
* left;
* right;
* stop.

### Examples

    $ GET http://username:password@192.168.1.10:5000/move/forward/50
    {"message": "OK", "direction": "forward", "action": "move"}

In this case the HTTP status code returned is 200.

    $ GET http://127.0.0.1:5000/move/nowhere
    {"message": "Unknown direction", "direction": "nowhere", "action": "move"}

In this case the HTTP status code returned is 400.


## Retrieve values from sensors

    $ GET http://192.168.1.10:5000/sensor/<sensor_name>

Acceptable values for *sensor_name*:

* button;
* ir_sensor.


### Examples

    $ GET http://username:password@192.168.1.10:5000/sensor/ir_sensor
    {"distance": 12}


# License

cve-search is free software released under the "Modified BSD license"

Copyright (c) 2013-2015 Cédric Bonhomme - https://www.cedricbonhomme.org

# Contact

[Cédric Bonhomme](https://www.cedricbonhomme.org).
