
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def PhysicalNicCdpInfo(vim, *args, **kwargs):
    '''CDP (Cisco Discovery Protocol) is a link level protocol that allows for
    discovering the CDP-awared network hardware at either end of a DIRECT
    connection. It's only good for direct connection because CDP doesn't get
    forwarded through switches. It's a simple advertisement protocol which beacons
    information about the switch or host along with some port information. The CDP
    information allows ESX Server admins to know which Cisco switch port is
    connected to any given virtual switch uplink (PNIC).'''
    
    obj = vim.client.factory.create('ns0:PhysicalNicCdpInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))

    required = [  ]
    optional = [ 'address', 'cdpVersion', 'deviceCapability', 'devId', 'fullDuplex',
        'hardwarePlatform', 'ipPrefix', 'ipPrefixLen', 'location', 'mgmtAddr', 'mtu',
        'portId', 'samples', 'softwareVersion', 'systemName', 'systemOID', 'timeout',
        'ttl', 'vlan', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    