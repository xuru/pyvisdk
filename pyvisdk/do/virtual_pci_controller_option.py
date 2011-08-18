# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualPCIControllerOption(vim, *args, **kwargs):
    '''This data object type contains the options for a virtual PCI Controller.'''
    
    obj = vim.client.factory.create('ns0:VirtualPCIControllerOption')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 11:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'autoAssignController', 'backingOption', 'connectOption', 'controllerType',
        'defaultBackingOptionIndex', 'deprecated', 'hotRemoveSupported',
        'licensingLimit', 'plugAndPlay', 'type', 'devices', 'supportedDevice',
        'numEthernetCards', 'numParaVirtualSCSIControllers',
        'numPCIPassthroughDevices', 'numSasSCSIControllers', 'numSCSIControllers',
        'numSoundCards', 'numVideoCards', 'numVmciDevices', 'numVmiRoms',
        'numVmxnet3EthernetCards' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    