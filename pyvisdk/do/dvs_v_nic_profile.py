
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DvsVNicProfile(vim, *args, **kwargs):
    '''The DvsVNicProfile data object is the base object for host and service console
    Virtual NIC subprofiles. If a profile plug-in defines additional policies or
    subprofiles, use the policy or property list to access the configuration data.'''
    
    obj = vim.client.factory.create('ns0:DvsVNicProfile')

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
    