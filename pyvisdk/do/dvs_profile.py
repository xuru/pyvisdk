
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DvsProfile(vim, *args, **kwargs):
    '''The DvsProfile data object represents the distributed virtual switch to which
    this host is connected. If a profile plug-in defines policies or subprofiles,
    use the policy or property list to access the additional configuration data.'''
    
    obj = vim.client.factory.create('ns0:DvsProfile')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 4 arguments got: %d' % len(args))

    required = [ 'key', 'name', 'enabled' ]
    optional = [ 'uplink', 'policy', 'profileTypeName', 'profileVersion', 'property',
        'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    