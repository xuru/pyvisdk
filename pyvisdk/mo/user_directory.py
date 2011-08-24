
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class UserDirectory(BaseEntity):
    '''The UserDirectory managed object provides information about users and groups on
    a vSphere server and ESX hosts. The method RetrieveUserGroups returns a list of
    user account data. The method can perform a search operation based on specific
    criteria - user name, group name, sub-string or string matching, and, on
    Windows, domain. Use the results as input to the AuthorizationManager methods
    SetEntityPermissions and ResetEntityPermissions.The content of the returned
    results depends on the server environment:'''
    
    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.UserDirectory):
        super(UserDirectory, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def domainList(self):
        '''List of Windows domains available for user searches. On ESX Server or Linux
    systems, this is an empty list.'''
        return self.update('domainList')
    
    