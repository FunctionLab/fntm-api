#!/usr/bin/env python

from setuptools import setup, find_packages

# Keyword order: https://packaging.python.org/distributing
setup(
    # These 9 fields are inserted into PKG-INFO. Unspecified keys are set to UNKNOWN values.
    name='fntmapi',
    version='1.0.0',
    description='FNTM API Python Demo',
    # long_description="",
    url='https://github.com/FunctionLab/fntm-api',
    author='amr4',
    # author_email='',
    # license='',
    # platform=''

    scripts=['fntmapi.py'],
    install_requires=['requests'],
)
