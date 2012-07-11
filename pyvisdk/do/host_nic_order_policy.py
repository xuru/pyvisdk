
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostNicOrderPolicy(vim, *args, **kwargs):
    '''This data object type describes network adapter ordering policy for a network
    adapter team. A physical network adapter can be in the active list, the standby
    list, or neither. It cannot be in both lists. For a virtual switch, the
    NicOrderPolicy property is never null when retrieved from the server. When
    creating a new virtual switch or updating an existing virtual switch, the
    NicOrderPolicy can be null, in which case the default NicOrderPolicy from the
    server will be used. For a portgroup, a null NicOrderPolicy property means the
    portgroup inherits the policy from its parent. Otherwise, the NicOrderPolicy
    property defined in the portgroup takes precedence. In all cases where the
    NicOrderPolicy property is set, an empty activeNic array means there are no
    active Ethernet adapters in the team. An empty standbyNic array means there are
    no standby Ethernet adapters.'''
    
    obj = vim.client.factory.create('ns0:HostNicOrderPolicy')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))

    required = [  ]
    optional = [ 'activeNic', 'standbyNic', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    