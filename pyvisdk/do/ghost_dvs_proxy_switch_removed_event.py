
from pyvisdk.do.host_event import HostEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class GhostDvsProxySwitchRemovedEvent(HostEvent):
    '''This event records when the ghost DVS proxy switches (a.k.a host proxy switches
        that don't match any DVS defined in Virtual Center) were removed on the
        host.
    '''
    
    def __init__(self, switchUuid):
        # MUST define these
        super(GhostDvsProxySwitchRemovedEvent, self).__init__()
    
        self.data['switchUuid'] = switchUuid
    
    
    @property
    def switchUuid(self):
        '''The list of ghost DVS proxy switch uuid that were removed.
        '''
        return self.data['switchUuid']

