
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineDatastoreVolumeOption(DynamicData):
    '''This data object type describes a file system volume option for this virtual
        machine.
    '''
    
    def __init__(self, fileSystemType, majorVersion):
        # MUST define these
        super(VirtualMachineDatastoreVolumeOption, self).__init__()
    
        self.data['fileSystemType'] = fileSystemType
        self.data['majorVersion'] = majorVersion
    
    
    @property
    def fileSystemType(self):
        '''The type name of the file system volume information object for this option.
        '''
        return self.data['fileSystemType']

    @property
    def majorVersion(self):
        '''The major version of the file system volume information for this option. If not
        specified, all versions of this file system are included in this option.
        Currently, this value is set only for VMFS volumes.
        '''
        return self.data['majorVersion']

