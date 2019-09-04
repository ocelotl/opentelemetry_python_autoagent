#!/usr/bin/env python3

from sys import exit, argv
from os import execl
import os
from os.path import dirname, join
from distutils.spawn import find_executable

from opentelemetry_python_autoagent import __version__, __file__


def run():

    print('opentelemetry_python_autoagent version {}'.format(__version__))

    os.environ['PYTHONPATH'] = join(dirname(__file__), 'initialize')

    python3 = find_executable('python3')

    execl(python3, python3, argv[1])

    exit(0)
