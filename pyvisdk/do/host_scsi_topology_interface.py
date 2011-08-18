# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostScsiTopologyInterface(vim, *args, **kwargs):
    '''This data object type describes the SCSI interface that is associated with a
    list of targets.'''
    
    obj = vim.client.factory.create('ns0:HostScsiTopologyInterface')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'adapter', 'key', 'target' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    