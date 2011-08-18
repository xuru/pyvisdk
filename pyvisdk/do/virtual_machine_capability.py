# -*- coding: ascii -*-

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
    if (len(args) + len(kwargs)) < 28:
        raise IndexError('Expected at least 29 arguments got: %d' % len(args))
        
    signature = [ 'bootOptionsSupported', 'bootRetryOptionsSupported', 'changeTrackingSupported',
        'consolePreferencesSupported', 'cpuFeatureMaskSupported',
        'disableSnapshotsSupported', 'diskSharesSupported', 'lockSnapshotsSupported',
        'memorySnapshotsSupported', 'multipleSnapshotsSupported',
        'npivWwnOnNonRdmVmSupported', 'poweredOffSnapshotsSupported',
        'quiescedSnapshotsSupported', 'recordReplaySupported',
        'revertToSnapshotSupported', 's1AcpiManagementSupported',
        'settingDisplayTopologySupported', 'settingScreenResolutionSupported',
        'settingVideoRamSizeSupported', 'snapshotConfigSupported',
        'snapshotOperationsSupported', 'swapPlacementSupported',
        'toolsAutoUpdateSupported', 'toolsSyncTimeSupported',
        'virtualMmuUsageSupported', 'vmNpivWwnDisableSupported', 'vmNpivWwnSupported',
        'vmNpivWwnUpdateSupported' ]
    inherited = [  ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    