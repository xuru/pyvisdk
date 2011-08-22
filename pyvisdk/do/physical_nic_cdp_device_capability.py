
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def PhysicalNicCdpDeviceCapability(vim, *args, **kwargs):
    '''The capability of the CDP-awared device that connects to a PNIC.
    PhysicalNicCdpInfo'''
    
    obj = vim.client.factory.create('ns0:PhysicalNicCdpDeviceCapability')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 7:
        raise IndexError('Expected at least 8 arguments got: %d' % len(args))
        
    signature = [ 'host', 'igmpEnabled', 'networkSwitch', 'repeater', 'router',
        'sourceRouteBridge', 'transparentBridge' ]
    inherited = [  ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    