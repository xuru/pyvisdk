
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostHardwareSummary(vim, *args, **kwargs):
    '''This data object type summarizes hardware used by the host.'''
    
    obj = vim.client.factory.create('ns0:HostHardwareSummary')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 11:
        raise IndexError('Expected at least 12 arguments got: %d' % len(args))
        
    signature = [ 'cpuMhz', 'cpuModel', 'memorySize', 'model', 'numCpuCores', 'numCpuPkgs',
        'numCpuThreads', 'numHBAs', 'numNics', 'uuid', 'vendor' ]
    inherited = [ 'otherIdentifyingInfo' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    