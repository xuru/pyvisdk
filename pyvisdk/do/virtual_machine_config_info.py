
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineConfigInfo(DynamicData):
    '''The ConfigInfo data object type encapsulates the configuration settings and
        virtual hardware for a virtual machine. This type holds all the
        information that is present in the .vmx configuration file for the virtual
        machine.
    '''
    
    def __init__(self, alternateGuestName, annotation, bootOptions, changeTrackingEnabled, changeVersion, consolePreferences, cpuAffinity, cpuAllocation, cpuFeatureMask, cpuHotAddEnabled, cpuHotRemoveEnabled, datastoreUrl, defaultPowerOps, extraConfig, files, flags, ftInfo, guestFullName, guestId, hardware, hotPlugMemoryIncrementSize, hotPlugMemoryLimit, instanceUuid, locationId, memoryAffinity, memoryAllocation, memoryHotAddEnabled, modified, name, networkShaper, npivDesiredNodeWwns, npivDesiredPortWwns, npivNodeWorldWideName, npivOnNonRdmDisks, npivPortWorldWideName, npivTemporaryDisabled, npivWorldWideNameType, swapPlacement, template, tools, uuid, vAppConfig, vAssertsEnabled, version):
        # MUST define these
        super(VirtualMachineConfigInfo, self).__init__()
    
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
        self.data['datastoreUrl'] = datastoreUrl
        self.data['defaultPowerOps'] = defaultPowerOps
        self.data['extraConfig'] = extraConfig
        self.data['files'] = files
        self.data['flags'] = flags
        self.data['ftInfo'] = ftInfo
        self.data['guestFullName'] = guestFullName
        self.data['guestId'] = guestId
        self.data['hardware'] = hardware
        self.data['hotPlugMemoryIncrementSize'] = hotPlugMemoryIncrementSize
        self.data['hotPlugMemoryLimit'] = hotPlugMemoryLimit
        self.data['instanceUuid'] = instanceUuid
        self.data['locationId'] = locationId
        self.data['memoryAffinity'] = memoryAffinity
        self.data['memoryAllocation'] = memoryAllocation
        self.data['memoryHotAddEnabled'] = memoryHotAddEnabled
        self.data['modified'] = modified
        self.data['name'] = name
        self.data['networkShaper'] = networkShaper
        self.data['npivDesiredNodeWwns'] = npivDesiredNodeWwns
        self.data['npivDesiredPortWwns'] = npivDesiredPortWwns
        self.data['npivNodeWorldWideName'] = npivNodeWorldWideName
        self.data['npivOnNonRdmDisks'] = npivOnNonRdmDisks
        self.data['npivPortWorldWideName'] = npivPortWorldWideName
        self.data['npivTemporaryDisabled'] = npivTemporaryDisabled
        self.data['npivWorldWideNameType'] = npivWorldWideNameType
        self.data['swapPlacement'] = swapPlacement
        self.data['template'] = template
        self.data['tools'] = tools
        self.data['uuid'] = uuid
        self.data['vAppConfig'] = vAppConfig
        self.data['vAssertsEnabled'] = vAssertsEnabled
        self.data['version'] = version
    
    
    @property
    def alternateGuestName(self):
        '''Used as display name for the operating system if guestId is
        '''
        return self.data['alternateGuestName']

    @property
    def annotation(self):
        '''Description for the virtual machine.
        '''
        return self.data['annotation']

    @property
    def bootOptions(self):
        '''Configuration options for the boot behavior of the virtual machine.
        '''
        return self.data['bootOptions']

    @property
    def changeTrackingEnabled(self):
        '''Indicates whether changed block tracking for this VM's disks is active.
        '''
        return self.data['changeTrackingEnabled']

    @property
    def changeVersion(self):
        '''The changeVersion is a unique identifier for a given version of the configuration.
        Each change to the configuration updates this value. This is typically
        implemented as an ever increasing count or a time-stamp. However, a client
        should always treat this as an opaque string.
        '''
        return self.data['changeVersion']

    @property
    def consolePreferences(self):
        '''Legacy console viewer preferences when doing power operations.
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
        '''Specifies CPU feature compatibility masks that override the defaults from the
        GuestOsDescriptor of the virtual machine's guest OS.
        '''
        return self.data['cpuFeatureMask']

    @property
    def cpuHotAddEnabled(self):
        '''Whether virtual processors can be added while this virtual machine is running.
        '''
        return self.data['cpuHotAddEnabled']

    @property
    def cpuHotRemoveEnabled(self):
        '''Whether virtual processors can be removed while this virtual machine is running.
        '''
        return self.data['cpuHotRemoveEnabled']

    @property
    def datastoreUrl(self):
        '''Enumerates the set of datastores that this virtual machine is stored on, as well
        as the URL identification for each of these.
        '''
        return self.data['datastoreUrl']

    @property
    def defaultPowerOps(self):
        '''Configuration of default power operations.
        '''
        return self.data['defaultPowerOps']

    @property
    def extraConfig(self):
        '''Additional configuration information for the virtual machine.
        '''
        return self.data['extraConfig']

    @property
    def files(self):
        '''Information about the files associated with a virtual machine. This information
        does not include files for specific virtual disks or snapshots.
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
    def guestFullName(self):
        '''This is the full name of the guest operating system for the virtual machine. For
        example: Windows 2000 Professional.
        '''
        return self.data['guestFullName']

    @property
    def guestId(self):
        '''Guest operating system configured on a virtual machine. This is a guest identifier
        that can be used to access the GuestOsDescriptor list for information
        about default configuration. For more information on possible values, see
        VirtualMachineGuestOsIdentifier.
        '''
        return self.data['guestId']

    @property
    def hardware(self):
        '''Processor, memory, and virtual devices for a virtual machine.
        '''
        return self.data['hardware']

    @property
    def hotPlugMemoryIncrementSize(self):
        '''Memory, in MB that can be added to a running virtual machine must be in increments
        of this value and needs be a multiple of this value. This value is
        determined by the virtual machine and is specified only if
        memoryHotAddEnabled has been set to true.
        '''
        return self.data['hotPlugMemoryIncrementSize']

    @property
    def hotPlugMemoryLimit(self):
        '''The maximum amount of memory, in MB, than can be added to a running virtual
        machine. This value is determined by the virtual machine and is specified
        only if memoryHotAddEnabled is set to true.
        '''
        return self.data['hotPlugMemoryLimit']

    @property
    def instanceUuid(self):
        '''VirtualCenter-specific 128-bit UUID of a virtual machine, represented as a
        hexademical string. This identifier is used by VirtualCenter to uniquely
        identify all virtual machine instances, including those that may share the
        same SMBIOS UUID.
        '''
        return self.data['instanceUuid']

    @property
    def locationId(self):
        '''Hash incorporating the virtual machine's config file location and the UUID of the
        host assigned to run the virtual machine.
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
        '''Whether memory can be added while this virtual machine is running.
        '''
        return self.data['memoryHotAddEnabled']

    @property
    def modified(self):
        '''Last time a virtual machine's configuration was modified.
        '''
        return self.data['modified']

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
        '''A 64-bit node WWN (World Wide Name). These WWNs are paired with the
        npivPortWorldWideName to be used by the NPIV VPORTs instantiated for the
        virtual machine on the physical HBAs of the host. A pair of node and port
        WWNs serves as a unique identifier in accessing a LUN, so that it can be
        monitored or controlled by the storage administrator.
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
        '''A 64-bit port WWN (World Wide Name). For detail description on WWN, see
        npivNodeWorldWideName.
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
    def npivWorldWideNameType(self):
        '''The source that provides/generates the assigned WWNs.
        '''
        return self.data['npivWorldWideNameType']

    @property
    def swapPlacement(self):
        '''Virtual machine swapfile placement policy. This will be unset if the virtual
        machine's swapPlacementSupported capability is false. If
        swapPlacementSupported is true, the default policy is "inherit".
        '''
        return self.data['swapPlacement']

    @property
    def template(self):
        '''Flag indicating whether or not a virtual machine is a template.
        '''
        return self.data['template']

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
        '''vApp meta-data for the virtual machine
        '''
        return self.data['vAppConfig']

    @property
    def vAssertsEnabled(self):
        '''Indicates whether user-configured virtual asserts will be triggered during virtual
        machine replay.
        '''
        return self.data['vAssertsEnabled']

    @property
    def version(self):
        '''The version string for this virtual machine.
        '''
        return self.data['version']

