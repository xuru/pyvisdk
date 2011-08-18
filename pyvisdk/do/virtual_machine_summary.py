# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineSummary(vim, *args, **kwargs):
    '''The summary data object type encapsulates a typical set of virtual machine
    information that is useful for list views and summary pages.VirtualCenter can
    retrieve this information very efficiently, even for large sets of virtual
    machines.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineSummary')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))
        
    signature = [ 'config' ]
    inherited = [ 'customValue', 'guest', 'overallStatus', 'quickStats', 'runtime', 'storage',
        'vm' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    