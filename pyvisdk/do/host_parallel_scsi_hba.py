
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostParallelScsiHba(vim, *args, **kwargs):
    '''The ParallelScsiHba data object type describes a parallel SCSI host bus
    adapter.'''
    
    obj = vim.client.factory.create('ns0:HostParallelScsiHba')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 5 arguments got: %d' % len(args))
        
    signature = [ 'bus', 'device', 'model', 'status' ]
    inherited = [ 'driver', 'key', 'pci' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    