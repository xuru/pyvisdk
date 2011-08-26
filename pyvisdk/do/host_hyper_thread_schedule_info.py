
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostHyperThreadScheduleInfo(vim, *args, **kwargs):
    '''Changes to the hyperthreading optimization can take effect only after a system
    restart. Therefore, while it is possible to change the configuration at any
    time, the change will take effect only on the next boot.'''
    
    obj = vim.client.factory.create('ns0:HostHyperThreadScheduleInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 4 arguments got: %d' % len(args))
        
    signature = [ 'active', 'available', 'config' ]
    inherited = [  ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    