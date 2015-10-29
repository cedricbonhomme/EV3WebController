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

import sys
if 'threading' in sys.modules:
    raise Exception('threading module loaded before patching!')
import conf
import logging
