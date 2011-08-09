
from pyvisdk.do.cluster_event import ClusterEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterStatusChangedEvent(ClusterEvent):
    '''This event records when a cluster's overall status changed.
    '''
    
    def __init__(self, newStatus, oldStatus):
        # MUST define these
        super(ClusterStatusChangedEvent, self).__init__()
    
        self.data['newStatus'] = newStatus
        self.data['oldStatus'] = oldStatus
    
    
    @property
    def newStatus(self):
        '''The new (status).
        '''
        return self.data['newStatus']

    @property
    def oldStatus(self):
        '''The old (status).
        '''
        return self.data['oldStatus']

