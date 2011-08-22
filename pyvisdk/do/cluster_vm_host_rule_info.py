
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ClusterVmHostRuleInfo(vim, *args, **kwargs):
    '''A ClusterVmHostRuleInfo object identifies virtual machines and host groups that
    determine virtual machine placement. The virtual machines and hosts referenced
    by a VM-Host rule must be in the same cluster.A VM-Host rule identifies the
    following groups.* A virtual machine group (ClusterVmGroup). * Two host groups
    - an affine host group and an anti-affine host group (ClusterHostGroup). At
    least one of the groups must contain one or more hosts.ClusterVmHostRuleInfo
    stores only the names of the relevant virtual machine and host groups. The
    group contents are stored in the virtual machine and host group objects.When
    you modify a VM-Host rule, only the fields that are specified are set.'''
    
    obj = vim.client.factory.create('ns0:ClusterVmHostRuleInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))
        
    signature = [  ]
    inherited = [ 'enabled', 'inCompliance', 'key', 'mandatory', 'name', 'status', 'userCreated',
        'affineHostGroupName', 'antiAffineHostGroupName', 'vmGroupName' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    