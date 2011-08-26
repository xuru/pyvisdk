
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostVirtualSwitchBeaconConfig(vim, *args, **kwargs):
    '''Define this data object to enable beacon probing as a method to validate the
    link status of a physical network adapter. Beacon probing must be configured in
    order to use the beacon status as a criteria to determine if a physical network
    adapter failed.See checkBeacon'''
    
    obj = vim.client.factory.create('ns0:HostVirtualSwitchBeaconConfig')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))
        
    signature = [ 'interval' ]
    inherited = [  ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    