
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineSnapshotInfo(DynamicData):
    '''The SnapshotInfo data object type provides all the information about the hierarchy
        of snapshots in a virtual machine.
    '''
    
    def __init__(self, currentSnapshot, rootSnapshotList):
        # MUST define these
        super(VirtualMachineSnapshotInfo, self).__init__()
    
        self.data['currentSnapshot'] = currentSnapshot
        self.data['rootSnapshotList'] = rootSnapshotList
    
    
    @property
    def currentSnapshot(self):
        '''Current snapshot of the virtual machine
        '''
        return self.data['currentSnapshot']

    @property
    def rootSnapshotList(self):
        '''Data for the entire set of snapshots for one virtual machine.
        '''
        return self.data['rootSnapshotList']

