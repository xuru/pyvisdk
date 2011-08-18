# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualBusLogicControllerOption(vim, *args, **kwargs):
    '''This data object contains the options for a BusLogic SCSI controller.'''
    
    obj = vim.client.factory.create('ns0:VirtualBusLogicControllerOption')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 8:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'autoAssignController', 'backingOption', 'connectOption', 'controllerType',
        'defaultBackingOptionIndex', 'deprecated', 'hotRemoveSupported',
        'licensingLimit', 'plugAndPlay', 'type', 'devices', 'supportedDevice',
        'defaultSharedIndex', 'hotAddRemove', 'numSCSICdroms', 'numSCSIDisks',
        'numSCSIPassthrough', 'scsiCtlrUnitNumber', 'sharing' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    