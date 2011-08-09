
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class AuthorizationDescription(DynamicData):
    '''Static strings for authorization.
    '''
    
    def __init__(self, privilege, privilegeGroup):
        # MUST define these
        super(AuthorizationDescription, self).__init__()
    
        self.data['privilege'] = privilege
        self.data['privilegeGroup'] = privilegeGroup
    
    
    @property
    def privilege(self):
        '''Description of the privilege.
        '''
        return self.data['privilege']

    @property
    def privilegeGroup(self):
        '''Description of a category of similar privileges, grouped together for convenience.
        '''
        return self.data['privilegeGroup']

