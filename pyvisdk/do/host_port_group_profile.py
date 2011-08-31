
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostPortGroupProfile(vim, *args, **kwargs):
    '''This data object type represents the profile for a Port Group that will be used
    by ESX host.'''
    
    obj = vim.client.factory.create('ns0:HostPortGroupProfile')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 7:
        raise IndexError('Expected at least 8 arguments got: %d' % len(args))
        
    required = [ 'ipConfig', 'key', 'name', 'networkPolicy', 'vlan', 'vswitch', 'enabled' ]
    optional = [ 'policy', 'dynamicProperty', 'dynamicType' ]
    
    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    