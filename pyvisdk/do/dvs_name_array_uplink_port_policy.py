
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DVSNameArrayUplinkPortPolicy(vim, *args, **kwargs):
    '''The uplink port policy specifies an array of uniform names for the uplink ports
    across the hosts. The size of the array indicates the number of uplink ports
    that will be created for each host in the switch.When the names in this array
    change, the uplink ports on all the hosts are automatically renamed
    accordingly. Increasing the number of names in the array automatically creates
    additional uplink ports bearing the added name on each host. Decreasing the
    number of name automatically deletes the unused uplink ports on each host.
    Decreasing beyond the number of unused uplink port raises a fault.This policy
    overrides the portgroup's port naming format, if both are defined and the
    uplink ports are created in a uplink portgroup.'''
    
    obj = vim.client.factory.create('ns0:DVSNameArrayUplinkPortPolicy')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))

    required = [ 'uplinkPortName' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    