# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def TemplateConfigFileQuery(vim, *args, **kwargs):
    '''This data object type describes the query specification for a template virtual
    machine configuration file.'''
    
    obj = vim.client.factory.create('ns0:TemplateConfigFileQuery')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'details', 'filter' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    