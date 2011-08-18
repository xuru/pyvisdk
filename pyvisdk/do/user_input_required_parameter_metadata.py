# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def UserInputRequiredParameterMetadata(vim, *args, **kwargs):
    '''DataObject represents the metadata information for a parameter which will be
    specified by the user during apply time.'''
    
    obj = vim.client.factory.create('ns0:UserInputRequiredParameterMetadata')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'id', 'parameter', 'userInputParameter' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    