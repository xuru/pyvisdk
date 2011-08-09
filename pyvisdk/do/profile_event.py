
from pyvisdk.do.event import Event
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ProfileEvent(Event):
    '''This event records a Profile specific event.
    '''
    
    def __init__(self, profile):
        # MUST define these
        super(ProfileEvent, self).__init__()
    
        self.data['profile'] = profile
    
    
    @property
    def profile(self):
        '''Link to the profile to which this event applies
        '''
        return self.data['profile']

