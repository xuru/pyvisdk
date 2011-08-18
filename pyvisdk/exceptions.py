'''
Created on Jul 29, 2011

@author: eplaster
'''
from exceptions import Exception

class InvalidArgumentError(Exception):
    pass

class PyVisdkError(Exception):
    pass

class VisdkTaskError(Exception):
    pass

class VisdkInvalidState(Exception):
    pass
