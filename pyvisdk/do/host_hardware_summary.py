
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

    required = [ 'cpuMhz', 'cpuModel', 'memorySize', 'model', 'numCpuCores', 'numCpuPkgs',
        'numCpuThreads', 'numHBAs', 'numNics', 'uuid', 'vendor' ]
    optional = [ 'otherIdentifyingInfo', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    