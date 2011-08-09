
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostHardwareInfo(DynamicData):
    '''The HardwareInfo data object type describes the hardware configuration of the
        host.
    '''
    
    def __init__(self, biosInfo, cpuFeature, cpuInfo, cpuPkg, cpuPowerManagementInfo, memorySize, numaInfo, pciDevice, systemInfo):
        # MUST define these
        super(HostHardwareInfo, self).__init__()
    
        self.data['biosInfo'] = biosInfo
        self.data['cpuFeature'] = cpuFeature
        self.data['cpuInfo'] = cpuInfo
        self.data['cpuPkg'] = cpuPkg
        self.data['cpuPowerManagementInfo'] = cpuPowerManagementInfo
        self.data['memorySize'] = memorySize
        self.data['numaInfo'] = numaInfo
        self.data['pciDevice'] = pciDevice
        self.data['systemInfo'] = systemInfo
    
    
    @property
    def biosInfo(self):
        '''Information about the system BIOS
        '''
        return self.data['biosInfo']

    @property
    def cpuFeature(self):
        '''CPU feature set that is supported by the hardware. This is the intersection of the
        feature sets supported by the individual CPU packages. This feature set is
        modified by the supportedCpuFeature array in the host capabilities to
        obtain the feature set supported by the virtualization platform.
        '''
        return self.data['cpuFeature']

    @property
    def cpuInfo(self):
        '''Overall CPU information.
        '''
        return self.data['cpuInfo']

    @property
    def cpuPkg(self):
        '''Information about each of the physical CPU packages on the host.
        '''
        return self.data['cpuPkg']

    @property
    def cpuPowerManagementInfo(self):
        '''vSphere API 4.0
        '''
        return self.data['cpuPowerManagementInfo']

    @property
    def memorySize(self):
        '''Total amount of physical memory on the host in bytes.
        '''
        return self.data['memorySize']

    @property
    def numaInfo(self):
        '''Information about the NUMA (non-uniform memory access).
        '''
        return self.data['numaInfo']

    @property
    def pciDevice(self):
        '''The list of Peripheral Component Interconnect (PCI) devices available on this
        host.
        '''
        return self.data['pciDevice']

    @property
    def systemInfo(self):
        '''Information about the system as a whole.
        '''
        return self.data['systemInfo']

