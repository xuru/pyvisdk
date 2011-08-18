# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostUnresolvedVmfsExtent(vim, *args, **kwargs):
    '''Information about an unresolved VMFS volume extent An unresolved VMFS volume
    extent is a device partition which is detected to have copy of an extent of a
    VMFS volume. Such a copy can be created via replication or snapshots, for
    example. See HostUnresolvedVmfsVolume'''
    
    obj = vim.client.factory.create('ns0:HostUnresolvedVmfsExtent')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 8:
        raise IndexError('Expected at least 9 arguments got: %d' % len(args))
        
    signature = [ 'device', 'devicePath', 'endBlock', 'isHeadExtent', 'ordinal', 'reason',
        'startBlock', 'vmfsUuid' ]
    inherited = [  ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    