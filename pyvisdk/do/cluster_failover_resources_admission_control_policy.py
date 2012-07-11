
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ClusterFailoverResourcesAdmissionControlPolicy(vim, *args, **kwargs):
    '''The ClusterFailoverResourcesAdmissionControlPolicy reserves a specified
    percentage of aggregate cluster resources for failover. With the resources
    failover policy in place, vSphere HA uses the following calculations to control
    virtual machine migration in the cluster.HA uses the actual reservations of the
    virtual machines. If a virtual machine does not have reservations, meaning that
    the reservation is 0, a default of 0MB memory and 256MHz CPU is applied. This
    is controlled by the same HA advanced options used for the failover level
    policy (ClusterFailoverLevelAdmissionControlPolicy).'''
    
    obj = vim.client.factory.create('ns0:ClusterFailoverResourcesAdmissionControlPolicy')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))

    required = [ 'cpuFailoverResourcesPercent', 'memoryFailoverResourcesPercent' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    