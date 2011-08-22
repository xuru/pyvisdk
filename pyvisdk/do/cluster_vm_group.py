
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ClusterVmGroup(vim, *args, **kwargs):
    '''The ClusterVmGroup data object identifies virtual machines for VM-Host rules.
    VM-Host rules determine placement of virtual machines on hosts in a cluster.
    The logic specified in a ClusterVmHostRuleInfo object determines where virtual
    machines can be powered-on.If a virtual machine is removed from the cluster, it
    loses its DRS group affiliation. The Server does not restore any group
    affiliations if the virtual machine is returned to the cluster.'''
    
    obj = vim.client.factory.create('ns0:ClusterVmGroup')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))
        
    signature = [ 'name' ]
    inherited = [ 'vm' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    