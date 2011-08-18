# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VAppConfigSpec(vim, *args, **kwargs):
    '''Configuration of a vApp'''
    
    obj = vim.client.factory.create('ns0:VAppConfigSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))
        
    signature = [  ]
    inherited = [ 'eula', 'installBootRequired', 'installBootStopDelay', 'ipAssignment',
        'ovfEnvironmentTransport', 'ovfSection', 'product', 'property_', 'annotation',
        'entityConfig', 'instanceUuid' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    