
from pyvisdk.do.authorization_event import AuthorizationEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class PermissionEvent(AuthorizationEvent):
    '''This event records a permission operation.
    '''
    
    def __init__(self, entity, group, principal):
        # MUST define these
        super(PermissionEvent, self).__init__()
    
        self.data['entity'] = entity
        self.data['group'] = group
        self.data['principal'] = principal
    
    
    @property
    def entity(self):
        '''The entity to which the permission applied.
        '''
        return self.data['entity']

    @property
    def group(self):
        '''Whether or not the principal was a group.
        '''
        return self.data['group']

    @property
    def principal(self):
        '''The user name or group to which the permission was granted.
        '''
        return self.data['principal']

