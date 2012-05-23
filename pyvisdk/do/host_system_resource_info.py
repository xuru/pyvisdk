
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostSystemResourceInfo(vim, *args, **kwargs):
    '''The SystemResourceInfo data object describes the configuration of a single
    system resource group. System resource groups are analogous to ResourcePool
    objects for virtual machines; however, their structure is fixed and groups may
    not be created nor destroyed, only configured.'''
    
    obj = vim.client.factory.create('ns0:HostSystemResourceInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))

    required = [ 'key' ]
    optional = [ 'child', 'config', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    