
from pyvisdk.do.host_event import HostEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostProfileAppliedEvent(HostEvent):
    '''This event records that a Profile application was done on the host
    '''
    
    def __init__(self, profile):
        # MUST define these
        super(HostProfileAppliedEvent, self).__init__()
    
        self.data['profile'] = profile
    
    
    @property
    def profile(self):
        '''Link to the profile which was applied
        '''
        return self.data['profile']

