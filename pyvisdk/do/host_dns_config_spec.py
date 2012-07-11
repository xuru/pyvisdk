
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostDnsConfigSpec(vim, *args, **kwargs):
    '''Dataobject for configuring the DNS settings on the host.'''
    
    obj = vim.client.factory.create('ns0:HostDnsConfigSpec')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 4 arguments got: %d' % len(args))

    required = [ 'dhcp', 'domainName', 'hostName' ]
    optional = [ 'virtualNicConnection', 'address', 'searchDomain', 'virtualNicDevice',
        'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    