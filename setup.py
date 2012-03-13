#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, Command
import subprocess
import inflection


class PyTest(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        errno = subprocess.call(['py.test'])
        raise SystemExit(errno)


setup(
    name='inflection',
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
    cmdclass={'test': PyTest},
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ),
)
