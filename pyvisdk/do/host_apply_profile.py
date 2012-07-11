
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostApplyProfile(vim, *args, **kwargs):
    '''The HostApplyProfile data object provides access to subprofiles that contain
    configuration data for different host capabilities. The Profile Engine will use
    any configuration data that you supply to overwrite the host configuration. See
    the ExecuteHostProfile and ApplyHostConfig_Task methods.'''
    
    obj = vim.client.factory.create('ns0:HostApplyProfile')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))

    required = [ 'enabled' ]
    optional = [ 'authentication', 'datetime', 'firewall', 'memory', 'network', 'option',
        'security', 'service', 'storage', 'userAccount', 'usergroupAccount', 'policy',
        'profileTypeName', 'profileVersion', 'property', 'dynamicProperty',
        'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    