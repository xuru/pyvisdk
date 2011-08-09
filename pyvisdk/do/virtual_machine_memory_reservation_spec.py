
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineMemoryReservationSpec(DynamicData):
    '''The VirtualMachineReservationSpec data object specifies configurable parameters
        for virtual machine memory reservation.
    '''
    
    def __init__(self, allocationPolicy, virtualMachineReserved):
        # MUST define these
        super(VirtualMachineMemoryReservationSpec, self).__init__()
    
        self.data['allocationPolicy'] = allocationPolicy
        self.data['virtualMachineReserved'] = virtualMachineReserved
    
    
    @property
    def allocationPolicy(self):
        '''Policy for allocating additional memory for virtual machines.
        '''
        return self.data['allocationPolicy']

    @property
    def virtualMachineReserved(self):
        '''The amount of memory reserved for all running virtual machines, in bytes.
        '''
        return self.data['virtualMachineReserved']

