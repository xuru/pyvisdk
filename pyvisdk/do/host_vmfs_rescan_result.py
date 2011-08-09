
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostVmfsRescanResult(DynamicData):
    '''When a user resignatures an UnresolvedVmfsVolume through DatastoreSystem API, we
        resignature and auto-mount on the other hosts which share the same
        underlying storage luns. As part of the operation, we rescan host. This
        data object describes the outcome of rescan operation on a host
    '''
    
    def __init__(self, fault, host):
        # MUST define these
        super(HostVmfsRescanResult, self).__init__()
    
        self.data['fault'] = fault
        self.data['host'] = host
    
    
    @property
    def fault(self):
        ''''fault' would be set if the operation was not successful
        '''
        return self.data['fault']

    @property
    def host(self):
        '''Host name on which rescan was performed
        '''
        return self.data['host']

