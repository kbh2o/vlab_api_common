#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Common logic used by all RESTful API services for vLab
"""
from setuptools import setup, find_packages


setup(name="vlab-api-common",
      author="Nicholas Willhite",
      version='2018.05.11',
      packages=find_packages(),
      include_package_data=True,
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.5',
      ],
      description="Common logic used by all our RESTful API services of vLab",
      install_requires=['flask-classy', 'requests', 'pyjwt', 'ujson', 'jsonschema',
                        'cryptography', 'pyVmomi']
      )