# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ClusterAffinityRuleSpec(vim, *args, **kwargs):
    '''The ClusterAffinityRuleSpec data object defines a set of virtual machines. DRS
    will attempt to schedule the virtual machines to run on the same host.'''
    
    obj = vim.client.factory.create('ns0:ClusterAffinityRuleSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))
        
    signature = [ 'vm' ]
    inherited = [ 'enabled', 'inCompliance', 'key', 'mandatory', 'name', 'status', 'userCreated' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    