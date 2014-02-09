# -*- coding: utf-8 -*-
"""
======
stopit
======

Raise asynchronous exceptions in other thread, control the timeout of blocks
or callables with a context manager or a decorator.
"""

from setuptools import setup
import os

version = '1.0.0-dev'

this_directory = os.path.abspath(os.path.dirname(__file__))

def read(*names):
    return open(os.path.join(this_directory, *names), 'r').read().strip()

long_description = read('README.rst')


setup(name='stopit',
      version=version,
      description="Timeout control decorator and context manager, raise exception in another thread",
      long_description=long_description,
      # FIXME: Add more classifiers from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Topic :: Utilities",
          "Programming Language :: Python",
          "Programming Language :: Python :: Implementation :: CPython",
          "Programming Language :: Python :: 2.6",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3.3",
          "Operating System :: OS Independent",
          "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
          "Intended Audience :: Developers",
          "Development Status :: 5 - Production/Stable"
      ],
      keywords='threads timeout',
      author='Gilles Lenfant',
      author_email='gilles.lenfant@gmail.com',
      url='http://pypi.python.org/pypi/stopit',
      license='GPLv3',
      py_modules=['stopit'],
      test_suite='tests.suite',
      zip_safe=False
      )