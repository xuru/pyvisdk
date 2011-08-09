
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineConfigOption(DynamicData):
    '''This configuration data object type contains information about the execution
        environment for a virtual machine. This includes information about which
        features are supported, such as:* Which guest operating systems are
        supported. * How devices are emulated. For example, that a CD-ROM drive
        can be emulated with a file or that a serial port can be emulated with a
        pipe.VirtualCenter can provide a broader environment than any single
        physical host. This is a departure from traditional virtualization
        approaches, which rely on the host system to define the environment for
        virtual machines. This data object describes environment capabilities and
        is used by VirtualCenter to choose hosts on which to run virtual machines.
    '''
    
    def __init__(self, capabilities, datastore, defaultDevice, description, guestOSDefaultIndex, guestOSDescriptor, hardwareOptions, supportedMonitorType, supportedOvfEnvironmentTransport, supportedOvfInstallTransport, version):
        # MUST define these
        super(VirtualMachineConfigOption, self).__init__()
    
        self.data['capabilities'] = capabilities
        self.data['datastore'] = datastore
        self.data['defaultDevice'] = defaultDevice
        self.data['description'] = description
        self.data['guestOSDefaultIndex'] = guestOSDefaultIndex
        self.data['guestOSDescriptor'] = guestOSDescriptor
        self.data['hardwareOptions'] = hardwareOptions
        self.data['supportedMonitorType'] = supportedMonitorType
        self.data['supportedOvfEnvironmentTransport'] = supportedOvfEnvironmentTransport
        self.data['supportedOvfInstallTransport'] = supportedOvfInstallTransport
        self.data['version'] = version
    
    
    @property
    def capabilities(self):
        '''Capabilities supported by a virtual machine.
        '''
        return self.data['capabilities']

    @property
    def datastore(self):
        '''The datastore options for this virtual machine.
        '''
        return self.data['datastore']

    @property
    def defaultDevice(self):
        '''The list of virtual devices that are created on a virtual machine by default.
        Clients should not create these devices.
        '''
        return self.data['defaultDevice']

    @property
    def description(self):
        '''A description string for this configOption.
        '''
        return self.data['description']

    @property
    def guestOSDefaultIndex(self):
        '''Index into guestOsDescriptor array denoting the default guest operating system.
        '''
        return self.data['guestOSDefaultIndex']

    @property
    def guestOSDescriptor(self):
        '''List of supported guest operating systems. The choice of guest operating system
        may limit the set of valid devices. For example, you cannot select Vmxnet
        with all guest operating systems.
        '''
        return self.data['guestOSDescriptor']

    @property
    def hardwareOptions(self):
        '''Processor, memory, and virtual device options for a virtual machine.
        '''
        return self.data['hardwareOptions']

    @property
    def supportedMonitorType(self):
        '''The monitor types supported by a host. The acceptable monitor types are enumerated
        by VirtualMachineFlagInfoMonitorType.
        '''
        return self.data['supportedMonitorType']

    @property
    def supportedOvfEnvironmentTransport(self):
        '''Specifies the supported property transports that are available for the OVF
        environment
        '''
        return self.data['supportedOvfEnvironmentTransport']

    @property
    def supportedOvfInstallTransport(self):
        '''Specifies the supported transports for the OVF installation phase.
        '''
        return self.data['supportedOvfInstallTransport']

    @property
    def version(self):
        '''The version corresponding to this configOption.
        '''
        return self.data['version']

