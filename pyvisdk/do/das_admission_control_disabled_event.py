# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DasAdmissionControlDisabledEvent(vim, *args, **kwargs):
    '''This event records when admission control checks have been disabled in a HA
    cluster.'''
    
    obj = vim.client.factory.create('ns0:DasAdmissionControlDisabledEvent')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'chainId', 'changeTag', 'computeResource', 'createdTime', 'datacenter', 'ds',
        'dvs', 'fullFormattedMessage', 'host', 'key', 'net', 'userName', 'vm' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    