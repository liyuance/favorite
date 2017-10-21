#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

setup(
    name='favorite',
    version='0.1',
    description=(
        'A tool for collect your favoriter commands'
    ),
    long_description=open('README.rst').read(),
    author='liyuance',
    author_email='liyuance@gmail.com',
    maintainer='liyuance',
    maintainer_email='liyuance@gmail.com',
    packages=["favorite"],
    entry_points = {
        'console_scripts': ['fav=favorite.__main__:main'],
    },
    license='BSD License',
    platforms=["all"],
    url='https://github.com/liyuance/favorite',
    classifiers=[
        'Programming Language :: Python'
    ],
)
