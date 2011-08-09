
from pyvisdk.do.cluster_event import ClusterEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterCreatedEvent(ClusterEvent):
    '''This event records when a cluster is created.
    '''
    
    def __init__(self, parent):
        # MUST define these
        super(ClusterCreatedEvent, self).__init__()
    
        self.data['parent'] = parent
    
    
    @property
    def parent(self):
        '''The folder where the cluster is created.
        '''
        return self.data['parent']

