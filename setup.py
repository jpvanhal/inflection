#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

import inflection

setup(
    name='inflection',
    version=inflection.__version__,
    description="A port of Ruby on Rails inflector to Python",
    long_description=open('README.rst').read(),
    author='Janne Vanhala',
    author_email='janne.vanhala@gmail.com',
    url='https://github.com/jpvanhal/inflection',
    license='MIT',
    py_modules=['inflection'],
    zip_safe=False,
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
