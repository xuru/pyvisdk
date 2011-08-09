
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineCapability(DynamicData):
    '''This data object type contains information about the operation/capabailities of a
        virtual machine
    '''
    
    def __init__(self, bootOptionsSupported, bootRetryOptionsSupported, changeTrackingSupported, consolePreferencesSupported, cpuFeatureMaskSupported, disableSnapshotsSupported, diskSharesSupported, lockSnapshotsSupported, memorySnapshotsSupported, multipleSnapshotsSupported, npivWwnOnNonRdmVmSupported, poweredOffSnapshotsSupported, quiescedSnapshotsSupported, recordReplaySupported, revertToSnapshotSupported, s1AcpiManagementSupported, settingDisplayTopologySupported, settingScreenResolutionSupported, settingVideoRamSizeSupported, snapshotConfigSupported, snapshotOperationsSupported, swapPlacementSupported, toolsAutoUpdateSupported, toolsSyncTimeSupported, virtualMmuUsageSupported, vmNpivWwnDisableSupported, vmNpivWwnSupported, vmNpivWwnUpdateSupported):
        # MUST define these
        super(VirtualMachineCapability, self).__init__()
    
        self.data['bootOptionsSupported'] = bootOptionsSupported
        self.data['bootRetryOptionsSupported'] = bootRetryOptionsSupported
        self.data['changeTrackingSupported'] = changeTrackingSupported
        self.data['consolePreferencesSupported'] = consolePreferencesSupported
        self.data['cpuFeatureMaskSupported'] = cpuFeatureMaskSupported
        self.data['disableSnapshotsSupported'] = disableSnapshotsSupported
        self.data['diskSharesSupported'] = diskSharesSupported
        self.data['lockSnapshotsSupported'] = lockSnapshotsSupported
        self.data['memorySnapshotsSupported'] = memorySnapshotsSupported
        self.data['multipleSnapshotsSupported'] = multipleSnapshotsSupported
        self.data['npivWwnOnNonRdmVmSupported'] = npivWwnOnNonRdmVmSupported
        self.data['poweredOffSnapshotsSupported'] = poweredOffSnapshotsSupported
        self.data['quiescedSnapshotsSupported'] = quiescedSnapshotsSupported
        self.data['recordReplaySupported'] = recordReplaySupported
        self.data['revertToSnapshotSupported'] = revertToSnapshotSupported
        self.data['s1AcpiManagementSupported'] = s1AcpiManagementSupported
        self.data['settingDisplayTopologySupported'] = settingDisplayTopologySupported
        self.data['settingScreenResolutionSupported'] = settingScreenResolutionSupported
        self.data['settingVideoRamSizeSupported'] = settingVideoRamSizeSupported
        self.data['snapshotConfigSupported'] = snapshotConfigSupported
        self.data['snapshotOperationsSupported'] = snapshotOperationsSupported
        self.data['swapPlacementSupported'] = swapPlacementSupported
        self.data['toolsAutoUpdateSupported'] = toolsAutoUpdateSupported
        self.data['toolsSyncTimeSupported'] = toolsSyncTimeSupported
        self.data['virtualMmuUsageSupported'] = virtualMmuUsageSupported
        self.data['vmNpivWwnDisableSupported'] = vmNpivWwnDisableSupported
        self.data['vmNpivWwnSupported'] = vmNpivWwnSupported
        self.data['vmNpivWwnUpdateSupported'] = vmNpivWwnUpdateSupported
    
    
    @property
    def bootOptionsSupported(self):
        '''Indicates whether boot options can be configured for this virtual machine.
        '''
        return self.data['bootOptionsSupported']

    @property
    def bootRetryOptionsSupported(self):
        '''Indicates whether automatic boot retry can be configured for this virtual machine.
        '''
        return self.data['bootRetryOptionsSupported']

    @property
    def changeTrackingSupported(self):
        '''Indicates that change tracking is supported for virtual disks of this virtual
        machine. However, even if change tracking is supported, it might not be
        available for all disks of the virtual machine. For example, passthru raw
        disk mappings or disks backed by any Ver1BackingInfo cannot be tracked.
        '''
        return self.data['changeTrackingSupported']

    @property
    def consolePreferencesSupported(self):
        '''Indicates whether console preferences can be set for this virtual machine.
        '''
        return self.data['consolePreferencesSupported']

    @property
    def cpuFeatureMaskSupported(self):
        '''Indicates whether CPU feature requirements masks can be set for this virtual
        machine.
        '''
        return self.data['cpuFeatureMaskSupported']

    @property
    def disableSnapshotsSupported(self):
        '''Indicates whether or not snapshots can be disabled.
        '''
        return self.data['disableSnapshotsSupported']

    @property
    def diskSharesSupported(self):
        '''Indicates whether resource settings for disks can be applied to this virtual
        machine.
        '''
        return self.data['diskSharesSupported']

    @property
    def lockSnapshotsSupported(self):
        '''Indicates whether or not the snapshot tree can be locked.
        '''
        return self.data['lockSnapshotsSupported']

    @property
    def memorySnapshotsSupported(self):
        '''Indicates whether or not a virtual machine supports memory snapshots.
        '''
        return self.data['memorySnapshotsSupported']

    @property
    def multipleSnapshotsSupported(self):
        '''Indicates whether or not a virtual machine supports multiple snapshots. This value
        is not set when the virtual machine is unavailable, for instance, when it
        is being created or deleted.
        '''
        return self.data['multipleSnapshotsSupported']

    @property
    def npivWwnOnNonRdmVmSupported(self):
        '''Supports assigning NPIV WWN to virtual machines that don't have RDM disks.
        '''
        return self.data['npivWwnOnNonRdmVmSupported']

    @property
    def poweredOffSnapshotsSupported(self):
        '''Indicates whether or not a virtual machine supports snapshot operations in
        poweredOff state. This flag doesn't affect vim.VirtualMachine.GetSnapshot,
        which is always supported.
        '''
        return self.data['poweredOffSnapshotsSupported']

    @property
    def quiescedSnapshotsSupported(self):
        '''Indicates whether or not a virtual machine supports quiesced snapshots.
        '''
        return self.data['quiescedSnapshotsSupported']

    @property
    def recordReplaySupported(self):
        '''Indicates whether record and replay functionality is supported on this virtual
        machine.
        '''
        return self.data['recordReplaySupported']

    @property
    def revertToSnapshotSupported(self):
        '''Indicates whether or not a virtual machine supports reverting to a snapshot.
        '''
        return self.data['revertToSnapshotSupported']

    @property
    def s1AcpiManagementSupported(self):
        '''Indicates whether or not a virtual machine supports ACPI S1 settings management.
        '''
        return self.data['s1AcpiManagementSupported']

    @property
    def settingDisplayTopologySupported(self):
        '''Indicates whether of not this virtual machine supports setting the display
        topology of the console window. This capability depends on the guest
        operating system configured for this virtual machine.
        '''
        return self.data['settingDisplayTopologySupported']

    @property
    def settingScreenResolutionSupported(self):
        '''Indicates whether of not this virtual machine supports setting the screen
        resolution of the console window. This capability depends on the guest
        operating system configured for this virtual machine.
        '''
        return self.data['settingScreenResolutionSupported']

    @property
    def settingVideoRamSizeSupported(self):
        '''Flag indicating whether the video ram size of this virtual machine can be
        configured.
        '''
        return self.data['settingVideoRamSizeSupported']

    @property
    def snapshotConfigSupported(self):
        '''Indicates whether or not a virtual machine supports snapshot config.
        '''
        return self.data['snapshotConfigSupported']

    @property
    def snapshotOperationsSupported(self):
        '''Indicates whether or not a virtual machine supports snapshot operations.
        '''
        return self.data['snapshotOperationsSupported']

    @property
    def swapPlacementSupported(self):
        '''Flag indicating whether the virtual machine has a configurable swapfile placement
        policy.
        '''
        return self.data['swapPlacementSupported']

    @property
    def toolsAutoUpdateSupported(self):
        '''Supports tools auto-update.
        '''
        return self.data['toolsAutoUpdateSupported']

    @property
    def toolsSyncTimeSupported(self):
        '''Indicates whether asking tools to sync time with the host is supported.
        '''
        return self.data['toolsSyncTimeSupported']

    @property
    def virtualMmuUsageSupported(self):
        '''Indicates whether or not the use of nested page table hardware support can be
        explicitly set.
        '''
        return self.data['virtualMmuUsageSupported']

    @property
    def vmNpivWwnDisableSupported(self):
        '''Indicates whether the NPIV disabling operation is supported the virtual machine.
        '''
        return self.data['vmNpivWwnDisableSupported']

    @property
    def vmNpivWwnSupported(self):
        '''Supports virtual machine NPIV WWN.
        '''
        return self.data['vmNpivWwnSupported']

    @property
    def vmNpivWwnUpdateSupported(self):
        '''Indicates whether the update of NPIV WWNs are supported on the virtual machine.
        '''
        return self.data['vmNpivWwnUpdateSupported']

