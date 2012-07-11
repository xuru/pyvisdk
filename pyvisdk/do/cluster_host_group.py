
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ClusterHostGroup(vim, *args, **kwargs):
    '''The ClusterHostGroup data object identifies hosts for VM-Host rules. VM-Host
    rules determine placement of virtual machines on hosts in a cluster. The logic
    specified in a ClusterVmHostRuleInfo object determines where virtual machines
    can be powered-on.'''
    
    obj = vim.client.factory.create('ns0:ClusterHostGroup')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))

    required = [ 'name' ]
    optional = [ 'host', 'userCreated', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    