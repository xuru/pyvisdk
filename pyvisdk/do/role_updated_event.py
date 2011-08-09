
from pyvisdk.do.role_event import RoleEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class RoleUpdatedEvent(RoleEvent):
    '''This event records the creation of a role.
    '''
    
    def __init__(self, privilegeList):
        # MUST define these
        super(RoleUpdatedEvent, self).__init__()
    
        self.data['privilegeList'] = privilegeList
    
    
    @property
    def privilegeList(self):
        '''The privileges granted to the role.
        '''
        return self.data['privilegeList']

