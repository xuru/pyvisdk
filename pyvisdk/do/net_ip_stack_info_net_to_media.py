
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def NetIpStackInfoNetToMedia(vim, *args, **kwargs):
    '''Information from an IP stack about known mappings betwwen an IP address and the
    underlying physical address it maps to as learned by: IPv4: Address Resolution
    Protocol (ARP) RFC 826 IPv6: Neighbor Discovery Protocol (NDP) RFC 4861'''
    
    obj = vim.client.factory.create('ns0:NetIpStackInfoNetToMedia')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 5 arguments got: %d' % len(args))

    required = [ 'device', 'ipAddress', 'physicalAddress', 'type' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    