# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostDiagnosticPartitionCreateDescription(vim, *args, **kwargs):
    '''The diagnostic partition create description details what will be done to create
    a new diagnostic partition on a disk. It contains a CreateSpec that can be
    submitted to create the partition and information that can be shown to the
    user.'''
    
    obj = vim.client.factory.create('ns0:HostDiagnosticPartitionCreateDescription')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'diskUuid', 'layout', 'spec' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    