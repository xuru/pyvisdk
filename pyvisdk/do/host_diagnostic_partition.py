# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostDiagnosticPartition(vim, *args, **kwargs):
    '''This data object type contains information about an available or active
    diagnostic partition.'''
    
    obj = vim.client.factory.create('ns0:HostDiagnosticPartition')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'diagnosticType', 'id', 'slots', 'storageType' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    