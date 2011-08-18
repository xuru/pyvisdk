# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ChoiceOption(vim, *args, **kwargs):
    '''The ChoiceOption data object type defines a set of supported string values, a
    localizable description for each value, and the default value.'''
    
    obj = vim.client.factory.create('ns0:ChoiceOption')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'valueIsReadonly', 'choiceInfo', 'defaultIndex' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    