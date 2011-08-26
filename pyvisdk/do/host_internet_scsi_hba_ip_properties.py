
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostInternetScsiHbaIPProperties(vim, *args, **kwargs):
    ''''''
    
    obj = vim.client.factory.create('ns0:HostInternetScsiHbaIPProperties')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))
        
    signature = [ 'dhcpConfigurationEnabled' ]
    inherited = [ 'address', 'alternateDnsServerAddress', 'arpRedirectEnabled', 'defaultGateway',
        'ipv6Address', 'ipv6DefaultGateway', 'ipv6SubnetMask', 'jumboFramesEnabled',
        'mac', 'mtu', 'primaryDnsServerAddress', 'subnetMask' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    