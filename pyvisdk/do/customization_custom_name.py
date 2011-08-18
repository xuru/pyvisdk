# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def CustomizationCustomName(vim, *args, **kwargs):
    '''Specifies that the VirtualCenter server will launch an external application to
    generate the (hostname/IP). The command line for this application must be
    specified in the server configuration file (vpxd.cfg) in the vpxd/name-ip-
    generator key.'''
    
    obj = vim.client.factory.create('ns0:CustomizationCustomName')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'argument' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    