
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DvsServiceConsoleVNicProfile(vim, *args, **kwargs):
    '''The DvsServiceConsoleVNicProfile data object describes the IP configuration for
    a service console Virtual NIC connected to a distributed virtual switch. The
    ipConfig property contains the Virtual NIC IP address. If a profile plug-in
    defines policies or subprofiles, use the policy or property list to access the
    additional configuration data.'''
    
    obj = vim.client.factory.create('ns0:DvsServiceConsoleVNicProfile')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 4 arguments got: %d' % len(args))

    required = [ 'ipConfig', 'key', 'enabled' ]
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
    