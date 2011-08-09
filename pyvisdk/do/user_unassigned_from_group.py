
from pyvisdk.do.host_event import HostEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class UserUnassignedFromGroup(HostEvent):
    '''This event records that a user account membership was removed from a group.
    '''
    
    def __init__(self, group, userLogin):
        # MUST define these
        super(UserUnassignedFromGroup, self).__init__()
    
        self.data['group'] = group
        self.data['userLogin'] = userLogin
    
    
    @property
    def group(self):
        '''
        '''
        return self.data['group']

    @property
    def userLogin(self):
        '''
        '''
        return self.data['userLogin']

