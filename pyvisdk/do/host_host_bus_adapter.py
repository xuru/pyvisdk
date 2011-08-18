# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostHostBusAdapter(vim, *args, **kwargs):
    '''This data object type describes the bus adapter for the host. A host bus
    adapter (HBA) is a hardware or software adapter that connects the host to
    storage devices.'''
    
    obj = vim.client.factory.create('ns0:HostHostBusAdapter')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))
        
    signature = [ 'bus', 'device' ]
    inherited = [ 'driver', 'key', 'model', 'pci', 'status' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    