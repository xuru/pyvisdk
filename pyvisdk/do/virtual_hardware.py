
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualHardware(DynamicData):
    '''The VirtualHardware data object type contains the complete configuration of the
        hardware in a virtual machine.
    '''
    
    def __init__(self, device, memoryMB, numCPU):
        # MUST define these
        super(VirtualHardware, self).__init__()
    
        self.data['device'] = device
        self.data['memoryMB'] = memoryMB
        self.data['numCPU'] = numCPU
    
    
    @property
    def device(self):
        '''The set of virtual devices belonging to the virtual machine. This list is
        unordered.
        '''
        return self.data['device']

    @property
    def memoryMB(self):
        '''Memory size, in MB.
        '''
        return self.data['memoryMB']

    @property
    def numCPU(self):
        '''Number of virtual CPUs present in this virtual machine.
        '''
        return self.data['numCPU']

