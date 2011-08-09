
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualHardwareOption(DynamicData):
    '''The VirtualHardwareOption data object contains the options available for all
        virtual devices.
    '''
    
    def __init__(self, deviceListReadonly, hwVersion, licensingLimit, memoryMB, numCPU, numCpuReadonly, numIDEControllers, numPCIControllers, numPS2Controllers, numSIOControllers, numSupportedWwnNodes, numSupportedWwnPorts, numUSBControllers, resourceConfigOption, virtualDeviceOption):
        # MUST define these
        super(VirtualHardwareOption, self).__init__()
    
        self.data['deviceListReadonly'] = deviceListReadonly
        self.data['hwVersion'] = hwVersion
        self.data['licensingLimit'] = licensingLimit
        self.data['memoryMB'] = memoryMB
        self.data['numCPU'] = numCPU
        self.data['numCpuReadonly'] = numCpuReadonly
        self.data['numIDEControllers'] = numIDEControllers
        self.data['numPCIControllers'] = numPCIControllers
        self.data['numPS2Controllers'] = numPS2Controllers
        self.data['numSIOControllers'] = numSIOControllers
        self.data['numSupportedWwnNodes'] = numSupportedWwnNodes
        self.data['numSupportedWwnPorts'] = numSupportedWwnPorts
        self.data['numUSBControllers'] = numUSBControllers
        self.data['resourceConfigOption'] = resourceConfigOption
        self.data['virtualDeviceOption'] = virtualDeviceOption
    
    
    @property
    def deviceListReadonly(self):
        '''Whether the set of virtual devices can be changed, e.g., can devices be added or
        removed. This does not preclude changing devices.
        '''
        return self.data['deviceListReadonly']

    @property
    def hwVersion(self):
        '''The virtual hardware version.
        '''
        return self.data['hwVersion']

    @property
    def licensingLimit(self):
        '''List of propery names which limits are given be a licensing restriction of the
        underlying product, e.g., a limit that is not derived based on the product
        or hardware features. For example, the property name "numCPU"
        '''
        return self.data['licensingLimit']

    @property
    def memoryMB(self):
        '''The minimum, maximum, and default memory options, in MB, per virtual machine, for
        this VirtualHardwareOption. These values are typically overruled by the
        supported and recommended values specified in the GuestOsDescriptor class.
        '''
        return self.data['memoryMB']

    @property
    def numCPU(self):
        '''List of acceptable values for the number of CPUs supported by this ConfigOption.
        This is usually superceded by the information available in the guest
        operating system descriptors. The guest operating system descriptor
        describes a maximum CPU count, but the acceptable values are still
        constrained to the set specified here. The default value is stored at
        index 0 in the list.
        '''
        return self.data['numCPU']

    @property
    def numCpuReadonly(self):
        '''Can the number of virtual CPUs be changed
        '''
        return self.data['numCpuReadonly']

    @property
    def numIDEControllers(self):
        '''The minimum, maximum, and default number of IDE controllers for this virtual
        machine configuration. Note: SCSI controllers sit on the PCI controller so
        their options (minimum, maximum, and default values) are contained inside
        the VirtualPCIControllerOption class.
        '''
        return self.data['numIDEControllers']

    @property
    def numPCIControllers(self):
        '''The minimum, maximum, and default number of PCI controllers for this virtual
        machine configuration.
        '''
        return self.data['numPCIControllers']

    @property
    def numPS2Controllers(self):
        '''The minimum, maximum, and default number of PS2 controllers for this virtual
        machine configuration.
        '''
        return self.data['numPS2Controllers']

    @property
    def numSIOControllers(self):
        '''The minimum, maximum, and default number of SIO controllers for this virtual
        machine configuration.
        '''
        return self.data['numSIOControllers']

    @property
    def numSupportedWwnNodes(self):
        '''The minimum, maximum and default number of NPIV WorldWidePort names supported for
        this virtual machine configuration.
        '''
        return self.data['numSupportedWwnNodes']

    @property
    def numSupportedWwnPorts(self):
        '''The minimum, maximum and default number of NPIV WorldWideNode names supported for
        this virtual machine configuration.
        '''
        return self.data['numSupportedWwnPorts']

    @property
    def numUSBControllers(self):
        '''The minimum, maximum, and default number of USB controllers for this virtual
        machine configuration.
        '''
        return self.data['numUSBControllers']

    @property
    def resourceConfigOption(self):
        '''Default value and value range for ResourceConfigOption
        '''
        return self.data['resourceConfigOption']

    @property
    def virtualDeviceOption(self):
        '''Array of virtual device options valid for this virtual machine configuration. The
        list is unordered.
        '''
        return self.data['virtualDeviceOption']

