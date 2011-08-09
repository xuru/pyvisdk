
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class AuthorizationRole(DynamicData):
    '''This data object type specifies a collection of privileges used to grant access to
        users on managed entities.
    '''
    
    def __init__(self, info, name, privilege, roleId, system):
        # MUST define these
        super(AuthorizationRole, self).__init__()
    
        self.data['info'] = info
        self.data['name'] = name
        self.data['privilege'] = privilege
        self.data['roleId'] = roleId
        self.data['system'] = system
    
    
    @property
    def info(self):
        '''Displayable role information.
        '''
        return self.data['info']

    @property
    def name(self):
        '''System-defined or user-defined role name.
        '''
        return self.data['name']

    @property
    def privilege(self):
        '''Privileges provided by this role, by privilege identifier.
        '''
        return self.data['privilege']

    @property
    def roleId(self):
        '''Unique role identifier.
        '''
        return self.data['roleId']

    @property
    def system(self):
        '''Whether or not the role is system-defined. System-defined roles cannot be changed.
        '''
        return self.data['system']

