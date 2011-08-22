
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DVPortStatus(vim, *args, **kwargs):
    '''The runtime information of a DistributedVirtualPort.'''
    
    obj = vim.client.factory.create('ns0:DVPortStatus')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))
        
    signature = [ 'blocked', 'linkUp' ]
    inherited = [ 'linkPeer', 'macAddress', 'mtu', 'statusDetail', 'trunkingMode', 'vlanIds',
        'vmDirectPathGen2Active', 'vmDirectPathGen2InactiveReasonExtended',
        'vmDirectPathGen2InactiveReasonNetwork', 'vmDirectPathGen2InactiveReasonOther' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    