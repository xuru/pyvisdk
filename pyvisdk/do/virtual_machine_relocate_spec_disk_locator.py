
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineRelocateSpecDiskLocator(DynamicData):
    '''The DiskLocator data object type specifies a virtual disk device (by ID) and a
        datastore locator for the disk's storage.
    '''
    
    def __init__(self, datastore, diskId, diskMoveType):
        # MUST define these
        super(VirtualMachineRelocateSpecDiskLocator, self).__init__()
    
        self.data['datastore'] = datastore
        self.data['diskId'] = diskId
        self.data['diskMoveType'] = diskMoveType
    
    
    @property
    def datastore(self):
        '''Target datastore.
        '''
        return self.data['datastore']

    @property
    def diskId(self):
        '''Device ID of the virtual disk.
        '''
        return self.data['diskId']

    @property
    def diskMoveType(self):
        '''Manner in which to move the virtual disk to the target datastore. The set of
        possible values is described in VirtualMachineRelocateDiskMoveOptions.
        '''
        return self.data['diskMoveType']

