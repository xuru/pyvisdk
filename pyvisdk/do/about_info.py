# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

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
        raise IndexError('Expected at least 5 arguments got: %d' % len(args))
        
    signature = [ 'apiType', 'apiVersion', 'build', 'fullName' ]
    inherited = [ 'instanceUuid', 'licenseProductName', 'licenseProductVersion', 'localeBuild',
        'localeVersion', 'name', 'osType', 'productLineId', 'vendor', 'version' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    