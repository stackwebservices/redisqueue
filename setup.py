#!/usr/bin/env python

from setuptools import setup

setup(
    name='RedisQueue',
    version='0.0.1',
    author='Vyacheslav Anzhiganov',
    author_email='hello@anzhiganov.com',
    packages=[
        'RedisQueue',
    ],
    install_requires=[
        'redis'
    ],
)
