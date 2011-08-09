
from pyvisdk.do.host_event import HostEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class UserPasswordChanged(HostEvent):
    '''This event records that a user password changed.
    '''
    
    def __init__(self, userLogin):
        # MUST define these
        super(UserPasswordChanged, self).__init__()
    
        self.data['userLogin'] = userLogin
    
    
    @property
    def userLogin(self):
        '''
        '''
        return self.data['userLogin']

