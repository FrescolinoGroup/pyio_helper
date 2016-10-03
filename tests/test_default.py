#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:  Dominik Gresch <greschd@gmx.ch>
# Date:    20.07.2016 15:16:30 CEST
# File:    test.py

import json

import pytest
import numpy as np

from fsc.iohelper.encoding import default

@pytest.mark.parametrize('obj', ['foo', None, True, False, [1, 2, 3], 1, 1.2, 1 + 2j])
def test_consistency_excat(obj):
    res = json.loads(
        json.dumps(
            obj, 
            default=default.encode
        ), 
        object_hook=default.decode
    )
    assert obj == res
    assert type(obj) == type(res)

@pytest.mark.parametrize('obj', [np.int32(1), np.float64(1.2), np.bool_(False), np.bool_(True)])
def test_consistency_notype(obj):
    res = json.loads(
        json.dumps(
            obj, 
            default=default.encode
        ), 
        object_hook=default.decode
    )
    assert obj == res

def test_invalid():
    class Bla:
        def __init__(self, x):
            self.x = x
    with pytest.raises(TypeError):
        json.dumps(Bla(2), default=default.encode)
