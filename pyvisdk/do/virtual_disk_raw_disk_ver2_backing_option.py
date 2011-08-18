# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualDiskRawDiskVer2BackingOption(vim, *args, **kwargs):
    '''The VirtualDiskOption.RawDiskVer2BackingOption object type contains the
    available options when backing a virtual disk using a host device on VMware
    Server.'''
    
    obj = vim.client.factory.create('ns0:VirtualDiskRawDiskVer2BackingOption')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 5 arguments got: %d' % len(args))
        
    signature = [ 'type', 'autoDetectAvailable', 'descriptorFileNameExtensions', 'uuid' ]
    inherited = [  ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    