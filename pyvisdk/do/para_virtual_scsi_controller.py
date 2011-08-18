# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ParaVirtualSCSIController(vim, *args, **kwargs):
    '''ParaVirtualSCSIController is the data object that represents a paravirtualized
    SCSI controller.'''
    
    obj = vim.client.factory.create('ns0:ParaVirtualSCSIController')
    
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
    