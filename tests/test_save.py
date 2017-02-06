#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:  Dominik Gresch <greschd@gmx.ch>
# Date:    20.07.2016 15:16:30 CEST
# File:    test_encoding.py

import os
import json
import pickle
import tempfile

import pytest
import msgpack
import numpy as np

from fsc.iohelper import SerializerDispatch, encoding

EXACT_MSGPACK_FAILS = ['foo']
EXACT_MSGPACK_WORKS = [None, True, False, [1, 2, 3], 1, 1.2, 1 + 2j]
NO_TYPE = [np.int32(1), np.float64(1.2), np.bool_(False), np.bool_(True)]

IO_HANDLER = SerializerDispatch(encoding.default)

@pytest.mark.parametrize('serializer', [pickle, msgpack, json]) 
@pytest.mark.parametrize('obj', EXACT_MSGPACK_WORKS)
def test_consistency_exact(obj, serializer):
    with tempfile.NamedTemporaryFile(mode='w+') as f:
        IO_HANDLER.save(obj, f.name, serializer=serializer)
        res = IO_HANDLER.load(f.name, serializer=serializer)
    assert obj == res
    assert type(obj) == type(res)

@pytest.mark.parametrize('serializer', [pickle, json]) 
@pytest.mark.parametrize('obj', EXACT_MSGPACK_FAILS)
def test_consistency_exact_no_msgpack(obj, serializer):
    with tempfile.NamedTemporaryFile(mode='w+') as f:
        IO_HANDLER.save(obj, f.name, serializer=serializer)
        res = IO_HANDLER.load(f.name, serializer=serializer)
    assert obj == res
    assert type(obj) == type(res)

@pytest.mark.parametrize('serializer', [pickle, msgpack, json]) 
@pytest.mark.parametrize('obj', NO_TYPE)
def test_consistency_notype(obj, serializer):
    with tempfile.NamedTemporaryFile(mode='w+') as f:
        IO_HANDLER.save(obj, f.name, serializer=serializer)
        res = IO_HANDLER.load(f.name, serializer=serializer)
    assert obj == res

@pytest.mark.parametrize('ending', ['.json', '.msgpack', '.p', '.pickle', '.JsoN', '.MsgPack', '.P', '.PicKle']) 
@pytest.mark.parametrize('obj', NO_TYPE + EXACT_MSGPACK_WORKS)
def test_implicit_serializer(obj, ending):
    filename = 'tmpfile' + ending
    IO_HANDLER.save(obj, filename)
    res = IO_HANDLER.load(filename)
    assert obj == res
    os.remove(filename)

def test_invalid_path():
    with pytest.raises(ValueError):
        IO_HANDLER.save(3, 'invalid/path/file.json')
