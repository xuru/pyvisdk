
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ClusterDasAamHostInfo(vim, *args, **kwargs):
    '''The ClusterDasAamHostInfo object contains a list of the ESX hosts in an HA
    cluster and a list that identifies the hosts. (AAM is a component of the HA
    service.) The primary hosts share the joint responsibility of maintaining all
    cluster state and one will initiate failover actions should a failure
    occur.When you add an ESX host to a vSphere HA cluster, the host downloads HA
    agent components from the vCenter Server. The HA agent maintains communication
    with the vCenter Server.When the host downloads the HA agent, the host
    configures the agent to communicate with other agents in the cluster. A host
    that joins the cluster communicates with an existing primary host to complete
    its configuration (except when you are adding the first host to the cluster).*
    The first five hosts added to the cluster are designated as primary hosts. All
    subsequent hosts are designated as secondary hosts. * If a primary host is
    removed from the cluster, the vCenter Server promotes another host to primary
    status. * There must be at least one functional primary host for vSphere HA to
    operate correctly. If there is not an available primary host (no response),
    host configuration for HA will fail. If there is a total cluster failure, HA
    will begin restarting virtual machines as soon as one host recovers and its HA
    agent is up and running.One of the primary hosts assumes the role of the active
    primary host. The active primary host responsibilities include the following
    activities:* Decides where to restart virtual machines. * Tracks failed restart
    attempts. * Determines when it is appropriate to continue attempts to restart a
    virtual machine.If the active primary host fails, another primary host replaces
    it.'''
    
    obj = vim.client.factory.create('ns0:ClusterDasAamHostInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))

    required = [  ]
    optional = [ 'hostDasState', 'primaryHosts', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    