
from pyvisdk.do.cluster_event import ClusterEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DasHostIsolatedEvent(ClusterEvent):
    '''This event records that a host has been isolated from the network in a HA cluster.
        Since an isolated host cannot be distinguished from a failed host except
        by the isolated host itself, this event is logged when the isolated host
        regains network connectivity.
    '''
    
    def __init__(self, isolatedHost):
        # MUST define these
        super(DasHostIsolatedEvent, self).__init__()
    
        self.data['isolatedHost'] = isolatedHost
    
    
    @property
    def isolatedHost(self):
        '''The host that was isolated.
        '''
        return self.data['isolatedHost']

