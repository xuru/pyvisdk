# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostVirtualNicConnection(vim, *args, **kwargs):
    '''DataObject which provides a level of indirection when identifying VirtualNics
    during configuration. This dataObject lets users specify a VirtualNic in terms
    of the portgroup/Dv Port the vnic is connected to. This is useful in cases
    where VirtualNic will be created as part of a configuration operation and the
    created VirtualNic is referred to in some other part of configuration. e.g: for
    configuring VMotion'''
    
    obj = vim.client.factory.create('ns0:HostVirtualNicConnection')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'dvPort', 'portgroup' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    