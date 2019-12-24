#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: José Sánchez-Gallego (gallegoj@uw.edu)
# @Date: 2019-12-17
# @Filename: build.py
# @License: BSD 3-clause (http://www.opensource.org/licenses/BSD-3-Clause)

# Extension build system using poetry, see https://github.com/python-poetry/poetry/issues/11.

import glob
import os
import sys

from setuptools import Extension


LIBFLI_PATH = os.path.join(os.path.dirname(__file__),
                           'cextern/libfli-1.999.1-180223')

TRAVIS = os.environ.get('TRAVIS', False)


def get_libfli_directories():

    dirs = [LIBFLI_PATH]

    if sys.platform in ['linux', 'darwin', 'unix']:
        dirs.append(os.path.join(LIBFLI_PATH, 'unix'))
        if not TRAVIS:
            dirs.append(os.path.join(LIBFLI_PATH, 'unix/libusb'))
            # if sys.platform in ['linux', 'unix']:
            #     dirs.append(os.path.join(LIBFLI_PATH, 'unix', 'linux'))
            # elif sys.platform in ['darwin']:
            #     dirs.append(os.path.join(LIBFLI_PATH, 'unix', 'osx'))

    return dirs


def get_libfli_sources():

    dirs = get_libfli_directories()

    sources = []
    for dir_ in dirs:
        sources += glob.glob(dir_ + '/*.c')

    return sources


libfli_extra_compile_args = ['-D__LIBUSB__', '-Wall', '-O3', '-fPIC', '-g']
libfli_extra_link_args = ['-lm', '-nostartfiles']


# Do not use libusb on travis because it makes the build fail.
# This still creates a usable library and we are mocking the device anyway.
if TRAVIS:
    libfli_libraries = []
else:
    libfli_libraries = ['usb-1.0']


# Compile libfli as a C library. This produces a statically linked archive
# called libfli.a that we can then link in the pybind11 library.
# libfli = ['fli',  # The lib prefix is added automatically.
#           {
#               'sources': get_libfli_sources(),
#               'include_dirs': get_libfli_directories(),
#               'libraries': libfli_libraries,
#               'extra_compile_args': libfli_extra_compile_args,
#               'extra_link_args': libfli_extra_link_args
#           }]

ext_modules = Extension(
    'flicamera.libfli',
    sources=get_libfli_sources(),
    include_dirs=get_libfli_directories(),
    libraries=libfli_libraries,
    extra_compile_args=libfli_extra_compile_args,
    extra_link_args=libfli_extra_link_args
)


# Now prepare the compilation of the pybind11 module

# extra_compile_args = ['--std=c++11', '-fPIC']
# if sys.platform == 'darwin':
#     extra_compile_args += ['-stdlib=libc++', '-mmacosx-version-min=10.9']

# ext_modules = [
#     Extension(
#         'flicamera/fliwrapper',
#         ['flicamera/src/libfli_wrapper.cpp'],
#         include_dirs=[
#             pybind11.get_include(user=False),
#             pybind11.get_include(user=True),
#             'cextern/libfli-1.999.1-180223'
#         ],
#         libraries=['fli'],
#         extra_compile_args=extra_compile_args,
#         extra_link_args=['-mmacosx-version-min=10.9'],
#         language='c++'
#     )
# ]


def build(setup_kwargs):
    """To build the extensions with poetry."""

    setup_kwargs.update({
        # 'libraries': [libfli],
        'ext_modules': [ext_modules]
    })
