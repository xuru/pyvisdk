# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def FaultToleranceSecondaryOpResult(vim, *args, **kwargs):
    '''FaultToleranceSecondaryOpResult is a data object that reports on the outcome of
    the CreateSecondaryVM_Task or EnableSecondaryVM_Task operation.'''
    
    obj = vim.client.factory.create('ns0:FaultToleranceSecondaryOpResult')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))
        
    signature = [ 'powerOnAttempted' ]
    inherited = [ 'powerOnResult', 'vm' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    