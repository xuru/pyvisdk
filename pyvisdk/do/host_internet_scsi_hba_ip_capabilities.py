
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostInternetScsiHbaIPCapabilities(vim, *args, **kwargs):
    '''The IP Capabilities for the host bus adapter'''
    
    obj = vim.client.factory.create('ns0:HostInternetScsiHbaIPCapabilities')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 6:
        raise IndexError('Expected at least 7 arguments got: %d' % len(args))

    required = [ 'addressSettable', 'alternateDnsServerAddressSettable',
        'defaultGatewaySettable', 'ipConfigurationMethodSettable',
        'primaryDnsServerAddressSettable', 'subnetMaskSettable' ]
    optional = [ 'arpRedirectSettable', 'hostNameAsTargetAddress', 'ipv6Supported',
        'mtuSettable', 'nameAliasSettable', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    