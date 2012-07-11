
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostProxySwitch(vim, *args, **kwargs):
    '''The HostProxySwitch is a software entity which represents the component of a
    DistributedVirtualSwitch on a particular host.'''
    
    obj = vim.client.factory.create('ns0:HostProxySwitch')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 6:
        raise IndexError('Expected at least 7 arguments got: %d' % len(args))

    required = [ 'dvsName', 'dvsUuid', 'key', 'numPorts', 'numPortsAvailable', 'spec' ]
    optional = [ 'configNumPorts', 'mtu', 'pnic', 'uplinkPort', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    