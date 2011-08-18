# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def PhysicalNic(vim, *args, **kwargs):
    '''This data object type describes the physical network adapter as seen by the
    primary operating system.'''
    
    obj = vim.client.factory.create('ns0:PhysicalNic')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))
        
    signature = [  ]
    inherited = [ 'autoNegotiateSupported', 'device', 'driver', 'key', 'linkSpeed', 'mac', 'pci',
        'resourcePoolSchedulerAllowed', 'resourcePoolSchedulerDisallowedReason',
        'spec', 'validLinkSpecification', 'vmDirectPathGen2Supported',
        'vmDirectPathGen2SupportedMode', 'wakeOnLanSupported' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    