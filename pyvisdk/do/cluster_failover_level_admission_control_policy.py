
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ClusterFailoverLevelAdmissionControlPolicy(vim, *args, **kwargs):
    '''The ClusterFailoverLevelAdmissionControlPolicy defines the number of host
    failures that should be tolerated and still guarantee enough unfragmented
    resources to failover all powered on virtual machines on those failed
    hosts.When you use the failover level policy, vSphere HA partitions resources
    into slots. A slot represents the minimum CPU and memory resources that are
    required to support any powered-on virtual machine in the cluster.With the
    failover level policy in place, HA uses the following slot calculations to
    control virtual machine migration within the cluster:If your cluster contains
    any virtual machines that have much larger reservations than the others, they
    will distort slot size calculation. To avoid this, you can specify an upper
    bound for slot sizes; use the configuration editor in the vSphere Client to set
    the das.slotCpuInMHz and das.slotMemInMB attributes. When you use these
    attributes, there is a risk that resource fragmentation will cause virtual
    machines with resource requirements larger than the slot size to be assigned
    multiple slots. In a cluster that is close to capacity, there might be enough
    slots in aggregate for HA to successfully failover a virtual machine. However,
    if those slots are located on multiple hosts, a virtual machine assigned
    multiple slots cannot use them because a virtual machine can run on only a
    single host at a time.The CPU slot resource is the host CPU resource amount
    divided by the CPU component of the slot size; the result is rounded down. HA
    makes the same calculation for host memory resource amount. HA compares the
    results; the lower of the two numbers is the host slot capacity.'''
    
    obj = vim.client.factory.create('ns0:ClusterFailoverLevelAdmissionControlPolicy')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))

    required = [ 'failoverLevel' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    