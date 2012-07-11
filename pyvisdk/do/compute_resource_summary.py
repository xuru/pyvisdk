
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ComputeResourceSummary(vim, *args, **kwargs):
    '''This data object type encapsulates a typical set of ComputeResource information
    that is useful for list views and summary pages.'''
    
    obj = vim.client.factory.create('ns0:ComputeResourceSummary')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 9:
        raise IndexError('Expected at least 10 arguments got: %d' % len(args))

    required = [ 'effectiveCpu', 'effectiveMemory', 'numCpuCores', 'numCpuThreads',
        'numEffectiveHosts', 'numHosts', 'overallStatus', 'totalCpu', 'totalMemory' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    