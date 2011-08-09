
from pyvisdk.do.dvs_event import DvsEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DvsHostJoinedEvent(DvsEvent):
    '''A host joined the distributed virtual switch.
    '''
    
    def __init__(self, hostJoined):
        # MUST define these
        super(DvsHostJoinedEvent, self).__init__()
    
        self.data['hostJoined'] = hostJoined
    
    
    @property
    def hostJoined(self):
        '''The host that joined DVS.
        '''
        return self.data['hostJoined']

