
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostMultipathInfoLogicalUnitStorageArrayTypePolicy(vim, *args, **kwargs):
    '''This data object type describes a storage array type policy for for a device.
    This policy determines how device I/O and management is performed.'''
    
    obj = vim.client.factory.create('ns0:HostMultipathInfoLogicalUnitStorageArrayTypePolicy')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))
        
    signature = [ 'policy' ]
    inherited = [  ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    