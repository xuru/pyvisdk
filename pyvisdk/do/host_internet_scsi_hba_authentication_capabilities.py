# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostInternetScsiHbaAuthenticationCapabilities(vim, *args, **kwargs):
    '''The authentication capabilities for this host bus adapter.'''
    
    obj = vim.client.factory.create('ns0:HostInternetScsiHbaAuthenticationCapabilities')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))
        
    signature = [ 'chapAuthSettable', 'krb5AuthSettable' ]
    inherited = [ 'mutualChapSettable', 'spkmAuthSettable', 'srpAuthSettable',
        'targetChapSettable', 'targetMutualChapSettable' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    