
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostCapability(DynamicData):
    '''Specifies the capabilities of the particular host. This set of capabilities is
        referenced in other parts of the API specification to indicate under what
        circumstances an API will throw a NotSupported fault.
    '''
    
    def __init__(self, backgroundSnapshotsSupported, cloneFromSnapshotSupported, cpuMemoryResourceConfigurationSupported, datastorePrincipalSupported, deltaDiskBackingsSupported, ftCompatibilityIssues, ftSupported, highGuestMemSupported, ipmiSupported, iscsiSupported, localSwapDatastoreSupported, loginBySSLThumbprintSupported, maintenanceModeSupported, maxRunningVMs, maxSupportedVcpus, maxSupportedVMs, nfsSupported, nicTeamingSupported, perVMNetworkTrafficShapingSupported, perVmSwapFiles, preAssignedPCIUnitNumbersSupported, rebootSupported, recordReplaySupported, recursiveResourcePoolsSupported, replayCompatibilityIssues, replayUnsupportedReason, restrictedSnapshotRelocateSupported, sanSupported, scaledScreenshotSupported, screenshotSupported, shutdownSupported, standbySupported, storageIORMSupported, storageVMotionSupported, supportedCpuFeature, suspendedRelocateSupported, tpmSupported, unsharedSwapVMotionSupported, virtualExecUsageSupported, vlanTaggingSupported, vmDirectPathGen2Supported, vmDirectPathGen2UnsupportedReason, vmDirectPathGen2UnsupportedReasonExtended, vmotionSupported, vmotionWithStorageVMotionSupported, vStorageCapable):
        # MUST define these
        super(HostCapability, self).__init__()
    
        self.data['backgroundSnapshotsSupported'] = backgroundSnapshotsSupported
        self.data['cloneFromSnapshotSupported'] = cloneFromSnapshotSupported
        self.data['cpuMemoryResourceConfigurationSupported'] = cpuMemoryResourceConfigurationSupported
        self.data['datastorePrincipalSupported'] = datastorePrincipalSupported
        self.data['deltaDiskBackingsSupported'] = deltaDiskBackingsSupported
        self.data['ftCompatibilityIssues'] = ftCompatibilityIssues
        self.data['ftSupported'] = ftSupported
        self.data['highGuestMemSupported'] = highGuestMemSupported
        self.data['ipmiSupported'] = ipmiSupported
        self.data['iscsiSupported'] = iscsiSupported
        self.data['localSwapDatastoreSupported'] = localSwapDatastoreSupported
        self.data['loginBySSLThumbprintSupported'] = loginBySSLThumbprintSupported
        self.data['maintenanceModeSupported'] = maintenanceModeSupported
        self.data['maxRunningVMs'] = maxRunningVMs
        self.data['maxSupportedVcpus'] = maxSupportedVcpus
        self.data['maxSupportedVMs'] = maxSupportedVMs
        self.data['nfsSupported'] = nfsSupported
        self.data['nicTeamingSupported'] = nicTeamingSupported
        self.data['perVMNetworkTrafficShapingSupported'] = perVMNetworkTrafficShapingSupported
        self.data['perVmSwapFiles'] = perVmSwapFiles
        self.data['preAssignedPCIUnitNumbersSupported'] = preAssignedPCIUnitNumbersSupported
        self.data['rebootSupported'] = rebootSupported
        self.data['recordReplaySupported'] = recordReplaySupported
        self.data['recursiveResourcePoolsSupported'] = recursiveResourcePoolsSupported
        self.data['replayCompatibilityIssues'] = replayCompatibilityIssues
        self.data['replayUnsupportedReason'] = replayUnsupportedReason
        self.data['restrictedSnapshotRelocateSupported'] = restrictedSnapshotRelocateSupported
        self.data['sanSupported'] = sanSupported
        self.data['scaledScreenshotSupported'] = scaledScreenshotSupported
        self.data['screenshotSupported'] = screenshotSupported
        self.data['shutdownSupported'] = shutdownSupported
        self.data['standbySupported'] = standbySupported
        self.data['storageIORMSupported'] = storageIORMSupported
        self.data['storageVMotionSupported'] = storageVMotionSupported
        self.data['supportedCpuFeature'] = supportedCpuFeature
        self.data['suspendedRelocateSupported'] = suspendedRelocateSupported
        self.data['tpmSupported'] = tpmSupported
        self.data['unsharedSwapVMotionSupported'] = unsharedSwapVMotionSupported
        self.data['virtualExecUsageSupported'] = virtualExecUsageSupported
        self.data['vlanTaggingSupported'] = vlanTaggingSupported
        self.data['vmDirectPathGen2Supported'] = vmDirectPathGen2Supported
        self.data['vmDirectPathGen2UnsupportedReason'] = vmDirectPathGen2UnsupportedReason
        self.data['vmDirectPathGen2UnsupportedReasonExtended'] = vmDirectPathGen2UnsupportedReasonExtended
        self.data['vmotionSupported'] = vmotionSupported
        self.data['vmotionWithStorageVMotionSupported'] = vmotionWithStorageVMotionSupported
        self.data['vStorageCapable'] = vStorageCapable
    
    
    @property
    def backgroundSnapshotsSupported(self):
        '''Flag indicating whether background snapshots are supported on this host.
        '''
        return self.data['backgroundSnapshotsSupported']

    @property
    def cloneFromSnapshotSupported(self):
        '''Indicates whether or not cloning a virtual machine from a snapshot point is
        allowed.
        '''
        return self.data['cloneFromSnapshotSupported']

    @property
    def cpuMemoryResourceConfigurationSupported(self):
        '''Flag indicating whether cpu and memory resource configuration is supported. If
        this is set to false, UpdateConfig, UpdateChildResourceConfiguration
        cannot be used for changing the cpu/memory resource configurations.
        '''
        return self.data['cpuMemoryResourceConfigurationSupported']

    @property
    def datastorePrincipalSupported(self):
        '''Flag indicating whether datastore principal user is supported on the host.
        '''
        return self.data['datastorePrincipalSupported']

    @property
    def deltaDiskBackingsSupported(self):
        '''Flag indicating whether explicitly creating arbirary configurations of delta disk
        backings is supported.
        '''
        return self.data['deltaDiskBackingsSupported']

    @property
    def ftCompatibilityIssues(self):
        '''For a host which doesn't support Fault Tolerance, indicates all the reasons for
        the incompatibility. HostCapabilityFtUnsupportedReason lists the set of
        possible values.
        '''
        return self.data['ftCompatibilityIssues']

    @property
    def ftSupported(self):
        '''Indicates whether this host supports Fault Tolerance There can be many reasons why
        a host does not support Fault Tolerance, which includes CPU compatibility,
        product compatibility as well as other host configuration settings. For
        specific reasons, look into replayCompatibilityIssues and
        ftCompatibilityIssues
        '''
        return self.data['ftSupported']

    @property
    def highGuestMemSupported(self):
        '''Is high guest memory supported.
        '''
        return self.data['highGuestMemSupported']

    @property
    def ipmiSupported(self):
        '''Flag indicating whether the host supports IPMI (Intelligent Platform Management
        Interface). XXX - Make ipmiSupported optional until there is a compatible
        hostagent.
        '''
        return self.data['ipmiSupported']

    @property
    def iscsiSupported(self):
        '''Is access to iSCSI devices supported.
        '''
        return self.data['iscsiSupported']

    @property
    def localSwapDatastoreSupported(self):
        '''Flag indicating whether the host supports selecting a datastore that that may be
        used to store virtual machine swapfiles.
        '''
        return self.data['localSwapDatastoreSupported']

    @property
    def loginBySSLThumbprintSupported(self):
        '''Flag indicating whether this host supports SSL thumbprint authentication
        '''
        return self.data['loginBySSLThumbprintSupported']

    @property
    def maintenanceModeSupported(self):
        '''Is maintenance mode supported
        '''
        return self.data['maintenanceModeSupported']

    @property
    def maxRunningVMs(self):
        '''The maximum number of virtual machines that can be running simultaneously on this
        host. If this capability is not set, the number of virtual machines
        running simultaneously is unlimited.
        '''
        return self.data['maxRunningVMs']

    @property
    def maxSupportedVcpus(self):
        '''The maximum number of virtual CPUs supported per virtual machine. If this
        capability is not set, the number is unlimited.
        '''
        return self.data['maxSupportedVcpus']

    @property
    def maxSupportedVMs(self):
        '''The maximum number of virtual machines that can exist on this host. If this
        capability is not set, the number of virtual machines is unlimited.
        '''
        return self.data['maxSupportedVMs']

    @property
    def nfsSupported(self):
        '''Is access to NFS devices supported.
        '''
        return self.data['nfsSupported']

    @property
    def nicTeamingSupported(self):
        '''Is NIC teaming supported.
        '''
        return self.data['nicTeamingSupported']

    @property
    def perVMNetworkTrafficShapingSupported(self):
        '''Indicates whether network traffic shaping on a per virtual machine basis is
        supported.
        '''
        return self.data['perVMNetworkTrafficShapingSupported']

    @property
    def perVmSwapFiles(self):
        '''Flag indicating whether virtual machine execution on this host involves a swapfile
        for each virtual machine. If true, the swapfile placement for a powered-on
        virtual machine is advertised in its FileLayout by the swapFile property.
        '''
        return self.data['perVmSwapFiles']

    @property
    def preAssignedPCIUnitNumbersSupported(self):
        '''Flag to indicate whether the server returns unit numbers in a pre-assigned range
        for devices on the PCI bus. When the server supports this flag, the device
        unit number namespace is partitioned by device type. Different types of
        devices will sit in a specific range of unit numbers that may not
        correspond to physical slots in the pci bus but present a relative
        ordering of the devices with respect to other devices of the same type.
        Note that this does not mean that the user can set the relative ordering
        between device types, but only allows stable orderings between devices of
        the same type. The unit number will now clearly represent an ordering
        between devices of the same type. unitNumber This property is only
        available for devices on the pci controller.
        '''
        return self.data['preAssignedPCIUnitNumbersSupported']

    @property
    def rebootSupported(self):
        '''Flag indicating whether rebooting the host is supported.
        '''
        return self.data['rebootSupported']

    @property
    def recordReplaySupported(self):
        '''Indicates whether this host supports record and replay
        '''
        return self.data['recordReplaySupported']

    @property
    def recursiveResourcePoolsSupported(self):
        '''
        '''
        return self.data['recursiveResourcePoolsSupported']

    @property
    def replayCompatibilityIssues(self):
        '''For a host which doesn't support replay, indicates all the reasons for the
        incompatibility. HostReplayUnsupportedReason lists the set of possible
        values.
        '''
        return self.data['replayCompatibilityIssues']

    @property
    def replayUnsupportedReason(self):
        '''For a host whose CPU doesn't support replay, indicates the reason for the
        incompatibility. HostReplayUnsupportedReason represents the set of
        possible values.
        '''
        return self.data['replayUnsupportedReason']

    @property
    def restrictedSnapshotRelocateSupported(self):
        '''Indicates whether this host supports relocation of virtual machines with
        snapshots. Must be true on the source and destination hosts for the
        relocation to work. Even if this is true, the following conditions must
        hold: 1) All the the vm's files are in one directory prior to the
        relocate. 2) All of the vm's files will be in one directory after the
        relocate. 3) The source and destination hosts are the same product
        version.
        '''
        return self.data['restrictedSnapshotRelocateSupported']

    @property
    def sanSupported(self):
        '''Flag indicating whether access to SAN devices is supported.
        '''
        return self.data['sanSupported']

    @property
    def scaledScreenshotSupported(self):
        '''Indicates whether scaling is supported for screenshots retrieved over https. If
        true, screenshot retrieval supports the additional optional parameters
        'width' and 'height'. After cropping, the returned image will be scaled to
        these dimensions. If only one of these parameters is specified, default
        behavior is to return an image roughly proportional to the source image.
        '''
        return self.data['scaledScreenshotSupported']

    @property
    def screenshotSupported(self):
        '''Indicates whether the screenshot retrival over https is supported for this host's
        virtual machines. If true, a screenshot can be retrieved at the HTTPS
        relative path
        '''
        return self.data['screenshotSupported']

    @property
    def shutdownSupported(self):
        '''Flag indicating whether the host can be powered off
        '''
        return self.data['shutdownSupported']

    @property
    def standbySupported(self):
        '''Flag indicating whether you can put the host in a power down state, from which it
        can be powered up automatically.
        '''
        return self.data['standbySupported']

    @property
    def storageIORMSupported(self):
        '''Indicates whether the host supports storage I/O resource management.
        '''
        return self.data['storageIORMSupported']

    @property
    def storageVMotionSupported(self):
        '''Indicates whether the storage of a powered-on virtual machine may be relocated.
        '''
        return self.data['storageVMotionSupported']

    @property
    def supportedCpuFeature(self):
        '''CPU feature set that is supported by the virtualization platform. This feature set
        may reflect characteristics of the product capabilities and licensing. For
        any feature marked '-', reference the cpuFeature array of the host's
        HardwareInfo to determine the correct value.
        '''
        return self.data['supportedCpuFeature']

    @property
    def suspendedRelocateSupported(self):
        '''Indicates whether this host supports relocation of suspended virtual machines.
        Must be true on the source and destination hosts for the relocation to
        work.
        '''
        return self.data['suspendedRelocateSupported']

    @property
    def tpmSupported(self):
        '''Flag indicating whether this host supports the integrity measurement using a TPM
        device.
        '''
        return self.data['tpmSupported']

    @property
    def unsharedSwapVMotionSupported(self):
        '''Flag indicating whether the host supports participating in a VMotion where the
        virtual machine swapfile is not visible to the destination.
        '''
        return self.data['unsharedSwapVMotionSupported']

    @property
    def virtualExecUsageSupported(self):
        '''Indicates whether the host supports configuring hardware virtualization (HV)
        support for virtual machines.
        '''
        return self.data['virtualExecUsageSupported']

    @property
    def vlanTaggingSupported(self):
        '''Is VLAN Tagging supported.
        '''
        return self.data['vlanTaggingSupported']

    @property
    def vmDirectPathGen2Supported(self):
        '''Indicates whether the host supports network passthrough using VMDirectPath Gen 2.
        Note that this is a general capability for the host and is independent of
        support by a given physical NIC. If false, the reason(s) for lack of
        support will be provided in vmDirectPathGen2UnsupportedReason and/or in
        vmDirectPathGen2UnsupportedReasonExtended.
        '''
        return self.data['vmDirectPathGen2Supported']

    @property
    def vmDirectPathGen2UnsupportedReason(self):
        '''If vmDirectPathGen2Supported is false, this array will be populated with reasons
        for the lack of support (chosen from VmDirectPathGen2UnsupportedReason).
        If there is a reason for the lack of support that cannot be described by
        the available constants, vmDirectPathGen2UnsupportedReasonExtended will be
        populated with an additional explanation provided by the platform.
        '''
        return self.data['vmDirectPathGen2UnsupportedReason']

    @property
    def vmDirectPathGen2UnsupportedReasonExtended(self):
        '''If vmDirectPathGen2Supported is false, this property may contain an explanation
        provided by the platform, beyond the reasons (if any) enumerated in
        vmDirectPathGen2UnsupportedReason.
        '''
        return self.data['vmDirectPathGen2UnsupportedReasonExtended']

    @property
    def vmotionSupported(self):
        '''Flag indicating whether you can perform VMotion.
        '''
        return self.data['vmotionSupported']

    @property
    def vmotionWithStorageVMotionSupported(self):
        '''Indicates whether the storage of a powered-on virtual machine may be relocated
        while simultaneously changing the execution host of the virtual machine.
        '''
        return self.data['vmotionWithStorageVMotionSupported']

    @property
    def vStorageCapable(self):
        '''Indicates whether the host supports vStorage Hardware acceleration.
        '''
        return self.data['vStorageCapable']

