
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterDasAdvancedRuntimeInfo(DynamicData):
    '''Base class for advanced runtime information related to the high availability
        service for a cluster.
    '''
    
    def __init__(self, dasHostInfo):
        # MUST define these
        super(ClusterDasAdvancedRuntimeInfo, self).__init__()
    
        self.data['dasHostInfo'] = dasHostInfo
    
    
    @property
    def dasHostInfo(self):
        '''The information pertaining to the HA agents on the hosts
        '''
        return self.data['dasHostInfo']

