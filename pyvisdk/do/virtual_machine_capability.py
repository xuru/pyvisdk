
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineCapability(vim, *args, **kwargs):
    '''This data object type contains information about the operation/capabailities of
    a virtual machine'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineCapability')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 32:
        raise IndexError('Expected at least 33 arguments got: %d' % len(args))

    required = [ 'bootOptionsSupported', 'bootRetryOptionsSupported', 'changeTrackingSupported',
        'consolePreferencesSupported', 'cpuFeatureMaskSupported',
        'disableSnapshotsSupported', 'diskSharesSupported', 'guestAutoLockSupported',
        'hostBasedReplicationSupported', 'lockSnapshotsSupported',
        'memoryReservationLockSupported', 'memorySnapshotsSupported',
        'multipleCoresPerSocketSupported', 'multipleSnapshotsSupported',
        'npivWwnOnNonRdmVmSupported', 'poweredOffSnapshotsSupported',
        'quiescedSnapshotsSupported', 'recordReplaySupported',
        'revertToSnapshotSupported', 's1AcpiManagementSupported',
        'settingDisplayTopologySupported', 'settingScreenResolutionSupported',
        'settingVideoRamSizeSupported', 'snapshotConfigSupported',
        'snapshotOperationsSupported', 'swapPlacementSupported',
        'toolsAutoUpdateSupported', 'toolsSyncTimeSupported',
        'virtualMmuUsageSupported', 'vmNpivWwnDisableSupported', 'vmNpivWwnSupported',
        'vmNpivWwnUpdateSupported' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    