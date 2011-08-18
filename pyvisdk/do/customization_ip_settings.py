# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def CustomizationIPSettings(vim, *args, **kwargs):
    '''IP settings for a virtual network adapter.'''
    
    obj = vim.client.factory.create('ns0:CustomizationIPSettings')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))
        
    signature = [  ]
    inherited = [ 'dnsDomain', 'dnsServerList', 'gateway', 'ip', 'ipV6Spec', 'netBIOS',
        'primaryWINS', 'secondaryWINS', 'subnetMask' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    