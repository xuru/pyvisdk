
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualDiskSpec(DynamicData):
    '''Specification used to create or clone a virtual disk
    '''
    
    def __init__(self, adapterType, diskType):
        # MUST define these
        super(VirtualDiskSpec, self).__init__()
    
        self.data['adapterType'] = adapterType
        self.data['diskType'] = diskType
    
    
    @property
    def adapterType(self):
        '''The type of the virtual disk adapter for the new virtual disk.
        '''
        return self.data['adapterType']

    @property
    def diskType(self):
        '''The type of the new virtual disk.
        '''
        return self.data['diskType']

