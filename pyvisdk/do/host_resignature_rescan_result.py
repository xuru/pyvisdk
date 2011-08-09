
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostResignatureRescanResult(DynamicData):
    '''When a user resignatures an UnresolvedVmfsVolume through DatastoreSystem API, we
        resignature and auto-mount on the other hosts which share the same
        underlying storage luns. As part of the operation, we rescan the specified
        list of hosts. This data object describes the return value of resignature
        APIs in DatastoreSystem.
    '''
    
    def __init__(self, rescan, result):
        # MUST define these
        super(HostResignatureRescanResult, self).__init__()
    
        self.data['rescan'] = rescan
        self.data['result'] = result
    
    
    @property
    def rescan(self):
        '''List of VMFS Rescan operation results
        '''
        return self.data['rescan']

    @property
    def result(self):
        '''When an UnresolvedVmfsVolume has been resignatured, we want to return the newly
        created VMFS Datastore.
        '''
        return self.data['result']

