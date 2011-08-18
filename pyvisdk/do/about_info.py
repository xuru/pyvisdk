# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def AboutInfo(vim, *args, **kwargs):
    '''This data object type describes system information including the name, type,
    version, and build number.'''
    
    obj = vim.client.factory.create('ns0:AboutInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'apiType', 'apiVersion', 'build', 'fullName', 'instanceUuid',
        'licenseProductName', 'licenseProductVersion', 'localeBuild', 'localeVersion',
        'name', 'osType', 'productLineId', 'vendor', 'version' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    