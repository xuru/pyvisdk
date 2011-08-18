# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def LicenseReservationInfo(vim, *args, **kwargs):
    '''A reservation describes how many licenses of a particular feature are being
    used by a particular feature.'''
    
    obj = vim.client.factory.create('ns0:LicenseReservationInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'key', 'required', 'state' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    