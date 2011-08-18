# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VAppConfigSpec(vim, *args, **kwargs):
    '''Configuration of a vApp'''
    
    obj = vim.client.factory.create('ns0:VAppConfigSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'eula', 'installBootRequired', 'installBootStopDelay', 'ipAssignment',
        'ovfEnvironmentTransport', 'ovfSection', 'product', 'property_', 'annotation',
        'entityConfig', 'instanceUuid' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    