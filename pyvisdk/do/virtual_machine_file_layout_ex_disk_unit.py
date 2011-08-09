
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineFileLayoutExDiskUnit(DynamicData):
    '''Information about a single unit of a virtual disk, such as the base-disk or a
        delta-disk.A disk-unit consists of at least one descriptor file, and zero
        or more extent files.Sometimes, a disk-unit is also referred to as a .
    '''
    
    def __init__(self, fileKey):
        # MUST define these
        super(VirtualMachineFileLayoutExDiskUnit, self).__init__()
    
        self.data['fileKey'] = fileKey
    
    
    @property
    def fileKey(self):
        '''Array of keys of the files that make up the disk unit. Values here correspond to
        property key in file.
        '''
        return self.data['fileKey']

