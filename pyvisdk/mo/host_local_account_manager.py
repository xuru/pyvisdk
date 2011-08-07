
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostLocalAccountManager(BaseEntity):
    '''This managed object type provides an interface through which local accounts on a
        host are managed. Note that this managed object applies only to
        applications that use a local account database on the host to provide
        authentication (ESX Server, for example). POSIX and win32 hosts may impose
        different restrictions on the password, ID, and description formats. POSIX
        host implementation may restrict the user or group name to be lower case
        letters and less than 16 characters in total. It may also disallow
        characters such as ";", "\n", and so on. In short, all the platform
        dependent rules and restrictions regarding naming of users/groups and
        password apply here. An InvalidArgument fault is thrown if any of these
        rules are not obeyed.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.HostLocalAccountManager):
        # MUST define these
        super(HostLocalAccountManager, self).__init__(core, name=name, ref=ref, type=type)
    
    

    def AssignUserToGroup(self, user):
        '''Assigns a user to a group.

        :param user: Specification of user being updated.

        '''
        
        return self.delegate("AssignUserToGroup")(user)
        

    def CreateGroup(self, user):
        '''Creates a local group account using the parameters defined in the
        HostLocalAccountManagerAccountSpecification data object type. For POSIX
        hosts, passing the HostLocalAccountManagerPosixAccountSpecification data
        object type allows you to control the group ID format of the group account
        being created.

        :param user: Specification of user being updated.

        '''
        
        return self.delegate("CreateGroup")(user)
        

    def CreateUser(self, user):
        '''Creates a local user account using the parameters defined in the
        HostLocalAccountManagerAccountSpecification data object type. For POSIX
        hosts, passing HostLocalAccountManagerPosixAccountSpecification data
        object type allows you to control the format of the user ID of the user
        account being created.

        :param user: Specification of user being updated.

        '''
        
        return self.delegate("CreateUser")(user)
        

    def RemoveGroup(self, user):
        '''Removes a local group account.

        :param user: Specification of user being updated.

        '''
        
        return self.delegate("RemoveGroup")(user)
        

    def RemoveUser(self, user):
        '''Removes a local user account.

        :param user: Specification of user being updated.

        '''
        
        return self.delegate("RemoveUser")(user)
        

    def UnassignUserFromGroup(self, user):
        '''Unassigns a user from a group.

        :param user: Specification of user being updated.

        '''
        
        return self.delegate("UnassignUserFromGroup")(user)
        

    def UpdateUser(self, user):
        '''Updates a local user account using the parameters defined in the
        HostLocalAccountManagerAccountSpecification data object type.

        :param user: Specification of user being updated.

        '''
        
        return self.delegate("UpdateUser")(user)
        
