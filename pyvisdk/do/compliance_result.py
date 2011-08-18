# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ComplianceResult(vim, *args, **kwargs):
    '''DataObject representing the result from a ComplianceCheck'''
    
    obj = vim.client.factory.create('ns0:ComplianceResult')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'checkTime', 'complianceStatus', 'entity', 'failure', 'profile' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    