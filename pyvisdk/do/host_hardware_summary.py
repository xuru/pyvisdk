
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostHardwareSummary(DynamicData):
    '''This data object type summarizes hardware used by the host.
    '''
    
    def __init__(self, cpuMhz, cpuModel, memorySize, model, numCpuCores, numCpuPkgs, numCpuThreads, numHBAs, numNics, otherIdentifyingInfo, uuid, vendor):
        # MUST define these
        super(HostHardwareSummary, self).__init__()
    
        self.data['cpuMhz'] = cpuMhz
        self.data['cpuModel'] = cpuModel
        self.data['memorySize'] = memorySize
        self.data['model'] = model
        self.data['numCpuCores'] = numCpuCores
        self.data['numCpuPkgs'] = numCpuPkgs
        self.data['numCpuThreads'] = numCpuThreads
        self.data['numHBAs'] = numHBAs
        self.data['numNics'] = numNics
        self.data['otherIdentifyingInfo'] = otherIdentifyingInfo
        self.data['uuid'] = uuid
        self.data['vendor'] = vendor
    
    
    @property
    def cpuMhz(self):
        '''The speed of the CPU cores. This is an average value if there are multiple speeds.
        The product of cpuMhz and numCpuCores is approximately equal to the sum of
        the MHz for all the individual cores on the host.
        '''
        return self.data['cpuMhz']

    @property
    def cpuModel(self):
        '''The CPU model.
        '''
        return self.data['cpuModel']

    @property
    def memorySize(self):
        '''The physical memory size in bytes.
        '''
        return self.data['memorySize']

    @property
    def model(self):
        '''The system model identification.
        '''
        return self.data['model']

    @property
    def numCpuCores(self):
        '''Number of physical CPU cores on the host. Physical CPU cores are the processors
        contained by a CPU package.
        '''
        return self.data['numCpuCores']

    @property
    def numCpuPkgs(self):
        '''Number of physical CPU packages on the host. Physical CPU packages are chips that
        contain one or more processors. Processors contained by a package are also
        known as CPU cores. For example, one dual-core package is comprised of one
        chip that contains two CPU cores.
        '''
        return self.data['numCpuPkgs']

    @property
    def numCpuThreads(self):
        '''Number of physical CPU threads on the host.
        '''
        return self.data['numCpuThreads']

    @property
    def numHBAs(self):
        '''The number of host bus adapters (HBAs).
        '''
        return self.data['numHBAs']

    @property
    def numNics(self):
        '''The number of network adapters.
        '''
        return self.data['numNics']

    @property
    def otherIdentifyingInfo(self):
        '''Other identification information. This information may be vendor specific.
        '''
        return self.data['otherIdentifyingInfo']

    @property
    def uuid(self):
        '''The hardware BIOS identification.
        '''
        return self.data['uuid']

    @property
    def vendor(self):
        '''The hardware vendor identification.
        '''
        return self.data['vendor']

