
from pyvisdk.do.host_event import HostEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class GhostDvsProxySwitchDetectedEvent(HostEvent):
    '''This event records when Virtual Center server found DVS proxy switches on the host
        that don't match any DVS defined in Virtual Center.
    '''
    
    def __init__(self, switchUuid):
        # MUST define these
        super(GhostDvsProxySwitchDetectedEvent, self).__init__()
    
        self.data['switchUuid'] = switchUuid
    
    
    @property
    def switchUuid(self):
        '''The list of ghost DVS proxy switch uuids that were found.
        '''
        return self.data['switchUuid']

