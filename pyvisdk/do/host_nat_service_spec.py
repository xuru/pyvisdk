
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostNatServiceSpec(vim, *args, **kwargs):
    '''This data object type provides the details about the Network Address
    Translation (NAT) service.'''
    
    obj = vim.client.factory.create('ns0:HostNatServiceSpec')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 6:
        raise IndexError('Expected at least 7 arguments got: %d' % len(args))

    required = [ 'activeFtp', 'allowAnyOui', 'configPort', 'ipGatewayAddress', 'udpTimeout',
        'virtualSwitch' ]
    optional = [ 'nameService', 'portForward', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    