
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostLocalAccountManager(BaseEntity):
    '''This managed object type provides an interface through which local accounts on
    a host are managed. Note that this managed object applies only to applications
    that use a local account database on the host to provide authentication (ESX
    Server, for example). POSIX and win32 hosts may impose different restrictions
    on the password, ID, and description formats. POSIX host implementation may
    restrict the user or group name to be lower case letters and less than 16
    characters in total. It may also disallow characters such as ";", "\n", and so
    on. In short, all the platform dependent rules and restrictions regarding
    naming of users/groups and password apply here. An InvalidArgument fault is
    thrown if any of these rules are not obeyed.'''
    
    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.HostLocalAccountManager):
        super(HostLocalAccountManager, self).__init__(core, name=name, ref=ref, type=type)
    
    
    
    
    
    def AssignUserToGroup(self):
        '''Assigns a user to a group.
        :rtype: None
        :returns: 
        '''
        return self.delegate("AssignUserToGroup")()
    
    def CreateGroup(self):
        '''Creates a local group account using the parameters defined in the
        HostLocalAccountManagerAccountSpecification data object type. For POSIX hosts,
        passing the HostLocalAccountManagerPosixAccountSpecification data object type
        allows you to control the group ID format of the group account being created.
        :rtype: None
        :returns: 
        '''
        return self.delegate("CreateGroup")()
    
    def CreateUser(self):
        '''Creates a local user account using the parameters defined in the
        HostLocalAccountManagerAccountSpecification data object type. For POSIX hosts,
        passing HostLocalAccountManagerPosixAccountSpecification data object type
        allows you to control the format of the user ID of the user account being
        created.
        :rtype: None
        :returns: 
        '''
        return self.delegate("CreateUser")()
    
    def RemoveGroup(self):
        '''Removes a local group account.
        :rtype: None
        :returns: 
        '''
        return self.delegate("RemoveGroup")()
    
    def RemoveUser(self):
        '''Removes a local user account.
        :rtype: None
        :returns: 
        '''
        return self.delegate("RemoveUser")()
    
    def UnassignUserFromGroup(self):
        '''Unassigns a user from a group.
        :rtype: None
        :returns: 
        '''
        return self.delegate("UnassignUserFromGroup")()
    
    def UpdateUser(self):
        '''Updates a local user account using the parameters defined in the
        HostLocalAccountManagerAccountSpecification data object type.
        :rtype: None
        :returns: 
        '''
        return self.delegate("UpdateUser")()