
from pyvisdk.do.virtual_machine_target_info import VirtualMachineTargetInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineDiskDeviceInfo(VirtualMachineTargetInfo):
    '''The DiskDeviceInfo class contains basic information about a specific disk hardware
        device.
    '''
    
    def __init__(self, capacity, vm):
        # MUST define these
        super(VirtualMachineDiskDeviceInfo, self).__init__()
    
        self.data['capacity'] = capacity
        self.data['vm'] = vm
    
    
    @property
    def capacity(self):
        '''Size of disk
        '''
        return self.data['capacity']

    @property
    def vm(self):
        '''List of known virtual machines using this physical disk as a backing
        '''
        return self.data['vm']

