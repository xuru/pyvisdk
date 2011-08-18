# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineConfigSummary(vim, *args, **kwargs):
    '''A subset of virtual machine configuration.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineConfigSummary')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'annotation', 'cpuReservation', 'ftInfo', 'guestFullName', 'guestId',
        'installBootRequired', 'instanceUuid', 'memoryReservation', 'memorySizeMB',
        'name', 'numCpu', 'numEthernetCards', 'numVirtualDisks', 'product', 'template',
        'uuid', 'vmPathName' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    