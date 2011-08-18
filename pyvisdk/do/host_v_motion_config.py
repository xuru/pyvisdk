# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostVMotionConfig(vim, *args, **kwargs):
    '''This data object configuring VMotion on the host. The runtime information is
    available from the VMotionInfo data object type.'''
    
    obj = vim.client.factory.create('ns0:HostVMotionConfig')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'enabled', 'vmotionNicKey' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    