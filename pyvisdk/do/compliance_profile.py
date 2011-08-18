# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ComplianceProfile(vim, *args, **kwargs):
    '''DataObject contains the verifications that need to be done to make sure the
    entity is in compliance.'''
    
    obj = vim.client.factory.create('ns0:ComplianceProfile')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'expression', 'rootExpression' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    