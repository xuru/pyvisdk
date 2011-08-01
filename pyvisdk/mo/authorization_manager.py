
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class AuthorizationManager(BaseEntity):
    '''This managed object provides operations to query and update roles and permissions.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.AuthorizationManager):
        # MUST define these
        super(AuthorizationManager, self).__init__(core, name=name, ref=ref, type=type)
    
    

    def AddAuthorizationRole(self, name):
        '''Adds a new role. This method will add a user-defined role with given list of
        privileges and three system-defined privileges, "System.Anonymous",
        "System.View", and "System.Read".

        :param name: Name of the new role.


        :rtype: xsd:int 

        '''
        
        return self.delegate("AddAuthorizationRole")(name)
        

    def MergePermissions(self, srcRoleId, dstRoleId):
        '''Reassigns all permissions of a role to another role.

        :param srcRoleId: The ID of the source role providing the permissions which are changing.

        :param dstRoleId: The ID of the destination role to which the permissions are reassigned.

        '''
        
        return self.delegate("MergePermissions")(srcRoleId,dstRoleId)
        

    def RemoveAuthorizationRole(self, roleId, failIfUsed):
        '''Removes a role.

        :param roleId: 

        :param failIfUsed: If true, prevents the role from being removed if any permissions are using it.

        '''
        
        return self.delegate("RemoveAuthorizationRole")(roleId,failIfUsed)
        

    def ResetEntityPermissions(self):
        '''Update the entire set of permissions defined on an entity. Any existing
        permissions on the entity are removed and replaced with the provided
        set.If a permission is specified multiple times for the same user or
        group, the last permission specified takes effect.The operation is
        transactional per permission and could partially fail. The updates are
        performed in the order of the permission array argument. The first failed
        update will abort the operation and throw the appropriate exception. When
        the operation aborts, any permissions that have not yet been removed are
        left in their original state.After updates are applied, original
        permissions that are not in the new set are removed. A failure to remove a
        permission, such as a violation of the minimum administrator permission
        rule, will abort the operation and could leave remaining original
        permissions still effective on the entity.This will fail with an
        InvalidArgument fault if called on: the direct child folders of a
        datacenter managed object, the root resource pool of a ComputeResource or
        ClusterComputeResource, or a HostSystem that is part of a ComputeResource
        (Stand-alone Host). These objects always have the same permissions as
        their parent.This will fail with an InvalidArgument fault if called on a
        fault-tolerance (FT) secondary VirtualMachine. Such a VirtualMachine
        always has the same permissions as its FT primary VirtualMachine.
        '''
        
        return self.delegate("ResetEntityPermissions")()
        

    def SetEntityPermissions(self):
        '''Defines one or more permission rules on an entity or updates rules if already
        present for the given user or group on the entity.If a permission is
        specified multiple times for the same user or group, then the last
        permission specified takes effect.The operation is applied transactionally
        per permission and is applied to the entity following the order of the
        elements in the permission array argument. This means that if a failure
        occurs, the method terminates at that point in the permission array with
        an exception, leaving at least one and as many as all permissions
        unapplied.This will fail with an InvalidArgument fault if called on: the
        direct child folders of a datacenter managed object, the root resource
        pool of a ComputeResource or ClusterComputeResource, or a HostSystem that
        is part of a ComputeResource (Stand-alone Host). These objects always have
        the same permissions as their parent.This will fail with an
        InvalidArgument fault if called on a fault-tolerance (FT) secondary
        VirtualMachine. Such a VirtualMachine always has the same permissions as
        its FT primary VirtualMachine.
        '''
        
        return self.delegate("SetEntityPermissions")()
        

    def UpdateAuthorizationRole(self, newName, roleId):
        '''Updates a role's name or privileges. If the new set of privileges are assigned to
        the role, the system-defined privileges, "System.Anonymous",
        "System.View", and "System.Read" will be assigned to the role too.

        :param newName: The new name for the role.

        :param roleId: The ID of the role that is updated.

        '''
        
        return self.delegate("UpdateAuthorizationRole")(newName,roleId)
        

    def RetrieveAllPermissions(self):
        '''Finds all permissions defined in the system. The result is restricted to the
        managed entities visible to the user making the call.

        :rtype: Permission[] 

        '''
        
        return self.delegate("RetrieveAllPermissions")()
        

    def RetrieveRolePermissions(self, roleId):
        '''Finds all the permissions that use a particular role. The result is restricted to
        managed entities that are visible to the user making the call.

        :param roleId: 


        :rtype: Permission[] 

        '''
        
        return self.delegate("RetrieveRolePermissions")(roleId)
        

    def RemoveEntityPermission(self, user, isGroup):
        '''Removes a permission rule from an entity.This will fail with an InvalidArgument
        fault if called on: the direct child folders of a datacenter managed
        object, the root resource pool of a ComputeResource or
        ClusterComputeResource, or a HostSystem that is part of a ComputeResource
        (Stand-alone Host). These objects always have the same permissions as
        their parent.This will fail with an InvalidArgument fault if called on a
        fault-tolerance (FT) secondary VirtualMachine. Such a VirtualMachine
        always has the same permissions as its FT primary VirtualMachine.

        :param user: User or group for which the permission is defined.

        :param isGroup: True, if user refers to a group name; false, for a user name.

        '''
        
        return self.delegate("RemoveEntityPermission")(user,isGroup)
        

    def RetrieveEntityPermissions(self, inherited):
        '''Gets permissions defined on or effective on a managed entity. This returns the
        actual permission objects defined in the system for all users and groups
        relative to the managed entity. The inherited flag specifies whether or
        not to include permissions defined by the parents of this entity that
        propagate to this entity.For complex entities, the entity reported as
        defining the permission may be either the parent or a child entity
        belonging to the complex entity.The purpose of this method is to discover
        permissions for administration purposes, not to determine the current
        permissions. The current user's permissions are found on the effectiveRole
        property of the user's ManagedEntity.

        :param inherited: Whether or not to include propagating permissions defined by parent entities.


        :rtype: Permission[] 

        '''
        
        return self.delegate("RetrieveEntityPermissions")(inherited)
        
