
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostNatServiceNameServiceSpec(vim, *args, **kwargs):
    '''This data object type specifies the information for the name servers.'''
    
    obj = vim.client.factory.create('ns0:HostNatServiceNameServiceSpec')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 7:
        raise IndexError('Expected at least 8 arguments got: %d' % len(args))

    required = [ 'dnsAutoDetect', 'dnsPolicy', 'dnsRetries', 'dnsTimeout', 'nbdsTimeout',
        'nbnsRetries', 'nbnsTimeout' ]
    optional = [ 'dnsNameServer', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    