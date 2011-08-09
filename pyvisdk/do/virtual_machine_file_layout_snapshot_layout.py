
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineFileLayoutSnapshotLayout(DynamicData):
    '''Enumerates the set of files that make up a snapshot or redo-point
    '''
    
    def __init__(self, key, snapshotFile):
        # MUST define these
        super(VirtualMachineFileLayoutSnapshotLayout, self).__init__()
    
        self.data['key'] = key
        self.data['snapshotFile'] = snapshotFile
    
    
    @property
    def key(self):
        '''Identification of the snapshot
        '''
        return self.data['key']

    @property
    def snapshotFile(self):
        '''A list of files that make up the snapshot state. These are relative paths from the
        snapshotDirectory. A slash is always used as a separator.
        '''
        return self.data['snapshotFile']

