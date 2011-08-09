
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineFlagInfo(DynamicData):
    '''The FlagInfo data object type encapsulates the flag settings for a virtual
        machine. These properties are optional since the same structure is used to
        change the values during an edit or create operation.
    '''
    
    def __init__(self, disableAcceleration, diskUuidEnabled, enableLogging, htSharing, monitorType, recordReplayEnabled, runWithDebugInfo, snapshotDisabled, snapshotLocked, snapshotPowerOffBehavior, useToe, virtualExecUsage, virtualMmuUsage):
        # MUST define these
        super(VirtualMachineFlagInfo, self).__init__()
    
        self.data['disableAcceleration'] = disableAcceleration
        self.data['diskUuidEnabled'] = diskUuidEnabled
        self.data['enableLogging'] = enableLogging
        self.data['htSharing'] = htSharing
        self.data['monitorType'] = monitorType
        self.data['recordReplayEnabled'] = recordReplayEnabled
        self.data['runWithDebugInfo'] = runWithDebugInfo
        self.data['snapshotDisabled'] = snapshotDisabled
        self.data['snapshotLocked'] = snapshotLocked
        self.data['snapshotPowerOffBehavior'] = snapshotPowerOffBehavior
        self.data['useToe'] = useToe
        self.data['virtualExecUsage'] = virtualExecUsage
        self.data['virtualMmuUsage'] = virtualMmuUsage
    
    
    @property
    def disableAcceleration(self):
        '''Flag to turn off video acceleration for a virtual machine console window.
        '''
        return self.data['disableAcceleration']

    @property
    def diskUuidEnabled(self):
        '''Indicates whether disk UUIDs are being used by this virtual machine. If this flag
        is set to false, disk UUIDs are not exposed to the guest.
        '''
        return self.data['diskUuidEnabled']

    @property
    def enableLogging(self):
        '''Flag to enable logging for a virtual machine.
        '''
        return self.data['enableLogging']

    @property
    def htSharing(self):
        '''Specifies how the VCPUs of a virtual machine are allowed to share physical cores
        on a hyperthreaded system. Two VCPUs are "sharing" a core if they are both
        running on logical CPUs of the core at the same time.
        '''
        return self.data['htSharing']

    @property
    def monitorType(self):
        '''Virtual machine monitor type. See VirtualMachineFlagInfoMonitorType for possible
        values for this property.
        '''
        return self.data['monitorType']

    @property
    def recordReplayEnabled(self):
        '''Flag to specify whether record and replay operations are allowed for this virtual
        machine. If this flag is set to 'true', instruction virtualization will
        use hardware virtualization (HV) support. I.e., virtualExecUsage will be
        set to 'hvOn'. If this flag is set to 'false' for a virtual machine that
        already has a recording, replay will be disallowed, though the recording
        will be preserved. If the value is unset, the behavior 'false' will be
        used.
        '''
        return self.data['recordReplayEnabled']

    @property
    def runWithDebugInfo(self):
        '''Flag to specify whether or not to run in debug mode.
        '''
        return self.data['runWithDebugInfo']

    @property
    def snapshotDisabled(self):
        '''Flag to specify whether snapshots are disabled for this virtual machine.
        '''
        return self.data['snapshotDisabled']

    @property
    def snapshotLocked(self):
        '''Flag to specify whether the snapshot tree is locked for this virtual machine.
        '''
        return self.data['snapshotLocked']

    @property
    def snapshotPowerOffBehavior(self):
        '''Specifies the power-off behavior for a virtual machine that has a snapshot. If the
        value is unset, the behavior 'powerOff' will be used.
        '''
        return self.data['snapshotPowerOffBehavior']

    @property
    def useToe(self):
        '''Flag to specify whether or not to use TOE (TCP/IP Offloading).
        '''
        return self.data['useToe']

    @property
    def virtualExecUsage(self):
        '''Indicates whether or not the system will try to use Hardware Virtualization (HV)
        support for instruction virtualization, if available.
        '''
        return self.data['virtualExecUsage']

    @property
    def virtualMmuUsage(self):
        '''Indicates whether or not the system will try to use nested page table hardware
        support, if available.
        '''
        return self.data['virtualMmuUsage']

