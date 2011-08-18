# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualSCSIControllerOption(vim, *args, **kwargs):
    '''The VirtualSCSIControllerOption data object type contains the options for a
    virtual SCSI controller defined by the VirtualSCSIController data object type.'''
    
    obj = vim.client.factory.create('ns0:VirtualSCSIControllerOption')
    
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
    