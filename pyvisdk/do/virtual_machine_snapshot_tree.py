
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineSnapshotTree(DynamicData):
    '''SnapshotTree encapsulates all the read-only data produced by the snapshot.
    '''
    
    def __init__(self, backupManifest, childSnapshotList, createTime, description, id, name, quiesced, replaySupported, snapshot, state, vm):
        # MUST define these
        super(VirtualMachineSnapshotTree, self).__init__()
    
        self.data['backupManifest'] = backupManifest
        self.data['childSnapshotList'] = childSnapshotList
        self.data['createTime'] = createTime
        self.data['description'] = description
        self.data['id'] = id
        self.data['name'] = name
        self.data['quiesced'] = quiesced
        self.data['replaySupported'] = replaySupported
        self.data['snapshot'] = snapshot
        self.data['state'] = state
        self.data['vm'] = vm
    
    
    @property
    def backupManifest(self):
        '''The relative path from the snapshotDirectory pointing to the backup manifest.
        Available for certain quiesced snapshots only.
        '''
        return self.data['backupManifest']

    @property
    def childSnapshotList(self):
        '''The snapshot data for all snapshots for which this snapshot is the parent.
        '''
        return self.data['childSnapshotList']

    @property
    def createTime(self):
        '''The date and time the snapshot was taken.
        '''
        return self.data['createTime']

    @property
    def description(self):
        '''Description of the snapshot.
        '''
        return self.data['description']

    @property
    def id(self):
        '''The unique identifier that distinguishes this snapshot from other snapshots of the
        virtual machine.
        '''
        return self.data['id']

    @property
    def name(self):
        '''Name of the snapshot.
        '''
        return self.data['name']

    @property
    def quiesced(self):
        '''Flag to indicate whether or not the snapshot was created with the "quiesce"
        option, ensuring a consistent state of the file system.
        '''
        return self.data['quiesced']

    @property
    def replaySupported(self):
        '''Flag to indicate whether this snapshot is associated with a recording session on
        the virtual machine that can be replayed.
        '''
        return self.data['replaySupported']

    @property
    def snapshot(self):
        '''The managed object for this snapshot.
        '''
        return self.data['snapshot']

    @property
    def state(self):
        '''The power state of the virtual machine when this snapshot was taken.
        '''
        return self.data['state']

    @property
    def vm(self):
        '''The virtual machine for which the snapshot was taken.
        '''
        return self.data['vm']

