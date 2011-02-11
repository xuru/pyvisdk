#!/usr/bin/env python

'''
pyvisdk - vSphere SDK  for Python
'''

import os, sys

APPDIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, APPDIR)

from setuptools import setup, find_packages

install_requires = ["suds>=0.3.9"]

setupOptions = {
    'name': 'pyvisdk',
    'author': "Eric Plaster",
    'author_email': "",
    'description': "vSphere SDK for Python",
    'long_description': "vSphere SDK for Python",
    'version': "0.1",
    'url': "https://github.com/xuru/pyvisdk",
    'license': "GPL",
    'install_requires': install_requires,
    'packages': find_packages(),
    'classifiers' : ['Development Status :: 4 - Beta',
                   'Framework :: VMWare',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Internet :: WWW/HTTP',
                   'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
                   'Topic :: Internet :: WWW/HTTP :: WSGI',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   ],
    }

if __name__ == '__main__':
    setup(**setupOptions)


