# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostPortGroup(vim, *args, **kwargs):
    '''This data object type is used to describe port groups. Port groups are used to
    group virtual network adapters on a virtual switch, associating them with
    networks and network policies.'''
    
    obj = vim.client.factory.create('ns0:HostPortGroup')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))
        
    signature = [ 'computedPolicy' ]
    inherited = [ 'key', 'port', 'spec', 'vswitch' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    