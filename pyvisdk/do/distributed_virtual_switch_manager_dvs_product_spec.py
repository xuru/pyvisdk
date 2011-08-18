# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DistributedVirtualSwitchManagerDvsProductSpec(vim, *args, **kwargs):
    '''This class is used to specify ProductSpec for the DVS. The two properties are
    strictly mutually exclusive. If both properties are set, then an
    InvalidArgument fault would be thrown.'''
    
    obj = vim.client.factory.create('ns0:DistributedVirtualSwitchManagerDvsProductSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'distributedVirtualSwitch', 'newSwitchProductSpec' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    