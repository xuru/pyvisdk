
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
    
    
    
    def RetrieveUserGroups(self, domain, searchStr, belongsToGroup, belongsToUser, exactMatch, findUsers, findGroups):
        '''Returns a list of UserSearchResult objects describing the users and groups
        defined for the server.You must hold the Authorization.ModifyPermissions
        privilege to invoke this method. If you hold the privilege on any
        ManagedEntity, you will have access to user and group information for the
        server.
        
        :param domain: Domain to be searched. If not set, then the method searches the local machine.
        
        :param searchStr: Case insensitive substring used to filter results; the search string is compared to the login and full name for users, and the name and description for groups. Leave this blank to match all users.
        
        :param belongsToGroup: If present, the returned list contains only users or groups that directly belong to the specified group. Users or groups that have indirect membership will not be included in the list.
        
        :param belongsToUser: If present, the returned list contains only groups that directly contain the specified user. Groups that indirectly contain the user will not be included in the list.
        
        :param exactMatch: Indicates the searchStr passed should match a user or group name exactly.
        
        :param findUsers: True, if users should be included in the result.
        
        :param findGroups: True, if groups should be included in the result.
        
        '''
        return self.delegate("RetrieveUserGroups")(domain, searchStr, belongsToGroup, belongsToUser, exactMatch, findUsers, findGroups)