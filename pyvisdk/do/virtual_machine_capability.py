# -*- coding: ascii -*-

import logging

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
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'bootOptionsSupported', 'bootRetryOptionsSupported', 'changeTrackingSupported',
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
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    