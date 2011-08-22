
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DistributedVirtualSwitchPortStatistics(vim, *args, **kwargs):
    '''Statistic data of a DistributedVirtualPort.'''
    
    obj = vim.client.factory.create('ns0:DistributedVirtualSwitchPortStatistics')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 16:
        raise IndexError('Expected at least 17 arguments got: %d' % len(args))
        
    signature = [ 'bytesInBroadcast', 'bytesInMulticast', 'bytesInUnicast', 'bytesOutBroadcast',
        'bytesOutMulticast', 'bytesOutUnicast', 'packetsInBroadcast',
        'packetsInDropped', 'packetsInException', 'packetsInMulticast',
        'packetsInUnicast', 'packetsOutBroadcast', 'packetsOutDropped',
        'packetsOutException', 'packetsOutMulticast', 'packetsOutUnicast' ]
    inherited = [  ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    