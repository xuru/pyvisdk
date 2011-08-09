
from pyvisdk.do.cluster_event import ClusterEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterComplianceCheckedEvent(ClusterEvent):
    '''This event records that a compliance check was triggered on the cluster.
    '''
    
    def __init__(self, profile):
        # MUST define these
        super(ClusterComplianceCheckedEvent, self).__init__()
    
        self.data['profile'] = profile
    
    
    @property
    def profile(self):
        '''
        '''
        return self.data['profile']

