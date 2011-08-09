
from pyvisdk.do.event_argument import EventArgument
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class RoleEventArgument(EventArgument):
    '''The event argument is a Role object.
    '''
    
    def __init__(self, name, roleId):
        # MUST define these
        super(RoleEventArgument, self).__init__()
    
        self.data['name'] = name
        self.data['roleId'] = roleId
    
    
    @property
    def name(self):
        '''The name of the role.
        '''
        return self.data['name']

    @property
    def roleId(self):
        '''The ID of the role.
        '''
        return self.data['roleId']

