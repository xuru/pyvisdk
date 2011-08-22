
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DistributedVirtualSwitchProductSpec(vim, *args, **kwargs):
    '''This data object type is a subset of AboutInfo. An object of this type can be
    used to describe the specification for a proxy switch module of a
    DistributedVirtualSwitch.'''
    
    obj = vim.client.factory.create('ns0:DistributedVirtualSwitchProductSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))
        
    signature = [  ]
    inherited = [ 'build', 'bundleId', 'bundleUrl', 'forwardingClass', 'name', 'vendor',
        'version' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    