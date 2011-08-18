# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def LicenseManagerLicenseInfo(vim, *args, **kwargs):
    '''Encapsulates information about a license'''
    
    obj = vim.client.factory.create('ns0:LicenseManagerLicenseInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'costUnit', 'editionKey', 'labels', 'licenseKey', 'name', 'properties',
        'total', 'used' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    