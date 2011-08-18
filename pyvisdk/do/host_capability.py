# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostCapability(vim, *args, **kwargs):
    '''Specifies the capabilities of the particular host. This set of capabilities is
    referenced in other parts of the API specification to indicate under what
    circumstances an API will throw a NotSupported fault.'''
    
    obj = vim.client.factory.create('ns0:HostCapability')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 5:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'backgroundSnapshotsSupported', 'cloneFromSnapshotSupported',
        'cpuMemoryResourceConfigurationSupported', 'datastorePrincipalSupported',
        'deltaDiskBackingsSupported', 'ftCompatibilityIssues', 'ftSupported',
        'highGuestMemSupported', 'ipmiSupported', 'iscsiSupported',
        'localSwapDatastoreSupported', 'loginBySSLThumbprintSupported',
        'maintenanceModeSupported', 'maxRunningVMs', 'maxSupportedVcpus',
        'maxSupportedVMs', 'nfsSupported', 'nicTeamingSupported',
        'perVMNetworkTrafficShapingSupported', 'perVmSwapFiles',
        'preAssignedPCIUnitNumbersSupported', 'rebootSupported',
        'recordReplaySupported', 'recursiveResourcePoolsSupported',
        'replayCompatibilityIssues', 'replayUnsupportedReason',
        'restrictedSnapshotRelocateSupported', 'sanSupported',
        'scaledScreenshotSupported', 'screenshotSupported', 'shutdownSupported',
        'standbySupported', 'storageIORMSupported', 'storageVMotionSupported',
        'supportedCpuFeature', 'suspendedRelocateSupported', 'tpmSupported',
        'unsharedSwapVMotionSupported', 'virtualExecUsageSupported',
        'vlanTaggingSupported', 'vmDirectPathGen2Supported',
        'vmDirectPathGen2UnsupportedReason',
        'vmDirectPathGen2UnsupportedReasonExtended', 'vmotionSupported',
        'vmotionWithStorageVMotionSupported', 'vStorageCapable' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    