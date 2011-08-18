# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostInternetScsiHbaDiscoveryProperties(vim, *args, **kwargs):
    '''The discovery settings for this host bus adapter. At least one discovery mode
    must always be active. Multiple modes may be active at the same time.'''
    
    obj = vim.client.factory.create('ns0:HostInternetScsiHbaDiscoveryProperties')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))
        
    signature = [ 'iSnsDiscoveryEnabled' ]
    inherited = [ 'iSnsDiscoveryMethod', 'iSnsHost', 'sendTargetsDiscoveryEnabled',
        'slpDiscoveryEnabled', 'slpDiscoveryMethod', 'slpHost',
        'staticTargetDiscoveryEnabled' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    