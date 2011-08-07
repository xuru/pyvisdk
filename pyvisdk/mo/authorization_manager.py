
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class AuthorizationManager(BaseEntity):
    '''This managed object provides operations to query and update roles and
        permissions.are the basic individual rights required to perform
        operations. They are statically defined and never change for a single
        version of a product. Examples of privileges are "Power on a virtual
        machine" or "Configure a host."are aggregations of privileges, used for
        convenience. For user-defined roles, the system-defined privileges,
        "System.Anonymous", "System.View", and "System.Read" are always
        present.are the actual access-control rules. A permission is defined on a
        ManagedEntity and specifies the user or group ("principal") to which the
        rule applies. The role specifies the privileges to apply, and the
        propagate flag specifies whether or not the rule applies to sub-objects of
        the managed entity.A ManagedEntity may have multiple permissions, but may
        have only one permission per user or group. If, when logging in, a user
        has both a user permission and a group permission (as a group member) for
        the same entity, then the user-specific permission takes precedent. If
        there is no user-specific permission, but two or more group permissions
        are present, and the user is a member of the groups, then the privileges
        are the union of the specified roles.Managed entities may be collected
        together into a "complex entity" for the purpose of applying permissions
        consistently. Complex entities may have a Datacenter, ComputeResource, or
        ClusterComputeResource as a parent, with other child managed objects as
        additional parts of the complex entity:* A Datacenter's child objects are
        the root virtual machine and host Folders. * A ComputeResource's child
        objects are the root ResourcePool and HostSystem. * A
        ClusterComputeResource has only the root ResourcePool as a child
        object.Child objects in a complex entity are forced to inherit permissions
        from the parent object. When query operations are used to discover
        permissions on child objects of complex entities, different results may be
        returned for the owner of the permission. In some cases, the child object
        of the complex entity is returned as the object that defines the
        permission, and in other cases, the parent from which the permission is
        propagated is returned as the object that defines the permission. In both
        cases, the information about the owner of the permission is correct, since
        the entities within a complex entity are considered equivalent.
        Permissions defined on complex entities are always applicable on the child
        entities, regardless of the propagation flag, but may only be defined or
        modified on the parent object.In a group of fault-tolerance (FT) protected
        VirtualMachines, the secondary VirtualMachines are forced to inherit
        permissions from the primary VirtualMachine. Queries to discover
        permissions on FT secondary VMs always return the primary VM as the object
        that defines the permissions. Permissions defined on an FT primary VM are
        always applicable on its secondary VMs, but can only be defined or
        modified on the primary VM.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.AuthorizationManager):
        # MUST define these
        super(AuthorizationManager, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def description(self):
        '''Static, descriptive strings for system roles and privileges.
        '''
        return self.update('description')

    @property
    def privilegeList(self):
        '''The list of system-defined privileges.
        '''
        return self.update('privilegeList')

    @property
    def roleList(self):
        '''The currently defined roles in the system, including static system-defined roles.
        '''
        return self.update('roleList')


    def AddAuthorizationRole(self, roleId, newName, privIds):
        '''Adds a new role. This method will add a user-defined role with given list of
        privileges and three system-defined privileges, "System.Anonymous",
        "System.View", and "System.Read".

        :param roleId: The ID of the role that is updated.

        :param newName: The new name for the role.

        :param privIds: The new set of privileges to assign to the role.

        '''
        
        return self.delegate("AddAuthorizationRole")(roleId,newName,privIds)
        

    def MergePermissions(self, roleId, newName, privIds):
        '''Reassigns all permissions of a role to another role.

        :param roleId: The ID of the role that is updated.

        :param newName: The new name for the role.

        :param privIds: The new set of privileges to assign to the role.

        '''
        
        return self.delegate("MergePermissions")(roleId,newName,privIds)
        

    def RemoveAuthorizationRole(self, roleId, newName, privIds):
        '''Removes a role.

        :param roleId: The ID of the role that is updated.

        :param newName: The new name for the role.

        :param privIds: The new set of privileges to assign to the role.

        '''
        
        return self.delegate("RemoveAuthorizationRole")(roleId,newName,privIds)
        

    def RemoveEntityPermission(self, roleId, newName, privIds):
        '''Removes a permission rule from an entity.This will fail with an InvalidArgument
        fault if called on: the direct child folders of a datacenter managed
        object, the root resource pool of a ComputeResource or
        ClusterComputeResource, or a HostSystem that is part of a ComputeResource
        (Stand-alone Host). These objects always have the same permissions as
        their parent.This will fail with an InvalidArgument fault if called on a
        fault-tolerance (FT) secondary VirtualMachine. Such a VirtualMachine
        always has the same permissions as its FT primary VirtualMachine.

        :param roleId: The ID of the role that is updated.

        :param newName: The new name for the role.

        :param privIds: The new set of privileges to assign to the role.

        '''
        
        return self.delegate("RemoveEntityPermission")(roleId,newName,privIds)
        

    def ResetEntityPermissions(self, roleId, newName, privIds):
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

        :param roleId: The ID of the role that is updated.

        :param newName: The new name for the role.

        :param privIds: The new set of privileges to assign to the role.

        '''
        
        return self.delegate("ResetEntityPermissions")(roleId,newName,privIds)
        

    def RetrieveAllPermissions(self, roleId, newName, privIds):
        '''Finds all permissions defined in the system. The result is restricted to the
        managed entities visible to the user making the call.

        :param roleId: The ID of the role that is updated.

        :param newName: The new name for the role.

        :param privIds: The new set of privileges to assign to the role.

        '''
        
        return self.delegate("RetrieveAllPermissions")(roleId,newName,privIds)
        

    def RetrieveEntityPermissions(self, roleId, newName, privIds):
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

        :param roleId: The ID of the role that is updated.

        :param newName: The new name for the role.

        :param privIds: The new set of privileges to assign to the role.

        '''
        
        return self.delegate("RetrieveEntityPermissions")(roleId,newName,privIds)
        

    def RetrieveRolePermissions(self, roleId, newName, privIds):
        '''Finds all the permissions that use a particular role. The result is restricted to
        managed entities that are visible to the user making the call.

        :param roleId: The ID of the role that is updated.

        :param newName: The new name for the role.

        :param privIds: The new set of privileges to assign to the role.

        '''
        
        return self.delegate("RetrieveRolePermissions")(roleId,newName,privIds)
        

    def SetEntityPermissions(self, roleId, newName, privIds):
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

        :param roleId: The ID of the role that is updated.

        :param newName: The new name for the role.

        :param privIds: The new set of privileges to assign to the role.

        '''
        
        return self.delegate("SetEntityPermissions")(roleId,newName,privIds)
        

    def UpdateAuthorizationRole(self, roleId, newName, privIds):
        '''Updates a role's name or privileges. If the new set of privileges are assigned to
        the role, the system-defined privileges, "System.Anonymous",
        "System.View", and "System.Read" will be assigned to the role too.

        :param roleId: The ID of the role that is updated.

        :param newName: The new name for the role.

        :param privIds: The new set of privileges to assign to the role.

        '''
        
        return self.delegate("UpdateAuthorizationRole")(roleId,newName,privIds)
        
