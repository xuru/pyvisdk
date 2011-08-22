
import logging
from pyvisdk.exceptions import InvalidArgumentError

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
    if (len(args) + len(kwargs)) < 35:
        raise IndexError('Expected at least 36 arguments got: %d' % len(args))
        
    signature = [ 'backgroundSnapshotsSupported', 'cloneFromSnapshotSupported',
        'cpuMemoryResourceConfigurationSupported', 'datastorePrincipalSupported',
        'deltaDiskBackingsSupported', 'ftSupported', 'highGuestMemSupported',
        'iscsiSupported', 'localSwapDatastoreSupported', 'maintenanceModeSupported',
        'nfsSupported', 'nicTeamingSupported', 'perVMNetworkTrafficShapingSupported',
        'perVmSwapFiles', 'preAssignedPCIUnitNumbersSupported', 'rebootSupported',
        'recordReplaySupported', 'recursiveResourcePoolsSupported',
        'restrictedSnapshotRelocateSupported', 'sanSupported',
        'scaledScreenshotSupported', 'screenshotSupported', 'shutdownSupported',
        'standbySupported', 'storageIORMSupported', 'storageVMotionSupported',
        'suspendedRelocateSupported', 'tpmSupported', 'unsharedSwapVMotionSupported',
        'virtualExecUsageSupported', 'vlanTaggingSupported',
        'vmDirectPathGen2Supported', 'vmotionSupported',
        'vmotionWithStorageVMotionSupported', 'vStorageCapable' ]
    inherited = [ 'ftCompatibilityIssues', 'ipmiSupported', 'loginBySSLThumbprintSupported',
        'maxRunningVMs', 'maxSupportedVcpus', 'maxSupportedVMs',
        'replayCompatibilityIssues', 'replayUnsupportedReason', 'supportedCpuFeature',
        'vmDirectPathGen2UnsupportedReason',
        'vmDirectPathGen2UnsupportedReasonExtended' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    