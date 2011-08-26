
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def AlarmDescription(vim, *args, **kwargs):
    ''''''
    
    obj = vim.client.factory.create('ns0:AlarmDescription')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 10:
        raise IndexError('Expected at least 11 arguments got: %d' % len(args))
        
    signature = [ 'action', 'datastoreConnectionState', 'entityStatus', 'expr',
        'hostSystemConnectionState', 'hostSystemPowerState', 'metricOperator',
        'stateOperator', 'virtualMachineGuestHeartbeatStatus',
        'virtualMachinePowerState' ]
    inherited = [  ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    