
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostNetworkPolicy(vim, *args, **kwargs):
    '''By contrast, if a host is capable of implementing a policy setting, every
    virtual switch has some value assigned to the policy setting. In this case,
    although all of the policy settings are optional, they always have some value
    either by inheritance or by direct setting.Policy settings are organized into
    policy groups such as SecurityPolicy. Policy groups are optional since it is
    possible that a host may not implement such policies. If a host does not
    support a policy group, the policy group is not set on both the virtual
    switches and the port groups.See HostNetCapabilities'''
    
    obj = vim.client.factory.create('ns0:HostNetworkPolicy')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))
        
    signature = [  ]
    inherited = [ 'nicTeaming', 'offloadPolicy', 'security', 'shapingPolicy' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    