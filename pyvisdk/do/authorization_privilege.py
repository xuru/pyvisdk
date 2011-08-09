
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class AuthorizationPrivilege(DynamicData):
    '''This data object type provides access to some aspect of the system. Privileges are
        generally independent. This means a user with a privilege usually can
        perform an associated set of actions without needing any additional
        supporting privileges.Within each product version, privileges do not
        change. See AuthorizationDescription for detailed information on the
        privileges defined by the system.
    '''
    
    def __init__(self, name, onParent, privGroupName, privId):
        # MUST define these
        super(AuthorizationPrivilege, self).__init__()
    
        self.data['name'] = name
        self.data['onParent'] = onParent
        self.data['privGroupName'] = privGroupName
        self.data['privId'] = privId
    
    
    @property
    def name(self):
        '''Privilege name.
        '''
        return self.data['name']

    @property
    def onParent(self):
        '''Determines whether or not the privilege is applied on the parent entity.
        '''
        return self.data['onParent']

    @property
    def privGroupName(self):
        '''Group name.
        '''
        return self.data['privGroupName']

    @property
    def privId(self):
        '''Unique identifier.
        '''
        return self.data['privId']

