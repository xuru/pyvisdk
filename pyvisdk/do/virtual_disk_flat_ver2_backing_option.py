# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualDiskFlatVer2BackingOption(vim, *args, **kwargs):
    '''This data object type contains the available options when backing a virtual
    disk using a host file with the flat file format used in VMware Server and in
    ESX Server 2.x and greater. Flat disks are pre-allocated, whereas sparse disks
    are grown as needed.'''
    
    obj = vim.client.factory.create('ns0:VirtualDiskFlatVer2BackingOption')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 9:
        raise IndexError('Expected at least 10 arguments got: %d' % len(args))
        
    signature = [ 'type', 'diskMode', 'eagerlyScrub', 'growable', 'hotGrowable', 'split',
        'thinProvisioned', 'uuid', 'writeThrough' ]
    inherited = [ 'fileNameExtensions' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    