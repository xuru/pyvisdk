
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def NetworkProfileDnsConfigProfile(vim, *args, **kwargs):
    '''The NetworkProfileDnsConfigProfile data object represents DNS configuration for
    the host. Use the policy list for access to configuration data for the DNS
    profile. Use the property list for access to subprofiles, if any.'''
    
    obj = vim.client.factory.create('ns0:NetworkProfileDnsConfigProfile')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))

    required = [ 'enabled' ]
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
    