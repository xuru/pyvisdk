# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def PerfProviderSummary(vim, *args, **kwargs):
    '''This data object type contains information about a performance provider, the
    type of statistics it generates, and the refreshRate for statistics generation.
    A performance provider is any managed object that generates real-time or
    historical statistics (or boththe currentSupported and summarySupported
    properties are not mutually exclusive).'''
    
    obj = vim.client.factory.create('ns0:PerfProviderSummary')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))
        
    signature = [ 'currentSupported', 'entity' ]
    inherited = [ 'refreshRate', 'summarySupported' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    