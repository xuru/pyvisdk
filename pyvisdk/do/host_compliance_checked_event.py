
from pyvisdk.do.host_event import HostEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostComplianceCheckedEvent(HostEvent):
    '''This event records that a compliance check was triggered on the host.
    '''
    
    def __init__(self, profile):
        # MUST define these
        super(HostComplianceCheckedEvent, self).__init__()
    
        self.data['profile'] = profile
    
    
    @property
    def profile(self):
        '''
        '''
        return self.data['profile']

