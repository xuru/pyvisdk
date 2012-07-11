
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ClusterFailoverHostAdmissionControlPolicy(vim, *args, **kwargs):
    '''The ClusterFailoverHostAdmissionControlPolicy dedicates one or more hosts for
    use during failover. When a host fails with this policy in place, vSphere HA
    attempts to restart its virtual machines on a dedicated failover host. If this
    is not possible, for example the failover host itself has failed or it has
    insufficient resources, HA attempts to restart those virtual machines on
    another host in the cluster.To support the availabilty of a failover host, the
    vCenter Server will prevent users from powering on virtual machines on that
    host, or from using vMotion to migrate virtual machines to the host. Also, DRS
    does not use the failover host for load balancing.To obtain the status of a
    failover host, use the hostStatus property
    (ClusterComputeResourceSummary.admissionControlInfo.hostStatus).'''
    
    obj = vim.client.factory.create('ns0:ClusterFailoverHostAdmissionControlPolicy')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))

    required = [  ]
    optional = [ 'failoverHosts', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    