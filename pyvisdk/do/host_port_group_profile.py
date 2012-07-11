
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostPortGroupProfile(vim, *args, **kwargs):
    '''The HostPortGroupProfile data object represents the subprofile for a port group
    that will be used by the ESX host. If a profile plug-in defines policies or
    subprofiles, use the policy or property list to access the additional
    configuration data.'''
    
    obj = vim.client.factory.create('ns0:HostPortGroupProfile')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 7:
        raise IndexError('Expected at least 8 arguments got: %d' % len(args))

    required = [ 'ipConfig', 'key', 'name', 'networkPolicy', 'vlan', 'vswitch', 'enabled' ]
    optional = [ 'policy', 'profileTypeName', 'profileVersion', 'property', 'dynamicProperty',
        'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    