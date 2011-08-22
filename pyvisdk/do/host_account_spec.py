
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostAccountSpec(vim, *args, **kwargs):
    '''This data object type contains common parameters for local account creation.
    The password and description properties are not supported for group accounts on
    POSIX hosts.'''
    
    obj = vim.client.factory.create('ns0:HostAccountSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))
        
    signature = [ 'id' ]
    inherited = [ 'description', 'password' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    