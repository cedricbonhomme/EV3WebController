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

"""Bootstrap

Required imports and code execution for basic functionning.
"""

import os
if os.geteuid() != 0:
    pass#raise Exception('You must run the application as root on the EV3.')
import sys
if 'threading' in sys.modules:
    raise Exception('threading module loaded before patching!')
import conf
import logging
