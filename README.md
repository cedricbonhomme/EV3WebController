EV3WebController
================

# Presentation

[EV3WebController](https://bitbucket.org/cedricbonhomme/ev3webcontroller)
provides a Web interface in order to control the Lego Mindstorms EV3 robot.

Tested with Python 3.4 and Python 2.7.

# Installation

## Installation of the system

First, install [ev3dev](http://www.ev3dev.org) on your
Lego Mindstorms EV3 brick.

For the network I recommend the Wireless Nano Adapter *Edimax EW-7811Un* which
is working perfectly out of the box.

## Installation of EV3WebController and the requirements

Then on the robot:

    $ ssh root@192.168.1.16
    $ wget https://bootstrap.pypa.io/get-pip.py
    $ python get-pip.py
    $ wget https://bitbucket.org/cedricbonhomme/ev3webcontroller/get/master.tar.gz
    $ tar -xzvf master.tar.gz
    $ rm master.tar.gz
    $ mv cedricbonhomme-ev3webcontroller-* EV3WebController
    $ cd EV3WebController/
    $ pip install -r requirements.txt
    $ wget https://github.com/topikachu/python-ev3/archive/master.tar.gz
    $ tar -xzvf master.tar.gz
    $ rm master.tar.gz
    $ cd python-ev3-master/
    $ python setup.py install
    $ cd ..
    $ rm -Rf python-ev3-master/
    $ cp conf/conf.cfg-sample conf/conf.cfg

Launch EV3WebController:

    $ python runserver.py
    * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
    * Restarting with stat

# Launch EV3WebController at boot

In order to get EV3WebController start at boot, just create a new systemd
service.

First create the file */etc/systemd/system/brickrc.service*:

    [Unit]
    Description=EV3WebController
    After=multi-user.target

    [Install]
    WantedBy=multi-user.target

    [Service]
    Type=oneshot
    RemainAfterExit=yes
    ExecStart=/root/EV3WebController/run.sh

Then enable the new service:

    $ systemctl daemon-reload
    $ systemctl enable brickrc.service
    $ systemctl restart brickrc.service


# How to use the interface

## Move the robot

    $ GET http://192.168.1.16:5000/move/<direction>/<speed=800>

The value of *speed* is optional. Default is 800.

Acceptable values for *direction*:

* forward;
* backward;
* left;
* right;
* stop.

### Examples

#### Action successfully completed

    $ GET http://192.168.1.16:5000/move/forward
    {"action": "move", "direction": "forward", "message": "OK"}

In this case the HTTP status code returned is 200.

#### Unable to understand the request

    $ GET http://192.168.1.16:5000/move/nowhere
    {"message": "Unknown direction", "direction": "nowhere", "action": "move"}

In this case the HTTP status code returned is 400.

#### Hit a wall

    $ GET http://192.168.1.16:5000/move/forward?blocks=25
    {"action": "move", "direction": "forward", "message": "hit_wall"}

If a wall is detected the current action is stopped and the server
will return the message "hit_wall".

#### End of the labyrinth

    $ GET http://192.168.1.16:5000/move/forward?blocks=20
    {"action": "move", "direction": "forward", "message": "in_target"}

If the red color is detected the current action is stopped and the server
will return the message "in_target".

## Retrieve values from sensors (not yet implemented)

    $ GET http://192.168.1.16:5000/sensor/<sensor_name>

Acceptable values for *sensor_name*:

* button;
* ir_sensor.

### Examples

    $ GET http://192.168.1.16:5000/sensor/ir_sensor
    {"distance": 12}

# Donation

If you wish and if you like *EV3WebController*, you can donate via bitcoin
[1GVmhR9fbBeEh7rP1qNq76jWArDdDQ3otZ](https://blockexplorer.com/address/1GVmhR9fbBeEh7rP1qNq76jWArDdDQ3otZ).
Thank you!

# License

EV3WebController is free software released under the "Modified BSD license"

Copyright (c) 2014-2015 Cédric Bonhomme - https://www.cedricbonhomme.org

# Contact

[Cédric Bonhomme](https://www.cedricbonhomme.org).
