
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineMemoryReservationInfo(DynamicData):
    '''The VirtualMachineReservationInfo data object type describes the amount of memory
        that is being reserved for virtual machines on the host, and how
        additional memory may be acquired.
    '''
    
    def __init__(self, allocationPolicy, virtualMachineMax, virtualMachineMin, virtualMachineReserved):
        # MUST define these
        super(VirtualMachineMemoryReservationInfo, self).__init__()
    
        self.data['allocationPolicy'] = allocationPolicy
        self.data['virtualMachineMax'] = virtualMachineMax
        self.data['virtualMachineMin'] = virtualMachineMin
        self.data['virtualMachineReserved'] = virtualMachineReserved
    
    
    @property
    def allocationPolicy(self):
        '''Policy for allocating additional memory for virtual machines.
        '''
        return self.data['allocationPolicy']

    @property
    def virtualMachineMax(self):
        '''The maximum amount of memory reserved for all running virtual machines, in bytes.
        '''
        return self.data['virtualMachineMax']

    @property
    def virtualMachineMin(self):
        '''The minimum amount of memory reserved for all running virtual machines, in bytes.
        '''
        return self.data['virtualMachineMin']

    @property
    def virtualMachineReserved(self):
        '''The amount of memory reserved for all running virtual machines, in bytes.
        '''
        return self.data['virtualMachineReserved']

