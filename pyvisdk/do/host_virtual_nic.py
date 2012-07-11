
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostVirtualNic(vim, *args, **kwargs):
    '''This data object type describes a virtual network adapter representing an
    adapter that connects to a virtual switch. A VirtualNic differs from a
    PhysicalNic in that the latter corresponds to a physical device that is
    connected to the physical network. The former is a virtual device that is
    connected to a virtual switch. A VirtualNic accesses the external network
    through a virtual switch that is bridged through a PhysicalNic to a physical
    network.'''
    
    obj = vim.client.factory.create('ns0:HostVirtualNic')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 5 arguments got: %d' % len(args))

    required = [ 'device', 'key', 'portgroup', 'spec' ]
    optional = [ 'port', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    