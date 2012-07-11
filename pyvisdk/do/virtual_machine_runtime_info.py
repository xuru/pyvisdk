
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineRuntimeInfo(vim, *args, **kwargs):
    '''The RuntimeInfo data object type provides information about the execution state
    and history of a virtual machine.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineRuntimeInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 7:
        raise IndexError('Expected at least 8 arguments got: %d' % len(args))

    required = [ 'connectionState', 'consolidationNeeded', 'faultToleranceState',
        'numMksConnections', 'powerState', 'recordReplayState', 'toolsInstallerMounted' ]
    optional = [ 'bootTime', 'cleanPowerOff', 'dasVmProtection', 'device', 'host',
        'maxCpuUsage', 'maxMemoryUsage', 'memoryOverhead', 'minRequiredEVCModeKey',
        'needSecondaryReason', 'question', 'suspendInterval', 'suspendTime',
        'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    