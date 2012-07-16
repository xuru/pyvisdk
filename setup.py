#!/usr/bin/python

# Copyright (c) 2011 Eric Plaster http://ogremountain.com/
# All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
'''
pyvisdk - vSphere SDK  for Python
'''

from setuptools import setup, find_packages
import os.path

location = os.path.abspath(os.path.dirname(__file__))
version = open(os.path.join(location, "pyvisdk", "__init__.py")).readline().split()[-1].strip("'")

# we need to make sure we have these to python modules in our path
install_requires = ["suds-jurko", "dataflake.cache", "enum", "brownie", "lxml", "bunch", "infi.pyutils", "jinja2", "python-cjson", ]

setup( 
    name = 'infi.pyvisdk',
    description = "vSphere SDK for Python",
    long_description = "vSphere SDK for Python",
    author = "Guy Rozendorn",
    author_email = "guy@rzn.co.il",
    version = version,
    url = "https://github.com/Infinidat/pyvisdk",
    license = "MIT",
    install_requires = install_requires,
    packages = ["pyvisdk", "pyvisdk.mo", "pyvisdk.base", "pyvisdk.do", "pyvisdk.enums", "pyvisdk.thirdparty", "pyvisdk.facade", "pyvisdk.facade.extension", "pyvisdk.facade.task", "pyvisdk.facade.property_collector", "pyvisdk.esxcli", "pyvisdk.esxcli.base", "pyvisdk.esxcli.executer", "pyvisdk.esxcli.generator", "pyvisdk.esxcli.handlers", ],
    package_data = {'pyvisdk': ['wsdl/*']},
    
    classifiers = ['Development Status :: 4 - Beta',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   ],
    include_package_data=True,
    )


