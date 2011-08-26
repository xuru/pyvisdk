
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ServiceConsolePortGroupProfile(vim, *args, **kwargs):
    ''''''
    
    obj = vim.client.factory.create('ns0:ServiceConsolePortGroupProfile')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 7:
        raise IndexError('Expected at least 8 arguments got: %d' % len(args))
        
    signature = [ 'enabled', 'key', 'name', 'networkPolicy', 'vlan', 'vswitch', 'ipConfig' ]
    inherited = [ 'policy' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    