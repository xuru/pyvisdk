
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ClusterFailoverLevelAdmissionControlPolicy(vim, *args, **kwargs):
    '''When you use the failover level policy, VMware HA partitions resources into
    slots. A slot represents the minimum CPU and memory resources that are required
    to support any powered-on virtual machine in the cluster.With the failover
    level policy in place, HA uses the following slot calculations to control
    virtual machine migration within the cluster:If your cluster contains any
    virtual machines that have much larger reservations than the others, they will
    distort slot size calculation. To avoid this, you can specify an upper bound
    for slot sizes; use the configuration editor in the vSphere Client to set the
    das.slotCpuInMHz and das.slotMemInMB attributes. When you use these attributes,
    there is a risk that resource fragmentation will cause virtual machines with
    resource requirements larger than the slot size to be assigned multiple slots.
    In a cluster that is close to capacity, there might be enough slots in
    aggregate for HA to successfully failover a virtual machine. However, if those
    slots are located on multiple hosts, a virtual machine assigned multiple slots
    cannot use them because a virtual machine can run on only a single host at a
    time. * Determine how many slots each host in the cluster can hold. HA uses the
    CPU and memory resources in a host's root resource pool to determine host slot
    capacity, not the total physical resources of the host. Resources used for
    virtualization purposes are not included. HA uses connected hosts that are not
    in maintenance mode and that do not have any HA errors.The CPU slot resource is
    the host CPU resource amount divided by the CPU component of the slot size; the
    result is rounded down. HA makes the same calculation for host memory resource
    amount. HA compares the results; the lower of the two numbers is the host slot
    capacity. * Determine the current failover capacity of the cluster. This is the
    number of hosts (starting from the largest) that can fail and still leave
    enough slots to satisfy all of the powered-on virtual machines. * Compare the
    current failover capacity to the configured failoverLevel. If the current
    failover capacity is less than the configured failover level, HA disallows the
    operation.'''
    
    obj = vim.client.factory.create('ns0:ClusterFailoverLevelAdmissionControlPolicy')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))
        
    signature = [ 'failoverLevel' ]
    inherited = [  ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    