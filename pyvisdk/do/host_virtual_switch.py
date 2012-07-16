
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostVirtualSwitch(vim, *args, **kwargs):
    '''The virtual switch is a software entity to which multiple virtual network
    adapters can connect to create a virtual network. It can also be bridged to a
    physical network.'''
    
    obj = vim.client.factory.create('ns0:HostVirtualSwitch')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 5:
        raise IndexError('Expected at least 6 arguments got: %d' % len(args))

    required = [ 'key', 'name', 'numPorts', 'numPortsAvailable', 'spec' ]
    optional = [ 'mtu', 'pnic', 'portgroup', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    