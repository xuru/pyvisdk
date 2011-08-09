
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineFileLayoutExSnapshotLayout(DynamicData):
    '''Layout of a snapshot.
    '''
    
    def __init__(self, dataKey, disk, key):
        # MUST define these
        super(VirtualMachineFileLayoutExSnapshotLayout, self).__init__()
    
        self.data['dataKey'] = dataKey
        self.data['disk'] = disk
        self.data['key'] = key
    
    
    @property
    def dataKey(self):
        '''Key to the snapshot data file in file.
        '''
        return self.data['dataKey']

    @property
    def disk(self):
        '''Layout of each virtual disk of the virtual machine when the snapshot was taken.
        '''
        return self.data['disk']

    @property
    def key(self):
        '''Reference to the snapshot.
        '''
        return self.data['key']

