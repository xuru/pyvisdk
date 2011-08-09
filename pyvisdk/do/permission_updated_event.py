
from pyvisdk.do.permission_event import PermissionEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class PermissionUpdatedEvent(PermissionEvent):
    '''This event records the update of a permission.
    '''
    
    def __init__(self, propagate, role):
        # MUST define these
        super(PermissionUpdatedEvent, self).__init__()
    
        self.data['propagate'] = propagate
        self.data['role'] = role
    
    
    @property
    def propagate(self):
        '''Whether or not the permission applies to sub-entities.
        '''
        return self.data['propagate']

    @property
    def role(self):
        '''The associated role.
        '''
        return self.data['role']

