# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostInternetScsiHbaStaticTarget(vim, *args, **kwargs):
    '''The iSCSI static target.'''
    
    obj = vim.client.factory.create('ns0:HostInternetScsiHbaStaticTarget')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'address', 'advancedOptions', 'authenticationProperties', 'digestProperties',
        'iScsiName', 'parent', 'port', 'supportedAdvancedOptions' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    