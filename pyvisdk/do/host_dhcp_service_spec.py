
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostDhcpServiceSpec(vim, *args, **kwargs):
    ''''''
    
    obj = vim.client.factory.create('ns0:HostDhcpServiceSpec')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 8:
        raise IndexError('Expected at least 9 arguments got: %d' % len(args))

    required = [ 'defaultLeaseDuration', 'ipSubnetAddr', 'ipSubnetMask', 'leaseBeginIp',
        'leaseEndIp', 'maxLeaseDuration', 'unlimitedLease', 'virtualSwitch' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    