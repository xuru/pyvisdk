# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostVmfsVolume(vim, *args, **kwargs):
    '''The VMFS file system.'''
    
    obj = vim.client.factory.create('ns0:HostVmfsVolume')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 5:
        raise IndexError('Expected at least 6 arguments got: %d' % len(args))
        
    signature = [ 'capacity', 'name', 'type', 'blockSizeMb', 'extent' ]
    inherited = [ 'forceMountedInfo', 'majorVersion', 'maxBlocks', 'uuid', 'version',
        'vmfsUpgradable' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    