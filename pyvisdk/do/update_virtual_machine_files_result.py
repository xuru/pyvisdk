
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class UpdateVirtualMachineFilesResult(DynamicData):
    '''UpdateVirtualMachineFilesResult is the result returned to the
        UpdateVirtualMachineFiles_Task method.
    '''
    
    def __init__(self, failedVmFile):
        # MUST define these
        super(UpdateVirtualMachineFilesResult, self).__init__()
    
        self.data['failedVmFile'] = failedVmFile
    
    
    @property
    def failedVmFile(self):
        '''The list of virtual machines files the server has attempted to update but failed
        to update.
        '''
        return self.data['failedVmFile']

