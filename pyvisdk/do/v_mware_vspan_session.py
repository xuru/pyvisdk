
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VMwareVspanSession(vim, *args, **kwargs):
    '''This class defines the configuration of a Distributed Port Mirroring session. A
    Distributed Port Mirroring session is used to mirror network traffic
    (inbound/outbound) from a set of source ports to a set of destination ports, to
    assist in troubleshooting, and as input for security and other network analysis
    appliances.Once a port is configured to be a source transmitted port on any
    Distributed Port Mirroring session, it can not be used as the destination port
    in any Distributed Port Mirroring session. Overlapping source ports among
    different Distributed Port Mirroring session is permitted but overlapping
    destination ports among different Distributed Port Mirroring session is not
    permitted.'''
    
    obj = vim.client.factory.create('ns0:VMwareVspanSession')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 4 arguments got: %d' % len(args))

    required = [ 'enabled', 'normalTrafficAllowed', 'stripOriginalVlan' ]
    optional = [ 'description', 'destinationPort', 'encapsulationVlanId', 'key',
        'mirroredPacketLength', 'name', 'sourcePortReceived', 'sourcePortTransmitted',
        'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    