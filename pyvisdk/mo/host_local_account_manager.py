
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostLocalAccountManager(BaseEntity):
    '''Methods
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.HostLocalAccountManager):
        # MUST define these
        super(HostLocalAccountManager, self).__init__(core, name=name, ref=ref, type=type)
    
    

    def AssignUserToGroup(self, user, group):
        '''Assigns a user to a group.

        :param user: User ID of the account whose group membership is being assigned.

        :param group: Destination group account to which the user is being assigned.

        '''
        
        return self.delegate("AssignUserToGroup")(user,group)
        

    def CreateGroup(self, group):
        '''Creates a local group account using the parameters defined in the
        HostLocalAccountManagerAccountSpecification data object type. For POSIX
        hosts, passing the HostLocalAccountManagerPosixAccountSpecification data
        object type allows you to control the group ID format of the group account
        being created.

        :param group: Specification of group being created.

        '''
        
        return self.delegate("CreateGroup")(group)
        

    def CreateUser(self, user):
        '''Creates a local user account using the parameters defined in the
        HostLocalAccountManagerAccountSpecification data object type. For POSIX
        hosts, passing HostLocalAccountManagerPosixAccountSpecification data
        object type allows you to control the format of the user ID of the user
        account being created.

        :param user: Specification of user being created.

        '''
        
        return self.delegate("CreateUser")(user)
        

    def RemoveGroup(self, groupName):
        '''Removes a local group account.

        :param groupName: Group ID of the group account being removed.

        '''
        
        return self.delegate("RemoveGroup")(groupName)
        

    def RemoveUser(self, userName):
        '''Removes a local user account.

        :param userName: User ID of the user account being removed.

        '''
        
        return self.delegate("RemoveUser")(userName)
        

    def UnassignUserFromGroup(self, user, group):
        '''Unassigns a user from a group.

        :param user: User being unassigned from group.

        :param group: Group from which the user is being removed.

        '''
        
        return self.delegate("UnassignUserFromGroup")(user,group)
        

    def UpdateUser(self, user):
        '''Updates a local user account using the parameters defined in the
        HostLocalAccountManagerAccountSpecification data object type.

        :param user: Specification of user being updated.

        '''
        
        return self.delegate("UpdateUser")(user)
        
