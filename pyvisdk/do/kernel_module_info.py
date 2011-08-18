# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def KernelModuleInfo(vim, *args, **kwargs):
    '''Information about a kernel module.'''
    
    obj = vim.client.factory.create('ns0:KernelModuleInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 13:
        raise IndexError('Expected at least 14 arguments got: %d' % len(args))
        
    signature = [ 'bssSection', 'dataSection', 'enabled', 'filename', 'id', 'loaded', 'name',
        'optionString', 'readOnlySection', 'textSection', 'useCount', 'version',
        'writableSection' ]
    inherited = [  ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    