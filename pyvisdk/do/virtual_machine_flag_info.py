
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineFlagInfo(vim, *args, **kwargs):
    '''The FlagInfo data object type encapsulates the flag settings for a virtual
    machine. These properties are optional since the same structure is used to
    change the values during an edit or create operation.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineFlagInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))

    required = [  ]
    optional = [ 'disableAcceleration', 'diskUuidEnabled', 'enableLogging', 'htSharing',
        'monitorType', 'recordReplayEnabled', 'runWithDebugInfo', 'snapshotDisabled',
        'snapshotLocked', 'snapshotPowerOffBehavior', 'useToe', 'virtualExecUsage',
        'virtualMmuUsage', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    