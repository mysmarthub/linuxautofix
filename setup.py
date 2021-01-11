#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details)
# Copyright © 2020-2021 Aleksandr Suvorov
# -----------------------------------------------------------------------------
from setuptools import setup, find_packages
from os.path import join, dirname

PACKAGE = "linuxautofix"
VERSION = __import__(PACKAGE).__version__
AUTHOR = __import__(PACKAGE).__author__
AUTHOR_EMAIL = "mysmarthub@ya.ru"
DESCRIPTION = "Linux Auto Fix - utility for automatic command execution, " \
              "and auto-tuning Linux distributions after installation. | " \
              "Aleksandr Suvorov | https://github.com/mysmarthub/ | Donate: https://yoomoney.ru/to/4100115206129186 |" \
              " https://paypal.me/myhackband"
NAME = "linuxautofix"
URL = "https://github.com/mysmarthub/linuxautofix"
LICENSE = 'BSD 3-Clause License'
LONG_DESCRIPTION = open(join(dirname(__file__), 'README.md')).read()
INSTALL_REQUIRES = []
PLATFORM = ['Linux', 'Windows']
CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Environment :: Console",
    "Intended Audience :: End Users/Desktop",
    "Intended Audience :: System Administrators",
    "License :: OSI Approved :: BSD License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: POSIX :: Linux",
    "Programming Language :: Python :: 3 :: Only",
    "Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Utilities"
]
KEYWORDS = [
    'linuxautofix',
    'fix ubuntu',
    'fix fedora',
    'fix linux mint',
    'aleksandr suvorov',
    'linux auto fix',
    'commandoro'
]
setup(
    name=NAME,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    description=DESCRIPTION,
    version=VERSION,
    license=LICENSE,
    platforms=PLATFORM,
    packages=find_packages(),
    long_description_content_type='text/markdown',
    long_description=LONG_DESCRIPTION,
    install_requires=INSTALL_REQUIRES,
    include_package_data=True,
    zip_safe=False,
    keywords=KEYWORDS,
    entry_points={
        'console_scripts':
            ['linuxautofix = linuxautofix.linuxautofix:cli']
        }
)
