
from pyvisdk.do.profile_event import ProfileEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ProfileReferenceHostChangedEvent(ProfileEvent):
    '''This event records that the reference host associated with this profile has
        changed
    '''
    
    def __init__(self, referenceHost):
        # MUST define these
        super(ProfileReferenceHostChangedEvent, self).__init__()
    
        self.data['referenceHost'] = referenceHost
    
    
    @property
    def referenceHost(self):
        '''The newly associated reference host with this profile
        '''
        return self.data['referenceHost']

