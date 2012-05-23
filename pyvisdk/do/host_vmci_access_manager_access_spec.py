
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostVmciAccessManagerAccessSpec(vim, *args, **kwargs):
    '''The AccessSpec data object declares an update to the service access granted to
    a VM. The given list of services will either be granted in addition to existing
    services, replace the existing service or be revoked depending on the mode
    specified. In case of a revoke, an empty or non-existing service list indicates
    that all granted services should be revoked.'''
    
    obj = vim.client.factory.create('ns0:HostVmciAccessManagerAccessSpec')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))

    required = [ 'mode', 'vm' ]
    optional = [ 'services', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    