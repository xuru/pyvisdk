
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def InventoryDescription(vim, *args, **kwargs):
    ''''''
    
    obj = vim.client.factory.create('ns0:InventoryDescription')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))
        
    signature = [ 'numHosts', 'numVirtualMachines' ]
    inherited = [ 'numClusters', 'numCpuDev', 'numDiskDev', 'numNetDev', 'numResourcePools',
        'numvCpuDev', 'numvDiskDev', 'numvNetDev' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    