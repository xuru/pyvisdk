# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostTpmDigestInfo(vim, *args, **kwargs):
    '''This data object type describes the digest values in the Platform Configuration
    Register (PCR) of a Trusted Platform Module (TPM) device.'''
    
    obj = vim.client.factory.create('ns0:HostTpmDigestInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'digestMethod', 'digestValue', 'objectName', 'pcrNumber' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    