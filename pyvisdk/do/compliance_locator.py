# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ComplianceLocator(vim, *args, **kwargs):
    '''This dataObject contains information about location of applyProfile which was
    responsible for generation of a particular ComplianceExpression.'''
    
    obj = vim.client.factory.create('ns0:ComplianceLocator')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'applyPath', 'expressionName' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    