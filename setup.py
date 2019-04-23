#!/usr/bin/env python
import os
from setuptools import setup, find_packages


on_rtd = os.environ.get('READTHEDOCS') == 'True'
# read the docs could not compile numpy and c extensions
if on_rtd:
    setup_requires = []
    install_requires = []
    tests_require = []
else:
    setup_requires = [
        'nose',
        'coverage',
    ]
    install_requires = []
    tests_require = []


description = """\
Split an iterable into chunks in Python."""

long_description = """\
Please visit  the `GitHub repository <https://github.com/ianlini/dchunk>`_
for more information.\n
"""
with open('README.rst') as fp:
    long_description += fp.read()


setup(
    name='dchunk',
    version="0.0.1",
    description=description,
    long_description=long_description,
    author='Ian Lin',
    url='https://github.com/ianlini/dchunk',
    setup_requires=setup_requires,
    install_requires=install_requires,
    tests_require=tests_require,
    license="MIT",
    classifiers=[
        'Topic :: Utilities',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
    ],
    test_suite='nose.collector',
    packages=find_packages(),
)
