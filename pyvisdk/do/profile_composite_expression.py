# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ProfileCompositeExpression(vim, *args, **kwargs):
    '''DataObject to Compose expressions. It is used to group expressions together.
    They are similar to a parentheses in an expression.'''
    
    obj = vim.client.factory.create('ns0:ProfileCompositeExpression')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 5:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'displayName', 'id', 'negated', 'expressionName', 'operator' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    