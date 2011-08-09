
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineConfigSpec(DynamicData):
    '''The ConfigSpec data object type encapsulates configuration settings when creating
        or reconfiguring a virtual machine. To support incremental changes, these
        properties are all optional.
    '''
    
    def __init__(self, alternateGuestName, annotation, bootOptions, changeTrackingEnabled, changeVersion, consolePreferences, cpuAffinity, cpuAllocation, cpuFeatureMask, cpuHotAddEnabled, cpuHotRemoveEnabled, deviceChange, extraConfig, files, flags, ftInfo, guestId, instanceUuid, locationId, memoryAffinity, memoryAllocation, memoryHotAddEnabled, memoryMB, name, networkShaper, npivDesiredNodeWwns, npivDesiredPortWwns, npivNodeWorldWideName, npivOnNonRdmDisks, npivPortWorldWideName, npivTemporaryDisabled, npivWorldWideNameOp, npivWorldWideNameType, numCPUs, powerOpInfo, swapPlacement, tools, uuid, vAppConfig, vAppConfigRemoved, vAssertsEnabled, version):
        # MUST define these
        super(VirtualMachineConfigSpec, self).__init__()
    
        self.data['alternateGuestName'] = alternateGuestName
        self.data['annotation'] = annotation
        self.data['bootOptions'] = bootOptions
        self.data['changeTrackingEnabled'] = changeTrackingEnabled
        self.data['changeVersion'] = changeVersion
        self.data['consolePreferences'] = consolePreferences
        self.data['cpuAffinity'] = cpuAffinity
        self.data['cpuAllocation'] = cpuAllocation
        self.data['cpuFeatureMask'] = cpuFeatureMask
        self.data['cpuHotAddEnabled'] = cpuHotAddEnabled
        self.data['cpuHotRemoveEnabled'] = cpuHotRemoveEnabled
        self.data['deviceChange'] = deviceChange
        self.data['extraConfig'] = extraConfig
        self.data['files'] = files
        self.data['flags'] = flags
        self.data['ftInfo'] = ftInfo
        self.data['guestId'] = guestId
        self.data['instanceUuid'] = instanceUuid
        self.data['locationId'] = locationId
        self.data['memoryAffinity'] = memoryAffinity
        self.data['memoryAllocation'] = memoryAllocation
        self.data['memoryHotAddEnabled'] = memoryHotAddEnabled
        self.data['memoryMB'] = memoryMB
        self.data['name'] = name
        self.data['networkShaper'] = networkShaper
        self.data['npivDesiredNodeWwns'] = npivDesiredNodeWwns
        self.data['npivDesiredPortWwns'] = npivDesiredPortWwns
        self.data['npivNodeWorldWideName'] = npivNodeWorldWideName
        self.data['npivOnNonRdmDisks'] = npivOnNonRdmDisks
        self.data['npivPortWorldWideName'] = npivPortWorldWideName
        self.data['npivTemporaryDisabled'] = npivTemporaryDisabled
        self.data['npivWorldWideNameOp'] = npivWorldWideNameOp
        self.data['npivWorldWideNameType'] = npivWorldWideNameType
        self.data['numCPUs'] = numCPUs
        self.data['powerOpInfo'] = powerOpInfo
        self.data['swapPlacement'] = swapPlacement
        self.data['tools'] = tools
        self.data['uuid'] = uuid
        self.data['vAppConfig'] = vAppConfig
        self.data['vAppConfigRemoved'] = vAppConfigRemoved
        self.data['vAssertsEnabled'] = vAssertsEnabled
        self.data['version'] = version
    
    
    @property
    def alternateGuestName(self):
        '''Full name for guest, if guestId is specified as
        '''
        return self.data['alternateGuestName']

    @property
    def annotation(self):
        '''User-provided description of the virtual machine. Because this property is
        optional in the virtual machine configuration, it is necessary to pass an
        explicit empty string in a ConfigSpec object to remove an annotation that
        is already present in the VirtualMachineConfigInfo for a virtual machine.
        '''
        return self.data['annotation']

    @property
    def bootOptions(self):
        '''Settings that control the boot behavior of the virtual machine. These settings
        take effect during the next power-on of the virtual machine.
        '''
        return self.data['bootOptions']

    @property
    def changeTrackingEnabled(self):
        '''Setting to control enabling/disabling changed block tracking for the virtual disks
        of this VM. This may only be set if the changeTrackingSupported capability
        is true for this virtual machine. Any change to this property will take
        effect the next time the virtual machine powers on, resumes from a
        suspended state, performs a snapshot create/delete/revert operation or
        migrates while powered on.
        '''
        return self.data['changeTrackingEnabled']

    @property
    def changeVersion(self):
        '''If specified, the changes are only applied if the current changeVersion matches
        the specified changeVersion. This field can be used to guard against
        updates that have happened between when configInfo is read and when it is
        applied.
        '''
        return self.data['changeVersion']

    @property
    def consolePreferences(self):
        '''Legacy console viewer preferences that are used with power operations. For
        example, power on.
        '''
        return self.data['consolePreferences']

    @property
    def cpuAffinity(self):
        '''Affinity settings for CPU.
        '''
        return self.data['cpuAffinity']

    @property
    def cpuAllocation(self):
        '''Resource limits for CPU.
        '''
        return self.data['cpuAllocation']

    @property
    def cpuFeatureMask(self):
        '''Specifies the CPU feature compatibility masks.
        '''
        return self.data['cpuFeatureMask']

    @property
    def cpuHotAddEnabled(self):
        '''Indicates whether or not virtual processors can be added to the virtual machine
        while it is running. This attribute can only be set when the virtual
        machine is powered-off.
        '''
        return self.data['cpuHotAddEnabled']

    @property
    def cpuHotRemoveEnabled(self):
        '''Indicates whether or not virtual processors can be removed from the virtual
        machine while it is running. This attribute can only be set when the
        virtual machine is powered-off.
        '''
        return self.data['cpuHotRemoveEnabled']

    @property
    def deviceChange(self):
        '''Set of virtual devices being modified by the configuration operation.
        '''
        return self.data['deviceChange']

    @property
    def extraConfig(self):
        '''Additional configuration information for the virtual machine. This describes a set
        of modifications to the additional options. An option is removed if the
        key is present but the value is not set or the value is an empty string.
        Otherwise, the key is set to the new value.
        '''
        return self.data['extraConfig']

    @property
    def files(self):
        '''Information about virtual machine files.
        '''
        return self.data['files']

    @property
    def flags(self):
        '''Additional flags for a virtual machine.
        '''
        return self.data['flags']

    @property
    def ftInfo(self):
        '''Fault Tolerance settings for this virtual machine.
        '''
        return self.data['ftInfo']

    @property
    def guestId(self):
        '''Short guest operating system identifier.
        '''
        return self.data['guestId']

    @property
    def instanceUuid(self):
        '''VirtualCenter-specific 128-bit UUID of a virtual machine, represented as a
        hexadecimal string. This identifier is used by VirtalCenter to uniquely
        identify all virtual machine instances in the Virtual Infrastructure
        environment, including those that may share the same SMBIOS UUID.
        '''
        return self.data['instanceUuid']

    @property
    def locationId(self):
        '''128-bit hash based on the virtual machine's configuration file location and the
        UUID of the host assigned to run the virtual machine.
        '''
        return self.data['locationId']

    @property
    def memoryAffinity(self):
        '''Affinity settings for memory.
        '''
        return self.data['memoryAffinity']

    @property
    def memoryAllocation(self):
        '''Resource limits for memory.
        '''
        return self.data['memoryAllocation']

    @property
    def memoryHotAddEnabled(self):
        '''Indicates whether or not memory can be added to the virtual machine while it is
        running. This attribute can only be set when the virtual machine is
        powered-off.
        '''
        return self.data['memoryHotAddEnabled']

    @property
    def memoryMB(self):
        '''Size of a virtual machine's memory, in MB.
        '''
        return self.data['memoryMB']

    @property
    def name(self):
        '''Display name of the virtual machine.
        '''
        return self.data['name']

    @property
    def networkShaper(self):
        '''Resource limits for network.
        '''
        return self.data['networkShaper']

    @property
    def npivDesiredNodeWwns(self):
        '''The NPIV node WWNs to be extended from the original list of WWN nummbers. This
        property should be set to desired number which is an aggregate of existing
        plus new numbers. Desired Node WWNs should always be greater than the
        existing number of node WWNs
        '''
        return self.data['npivDesiredNodeWwns']

    @property
    def npivDesiredPortWwns(self):
        '''The NPIV port WWNs to be extended from the original list of WWN nummbers. This
        property should be set to desired number which is an aggregate of existing
        plus new numbers. Desired Node WWNs should always be greater than the
        existing number of port WWNs
        '''
        return self.data['npivDesiredPortWwns']

    @property
    def npivNodeWorldWideName(self):
        '''The NPIV node WWN to be assigned to a virtual machine. This property should only
        be used or set when the value of npivWorldWideNameOp property is "set".
        Otherwise, an InvalidVmConfig fault will be thrown. If the specified node
        WWN is currently being used by another virtual machine, a VmWwnConflict
        fault will be thrown.
        '''
        return self.data['npivNodeWorldWideName']

    @property
    def npivOnNonRdmDisks(self):
        '''This property is used to check whether the NPIV can be enabled on the Virtual
        machine with non-rdm disks in the configuration, so this is potentially
        not enabling npiv on vmfs disks. Also this property is used to check
        whether RDM is required to generate WWNs for a virtual machine.
        '''
        return self.data['npivOnNonRdmDisks']

    @property
    def npivPortWorldWideName(self):
        '''The NPIV port WWN to be assigned to a virtual machine. This property should only
        be used or set when the value of npivWorldWideNameOp property is "set".
        Otherwise, an InvalidVmConfig fault will be thrown. If the specified port
        WWN is currently being used by another virtual machine, a VmWwnConflict
        fault will be thrown.
        '''
        return self.data['npivPortWorldWideName']

    @property
    def npivTemporaryDisabled(self):
        '''This property is used to enable or disable the NPIV capability on a desired
        virtual machine on a temporary basis. When this property is set NPIV Vport
        will not be instantiated by the VMX process of the Virtual Machine. When
        this property is set port WWNs and node WWNs in the VM configuration are
        preserved.
        '''
        return self.data['npivTemporaryDisabled']

    @property
    def npivWorldWideNameOp(self):
        '''The flag to indicate what type of NPIV WWN operation is going to be performed on
        the virtual machine. If unset, it indicates no change to existing NPIV WWN
        assignment (or not assigned) in the virtual machine.
        '''
        return self.data['npivWorldWideNameOp']

    @property
    def npivWorldWideNameType(self):
        '''This property is used internally in the communication between the VirtualCenter
        server and ESX Server to indicate the source for npivNodeWorldWideName and
        npivPortWorldWideName when npivWorldWideNameOp is "set". This property
        should only be set by the VirtualCenter server.
        '''
        return self.data['npivWorldWideNameType']

    @property
    def numCPUs(self):
        '''Number of virtual processors in a virtual machine.
        '''
        return self.data['numCPUs']

    @property
    def powerOpInfo(self):
        '''Configuration for default power operations.
        '''
        return self.data['powerOpInfo']

    @property
    def swapPlacement(self):
        '''Virtual machine swapfile placement policy. This may only be set if the
        swapPlacementSupported capability is true for this virtual machine. Any
        change to this policy will take effect the next time the virtual machine
        powers on, resumes from a suspended state, or migrates while powered on.
        '''
        return self.data['swapPlacement']

    @property
    def tools(self):
        '''Configuration of VMware Tools running in the guest operating system.
        '''
        return self.data['tools']

    @property
    def uuid(self):
        '''128-bit SMBIOS UUID of a virtual machine represented as a hexadecimal string in
        "12345678-abcd-1234-cdef-123456789abc" format.
        '''
        return self.data['uuid']

    @property
    def vAppConfig(self):
        '''Configuration of vApp meta-data for a virtual machine
        '''
        return self.data['vAppConfig']

    @property
    def vAppConfigRemoved(self):
        '''Set to true, if the vApp configuration should be removed
        '''
        return self.data['vAppConfigRemoved']

    @property
    def vAssertsEnabled(self):
        '''Indicates whether user-configured virtual asserts will be triggered during virtual
        machine replay. This setting takes effect during the next replay of the
        virtual machine.
        '''
        return self.data['vAssertsEnabled']

    @property
    def version(self):
        '''The version string for this virtual machine. This is used only while creating a
        new virtual machine, and can be updated by invoking UpgradeVM_Task for
        this virtual machine.
        '''
        return self.data['version']

