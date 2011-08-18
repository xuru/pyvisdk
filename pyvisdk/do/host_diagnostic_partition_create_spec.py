# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostDiagnosticPartitionCreateSpec(vim, *args, **kwargs):
    '''The diagnostic create specification is used by the system to create a new
    diagnostic partition on a SCSI disk.'''
    
    obj = vim.client.factory.create('ns0:HostDiagnosticPartitionCreateSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'active', 'diagnosticType', 'id', 'partition', 'storageType' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    