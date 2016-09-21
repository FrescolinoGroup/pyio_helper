#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:  C. Frescolino, D. Gresch
# File:    __init__.py

"""
A tool for saving / loading data from file with a given encoding and decoding function.
"""

from ._version import __version__

from . import encoding
from ._io_helper import *
