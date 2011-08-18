# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def CustomizationSpec(vim, *args, **kwargs):
    '''The Specification data object type contains information required to customize a
    virtual machine when deploying it or migrating it to a new host.'''
    
    obj = vim.client.factory.create('ns0:CustomizationSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'encryptionKey', 'globalIPSettings', 'identity', 'nicSettingMap', 'options' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    