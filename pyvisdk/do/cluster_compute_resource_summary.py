
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ClusterComputeResourceSummary(vim, *args, **kwargs):
    '''The ClusterComputeResourceSummary data object encapsulates runtime properties
    of a ClusterComputeResource.'''
    
    obj = vim.client.factory.create('ns0:ClusterComputeResourceSummary')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 11:
        raise IndexError('Expected at least 12 arguments got: %d' % len(args))

    required = [ 'currentFailoverLevel', 'numVmotions', 'effectiveCpu', 'effectiveMemory',
        'numCpuCores', 'numCpuThreads', 'numEffectiveHosts', 'numHosts',
        'overallStatus', 'totalCpu', 'totalMemory' ]
    optional = [ 'admissionControlInfo', 'currentBalance', 'currentEVCModeKey', 'dasData',
        'targetBalance', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    