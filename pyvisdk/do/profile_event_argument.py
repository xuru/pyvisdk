
from pyvisdk.do.event_argument import EventArgument
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ProfileEventArgument(EventArgument):
    '''The event argument is a Profile object
    '''
    
    def __init__(self, name, profile):
        # MUST define these
        super(ProfileEventArgument, self).__init__()
    
        self.data['name'] = name
        self.data['profile'] = profile
    
    
    @property
    def name(self):
        '''
        '''
        return self.data['name']

    @property
    def profile(self):
        '''
        '''
        return self.data['profile']

