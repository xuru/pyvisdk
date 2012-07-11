
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def AlarmDescription(vim, *args, **kwargs):
    '''Static strings for alarms.'''
    
    obj = vim.client.factory.create('ns0:AlarmDescription')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 10:
        raise IndexError('Expected at least 11 arguments got: %d' % len(args))

    required = [ 'action', 'datastoreConnectionState', 'entityStatus', 'expr',
        'hostSystemConnectionState', 'hostSystemPowerState', 'metricOperator',
        'stateOperator', 'virtualMachineGuestHeartbeatStatus',
        'virtualMachinePowerState' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    