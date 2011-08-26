
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostMultipathInfoPath(vim, *args, **kwargs):
    '''Path objects are identified by a key. The specifics of how the key is formatted
    are dependent on the implementation. Example implementations include using
    strings like "vmhba1:0:0:0".'''
    
    obj = vim.client.factory.create('ns0:HostMultipathInfoPath')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 5:
        raise IndexError('Expected at least 6 arguments got: %d' % len(args))
        
    signature = [ 'adapter', 'key', 'lun', 'name', 'pathState' ]
    inherited = [ 'isWorkingPath', 'state', 'transport' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    