# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ProfileDescription(vim, *args, **kwargs):
    '''DataObject which describes the profile. Description contains multiple sections.
    Each section describes some sub-part of the profile.'''
    
    obj = vim.client.factory.create('ns0:ProfileDescription')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'section' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    