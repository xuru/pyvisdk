
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostVirtualSwitchBeaconConfig(vim, *args, **kwargs):
    '''This data object type describes the configuration of the beacon to probe
    connectivity of physical network adapters. A beacon is sent out of one network
    adapter and should arrive on another network adapter in the team. The
    successful roundtrip indicates that the network adapters are working.Define
    this data object to enable beacon probing as a method to validate the link
    status of a physical network adapter. Beacon probing must be configured in
    order to use the beacon status as a criteria to determine if a physical network
    adapter failed.See checkBeacon'''
    
    obj = vim.client.factory.create('ns0:HostVirtualSwitchBeaconConfig')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))

    required = [ 'interval' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    