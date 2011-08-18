# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineConfigSummary(vim, *args, **kwargs):
    '''A subset of virtual machine configuration.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineConfigSummary')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))
        
    signature = [  ]
    inherited = [ 'annotation', 'cpuReservation', 'ftInfo', 'guestFullName', 'guestId',
        'installBootRequired', 'instanceUuid', 'memoryReservation', 'memorySizeMB',
        'name', 'numCpu', 'numEthernetCards', 'numVirtualDisks', 'product', 'template',
        'uuid', 'vmPathName' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    