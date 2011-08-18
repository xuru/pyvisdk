# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualSCSIController(vim, *args, **kwargs):
    '''The VirtualSCSIController data object type represents a SCSI controller in a
    virtual machine.'''
    
    obj = vim.client.factory.create('ns0:VirtualSCSIController')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'backing', 'connectable', 'controllerKey', 'deviceInfo', 'key', 'unitNumber',
        'busNumber', 'device', 'hotAddRemove', 'scsiCtlrUnitNumber', 'sharedBus' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    