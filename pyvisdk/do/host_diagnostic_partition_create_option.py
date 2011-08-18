# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostDiagnosticPartitionCreateOption(vim, *args, **kwargs):
    '''This data object describes a disk that can be used to create a diagnostic
    partition.'''
    
    obj = vim.client.factory.create('ns0:HostDiagnosticPartitionCreateOption')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'diagnosticType', 'disk', 'storageType' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    