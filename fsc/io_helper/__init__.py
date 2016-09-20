#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:  C. Frescolino, D. Gresch
# File:    __init__.py

from ._version import __version__

from . import default_encoding
from ._io_helper import *
set_encoding(default_encoding)
