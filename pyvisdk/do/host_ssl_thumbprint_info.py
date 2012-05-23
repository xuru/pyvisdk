
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostSslThumbprintInfo(vim, *args, **kwargs):
    '''The SSL thumbprint information for a host managed by a vCenter Server or a
    vCenter extension to login into other hosts without username/password
    authentication.'''
    
    obj = vim.client.factory.create('ns0:HostSslThumbprintInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))

    required = [ 'ownerTag', 'principal' ]
    optional = [ 'sslThumbprints', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    