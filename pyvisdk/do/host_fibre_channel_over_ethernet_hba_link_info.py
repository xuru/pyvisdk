
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostFibreChannelOverEthernetHbaLinkInfo(vim, *args, **kwargs):
    '''Represents FCoE link information. The link information represents a VNPort to
    VFPort Virtual Link, as described in the FC-BB-5 standard, with the addition of
    the VLAN ID over which a link exists.'''
    
    obj = vim.client.factory.create('ns0:HostFibreChannelOverEthernetHbaLinkInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 4 arguments got: %d' % len(args))

    required = [ 'fcfMac', 'vlanId', 'vnportMac' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    