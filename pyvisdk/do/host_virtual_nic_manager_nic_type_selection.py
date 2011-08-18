# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostVirtualNicManagerNicTypeSelection(vim, *args, **kwargs):
    '''DataObject which lets a VirtualNic be marked for use as a
    HostVirtualNicManagerNicType.'''
    
    obj = vim.client.factory.create('ns0:HostVirtualNicManagerNicTypeSelection')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'nicType', 'vnic' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    