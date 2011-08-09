
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class Permission(DynamicData):
    '''This data object type provides assignment of some role access to a principal on a
        specific entity. A ManagedEntity is limited to one permission per
        principal.
    '''
    
    def __init__(self, entity, group, principal, propagate, roleId):
        # MUST define these
        super(Permission, self).__init__()
    
        self.data['entity'] = entity
        self.data['group'] = group
        self.data['principal'] = principal
        self.data['propagate'] = propagate
        self.data['roleId'] = roleId
    
    
    @property
    def entity(self):
        '''Managed entity the permission is defined on. Left unset when calling
        setPermissions or resetPermissions, but present for the results of
        permission queries.
        '''
        return self.data['entity']

    @property
    def group(self):
        '''Whether principal refers to a user or a group. True for a group and false for a
        user.
        '''
        return self.data['group']

    @property
    def principal(self):
        '''User or group receiving access in the form of "login" for local or "DOMAIN\login"
        for users in a Windows domain.
        '''
        return self.data['principal']

    @property
    def propagate(self):
        '''Whether or not this permission propagates down the hierarchy to sub-entities.
        '''
        return self.data['propagate']

    @property
    def roleId(self):
        '''Reference to the role providing the access.
        '''
        return self.data['roleId']

