#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:  Dominik Gresch <greschd@gmx.ch>
# Date:    30.03.2016 00:29:06 CEST
# File:    setup.py

import sys

from setuptools import setup

pkgname = 'iohelper'
pkgname_qualified = 'fsc.' + pkgname

with open('doc/description.txt', 'r') as f:
    description = f.read()
try:
    with open('doc/README', 'r') as f:
        readme = f.read()
except IOError:
    readme = description

with open('version.txt', 'r') as f:
    version = f.read().strip()

if sys.version_info < (3, ):
    raise ValueError('only Python 3.x and higher are supported')

setup(
    name=pkgname_qualified,
    version=version,
    packages=[pkgname_qualified, pkgname_qualified + '.encoding'],
    url='http://frescolinogroup.github.io/frescolino/pyiohelper/' +
    '.'.join(version.split('.')[:2]),
    include_package_data=True,
    author='C. Frescolino',
    author_email='frescolino@lists.phys.ethz.ch',
    description=description,
    python_requires='>=3.5',
    install_requires=['msgpack~=1.0', 'fsc.export', 'numpy'],
    long_description=readme,
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3', 'Topic :: Utilities'
    ],
    license='Apache',
)
