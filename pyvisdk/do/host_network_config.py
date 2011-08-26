
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostNetworkConfig(vim, *args, **kwargs):
    ''''''
    
    obj = vim.client.factory.create('ns0:HostNetworkConfig')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))
        
    signature = [  ]
    inherited = [ 'consoleIpRouteConfig', 'consoleVnic', 'dhcp', 'dnsConfig', 'ipRouteConfig',
        'ipV6Enabled', 'nat', 'pnic', 'portgroup', 'proxySwitch', 'routeTableConfig',
        'vnic', 'vswitch' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    