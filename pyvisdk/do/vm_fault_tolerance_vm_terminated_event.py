
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VmFaultToleranceVmTerminatedEvent(vim, *args, **kwargs):
    '''This event records a secondary or primary VM is terminated. The reason could be
    : divergence, lost connection to secondary, partial hardware failure of
    secondary, or by user.'''
    
    obj = vim.client.factory.create('ns0:VmFaultToleranceVmTerminatedEvent')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 5:
        raise IndexError('Expected at least 6 arguments got: %d' % len(args))

    required = [ 'template', 'chainId', 'createdTime', 'key', 'userName' ]
    optional = [ 'reason', 'changeTag', 'computeResource', 'datacenter', 'ds', 'dvs',
        'fullFormattedMessage', 'host', 'net', 'vm', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    