
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VmDasUpdateErrorEvent(vim, *args, **kwargs):
    '''The event records that an error occured when updating the HA agents with the
    current state of the virtual machine. If this occurs during a powerOn
    operation, the virtual machine will not be failed over in the event of a host
    failure. If it occurs during a powerOff, the virtual machine will be
    automatically powered on if the host it was last running on crashes.'''
    
    obj = vim.client.factory.create('ns0:VmDasUpdateErrorEvent')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 5:
        raise IndexError('Expected at least 6 arguments got: %d' % len(args))

    required = [ 'template', 'chainId', 'createdTime', 'key', 'userName' ]
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
    