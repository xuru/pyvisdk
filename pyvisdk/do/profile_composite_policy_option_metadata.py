# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ProfileCompositePolicyOptionMetadata(vim, *args, **kwargs):
    '''DataObject represents the metadata information of a composite PolicyOption. The
    user will retrieve the metadata information about a composite policy and then
    compose the Composite PolicyOption.'''
    
    obj = vim.client.factory.create('ns0:ProfileCompositePolicyOptionMetadata')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'id', 'parameter', 'option' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    