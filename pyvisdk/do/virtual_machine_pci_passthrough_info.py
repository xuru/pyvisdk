
from pyvisdk.do.virtual_machine_target_info import VirtualMachineTargetInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachinePciPassthroughInfo(VirtualMachineTargetInfo):
    '''Description of a generic PCI device that can be attached to a virtual machine.
    '''
    
    def __init__(self, pciDevice, systemId):
        # MUST define these
        super(VirtualMachinePciPassthroughInfo, self).__init__()
    
        self.data['pciDevice'] = pciDevice
        self.data['systemId'] = systemId
    
    
    @property
    def pciDevice(self):
        '''Details of the PCI device, including vendor, class and device identification
        information.
        '''
        return self.data['pciDevice']

    @property
    def systemId(self):
        '''The ID of the system the PCI device is attached to.
        '''
        return self.data['systemId']

