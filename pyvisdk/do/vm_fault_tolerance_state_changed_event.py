
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VmFaultToleranceStateChangedEvent(vim, *args, **kwargs):
    '''This event records a fault tolerance state change. A default alarm will be
    triggered upon this event, which would change the vm state: the vm state is red
    if the newState is needSecondary; the vm state is yellow if the newState is
    disabled; the vm state is green if the newState is notConfigured, starting,
    enabled or running'''
    
    obj = vim.client.factory.create('ns0:VmFaultToleranceStateChangedEvent')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 7:
        raise IndexError('Expected at least 8 arguments got: %d' % len(args))

    required = [ 'newState', 'oldState', 'template', 'chainId', 'createdTime', 'key', 'userName' ]
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
    