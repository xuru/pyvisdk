# -*- coding: ascii -*-

import logging

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
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'address', 'cdpVersion', 'deviceCapability', 'devId', 'fullDuplex',
        'hardwarePlatform', 'ipPrefix', 'ipPrefixLen', 'location', 'mgmtAddr', 'mtu',
        'portId', 'samples', 'softwareVersion', 'systemName', 'systemOID', 'timeout',
        'ttl', 'vlan' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    