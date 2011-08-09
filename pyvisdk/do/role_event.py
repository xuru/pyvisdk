
from pyvisdk.do.authorization_event import AuthorizationEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class RoleEvent(AuthorizationEvent):
    '''This event records a role operation.
    '''
    
    def __init__(self, role):
        # MUST define these
        super(RoleEvent, self).__init__()
    
        self.data['role'] = role
    
    
    @property
    def role(self):
        '''The associated role.
        '''
        return self.data['role']

