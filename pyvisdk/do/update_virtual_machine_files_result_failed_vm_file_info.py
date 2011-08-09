
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class UpdateVirtualMachineFilesResultFailedVmFileInfo(DynamicData):
    '''
    '''
    
    def __init__(self, fault, vmFile):
        # MUST define these
        super(UpdateVirtualMachineFilesResultFailedVmFileInfo, self).__init__()
    
        self.data['fault'] = fault
        self.data['vmFile'] = vmFile
    
    
    @property
    def fault(self):
        '''The reason why the update failed.
        '''
        return self.data['fault']

    @property
    def vmFile(self):
        '''The file path
        '''
        return self.data['vmFile']

