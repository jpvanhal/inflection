#!/usr/bin/env python
# -*- coding: utf-8 -*-

import inflection

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='Inflection',
    version=inflection.__version__,
    description="A port of Ruby on Rails inflector to Python",
    long_description=open('README.rst').read() + '\n\n' +
                     open('CHANGES.rst').read(),
    author='Janne Vanhala',
    author_email='janne.vanhala@gmail.com',
    url='http://github.com/jpvanhal/inflection',
    license=open('LICENSE').read(),
    py_modules=['inflection'],
    zip_safe=False,
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ),
)
