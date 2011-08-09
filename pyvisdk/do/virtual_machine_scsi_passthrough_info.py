
from pyvisdk.do.virtual_machine_target_info import VirtualMachineTargetInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineScsiPassthroughInfo(VirtualMachineTargetInfo):
    '''Description of a generic SCSI device, including information about the device ID.
    '''
    
    def __init__(self, physicalUnitNumber, scsiClass, vendor):
        # MUST define these
        super(VirtualMachineScsiPassthroughInfo, self).__init__()
    
        self.data['physicalUnitNumber'] = physicalUnitNumber
        self.data['scsiClass'] = scsiClass
        self.data['vendor'] = vendor
    
    
    @property
    def physicalUnitNumber(self):
        '''Unit number of the generic device on the physical host.
        '''
        return self.data['physicalUnitNumber']

    @property
    def scsiClass(self):
        '''The class of the generic SCSI device.
        '''
        return self.data['scsiClass']

    @property
    def vendor(self):
        '''The vendor name.
        '''
        return self.data['vendor']

