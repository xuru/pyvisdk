
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
    if (len(args) + len(kwargs)) < 37:
        raise IndexError('Expected at least 38 arguments got: %d' % len(args))

    required = [ 'backgroundSnapshotsSupported', 'cloneFromSnapshotSupported',
        'cpuMemoryResourceConfigurationSupported', 'datastorePrincipalSupported',
        'deltaDiskBackingsSupported', 'ftSupported', 'highGuestMemSupported',
        'iscsiSupported', 'localSwapDatastoreSupported', 'maintenanceModeSupported',
        'nfsSupported', 'nicTeamingSupported', 'perVMNetworkTrafficShapingSupported',
        'perVmSwapFiles', 'preAssignedPCIUnitNumbersSupported', 'rebootSupported',
        'recordReplaySupported', 'recursiveResourcePoolsSupported',
        'restrictedSnapshotRelocateSupported', 'sanSupported',
        'scaledScreenshotSupported', 'screenshotSupported', 'shutdownSupported',
        'snapshotRelayoutSupported', 'standbySupported', 'storageIORMSupported',
        'storageVMotionSupported', 'suspendedRelocateSupported', 'tpmSupported',
        'unsharedSwapVMotionSupported', 'virtualExecUsageSupported',
        'vlanTaggingSupported', 'vmDirectPathGen2Supported',
        'vmfsDatastoreMountCapable', 'vmotionSupported',
        'vmotionWithStorageVMotionSupported', 'vStorageCapable' ]
    optional = [ 'firewallIpRulesSupported', 'ftCompatibilityIssues', 'ipmiSupported',
        'loginBySSLThumbprintSupported', 'maxHostRunningVms', 'maxHostSupportedVcpus',
        'maxRunningVMs', 'maxSupportedVcpus', 'maxSupportedVMs',
        'replayCompatibilityIssues', 'replayUnsupportedReason',
        'servicePackageInfoSupported', 'supportedCpuFeature',
        'supportedVmfsMajorVersion', 'vmDirectPathGen2UnsupportedReason',
        'vmDirectPathGen2UnsupportedReasonExtended', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    