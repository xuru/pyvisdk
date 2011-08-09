
from pyvisdk.do.vm_starting_event import VmStartingEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmUnsupportedStartingEvent(VmStartingEvent):
    '''This event records when an unsupported guest is powering on.
    '''
    
    def __init__(self, guestId):
        # MUST define these
        super(VmUnsupportedStartingEvent, self).__init__()
    
        self.data['guestId'] = guestId
    
    
    @property
    def guestId(self):
        '''
        '''
        return self.data['guestId']

