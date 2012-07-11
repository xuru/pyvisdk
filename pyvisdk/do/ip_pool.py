
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def IpPool(vim, *args, **kwargs):
    '''Specifications of the network configuration to be used on a network. This is
    used to generate IP addresses and for self-customization of vApps.'''
    
    obj = vim.client.factory.create('ns0:IpPool')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))

    required = [  ]
    optional = [ 'dnsDomain', 'dnsSearchPath', 'hostPrefix', 'httpProxy', 'id', 'ipv4Config',
        'ipv6Config', 'name', 'networkAssociation', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    