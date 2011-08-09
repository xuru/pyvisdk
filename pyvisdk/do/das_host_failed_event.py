
from pyvisdk.do.cluster_event import ClusterEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DasHostFailedEvent(ClusterEvent):
    '''This event records when a host failure has been detected by HA.
    '''
    
    def __init__(self, failedHost):
        # MUST define these
        super(DasHostFailedEvent, self).__init__()
    
        self.data['failedHost'] = failedHost
    
    
    @property
    def failedHost(self):
        '''The host that failed.
        '''
        return self.data['failedHost']

