
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineConfigInfo(vim, *args, **kwargs):
    '''The ConfigInfo data object type encapsulates the configuration settings and
    virtual hardware for a virtual machine. This type holds all the information
    that is present in the .vmx configuration file for the virtual machine.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineConfigInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 13:
        raise IndexError('Expected at least 14 arguments got: %d' % len(args))

    required = [ 'alternateGuestName', 'changeVersion', 'defaultPowerOps', 'files', 'flags',
        'guestFullName', 'guestId', 'hardware', 'modified', 'name', 'template', 'uuid',
        'version' ]
    optional = [ 'annotation', 'bootOptions', 'changeTrackingEnabled', 'consolePreferences',
        'cpuAffinity', 'cpuAllocation', 'cpuFeatureMask', 'cpuHotAddEnabled',
        'cpuHotRemoveEnabled', 'datastoreUrl', 'extraConfig', 'firmware', 'ftInfo',
        'guestAutoLockEnabled', 'hotPlugMemoryIncrementSize', 'hotPlugMemoryLimit',
        'initialOverhead', 'instanceUuid', 'locationId', 'managedBy',
        'maxMksConnections', 'memoryAffinity', 'memoryAllocation',
        'memoryHotAddEnabled', 'memoryReservationLockedToMax', 'networkShaper',
        'npivDesiredNodeWwns', 'npivDesiredPortWwns', 'npivNodeWorldWideName',
        'npivOnNonRdmDisks', 'npivPortWorldWideName', 'npivTemporaryDisabled',
        'npivWorldWideNameType', 'swapPlacement', 'tools', 'vAppConfig',
        'vAssertsEnabled', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    