
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DasAgentUnavailableEvent(vim, *args, **kwargs):
    '''This event records that VirtualCenter cannot contact any primary host in this
    HA cluster. HA designates some hosts as primary hosts in the HA cluster. When
    adding a new host to an existing cluster, HA needs to contact one of the
    primary hosts to finish the configuration. VirtualCenter has lost contact with
    all primary nodes in the connected state. Attempts to configure HA on a host in
    this cluster will fail until a DasAgentFoundEvent is logged or unless this is
    the first node to be configured. For example, if all the other hosts are
    disconnected first.'''
    
    obj = vim.client.factory.create('ns0:DasAgentUnavailableEvent')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 5 arguments got: %d' % len(args))

    required = [ 'chainId', 'createdTime', 'key', 'userName' ]
    optional = [ 'changeTag', 'computeResource', 'datacenter', 'ds', 'dvs',
        'fullFormattedMessage', 'host', 'net', 'vm', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    