
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostFlagInfo(DynamicData):
    '''The FlagInfo data object type encapsulates the flag settings for a host. These
        properties are optional since the same structure is used to change the
        values during an edit or create operation.
    '''
    
    def __init__(self, backgroundSnapshotsEnabled):
        # MUST define these
        super(HostFlagInfo, self).__init__()
    
        self.data['backgroundSnapshotsEnabled'] = backgroundSnapshotsEnabled
    
    
    @property
    def backgroundSnapshotsEnabled(self):
        '''Flag to specify whether background snapshots are enabled.
        '''
        return self.data['backgroundSnapshotsEnabled']

