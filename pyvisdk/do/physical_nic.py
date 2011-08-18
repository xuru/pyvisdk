# -*- coding: ascii -*-

import logging

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
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'autoNegotiateSupported', 'device', 'driver', 'key', 'linkSpeed', 'mac', 'pci',
        'resourcePoolSchedulerAllowed', 'resourcePoolSchedulerDisallowedReason',
        'spec', 'validLinkSpecification', 'vmDirectPathGen2Supported',
        'vmDirectPathGen2SupportedMode', 'wakeOnLanSupported' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    