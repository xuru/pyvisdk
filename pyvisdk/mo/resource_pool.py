
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.managed_entity import ManagedEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ResourcePool(ManagedEntity):
    '''Configuration
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.ResourcePool):
        # MUST define these
        super(ResourcePool, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def childConfiguration(self):
        '''The resource configuration of all direct children (VirtualMachine and
        ResourcePool) of this resource group.
        '''
        return self.update('childConfiguration')

    @property
    def config(self):
        '''Configuration of this resource pool.
        '''
        return self.update('config')

    @property
    def owner(self):
        '''The ComputeResource to which this set of one or more nested resource pools belong.
        '''
        return self.update('owner')

    @property
    def resourcePool(self):
        '''The set of child resource pools.
        '''
        return self.update('resourcePool')

    @property
    def runtime(self):
        '''Runtime information about a resource pool. The ResourcePoolResourceUsage
        information within ResourcePoolRuntimeInfo can be transiently stale. Use
        RefreshRuntime method to update the information.
        '''
        return self.update('runtime')

    @property
    def summary(self):
        '''Basic information about a resource pool.
        '''
        return self.update('summary')

    @property
    def vm(self):
        '''The set of virtual machines associated with this resource pool.
        '''
        return self.update('vm')


    def CreateChildVM_Task(self, config, host):
        '''Creates a new virtual machine in a vApp container.This method supports creating a
        virtual machine directly in a vApp. A virtual machine in a vApp is not
        associated with a VM folder and therefore cannot be created using the
        method on a Folder.This method can only be called directly on a vApp or on
        a resource pool that is a child of a vApp.The privilege
        VirtualMachine.Inventory.Create is required on this entity. Further, if
        this is a resource pool, the privilege Resource.AssignVMToPool is
        required. If this is a vApp, the privilege VApp.AssignVM is
        required.Depending on the properties of the virtual machine bring created,
        additional privileges may be required. See CreateVM_Task for a description
        of these privileges.

        :param config: The configuration of the virtual machine hardware.

        :param host: The target host on which the virtual machine will run. This must specify a host
        that is a member of the ComputeResource indirectly specified by the pool.
        For a stand-alone host or a cluster with DRS, host can be omitted, and the
        system selects a default.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("CreateChildVM_Task")(config,host)
        

    def CreateResourcePool(self):
        '''Creates a new resource pool.In the ResourceConfigSpec, all values in
        ResourceAllocationInfo must be supplied; they are not optional.Any %
        (percent) character used in this name parameter must be escaped, unless it
        is used to start an escape sequence. Clients may also escape any other
        characters in this name parameter.

        :rtype: ManagedObjectReference to a ResourcePool 

        '''
        
        return self.delegate("CreateResourcePool")()
        

    def CreateVApp(self, name, resSpec, configSpec, vmFolder):
        '''Creates a new vApp container.Any % (percent) character used in this name parameter
        must be escaped, unless it is used to start an escape sequence. Clients
        may also escape any other characters in this name parameter.

        :param name: The name of the vApp container in the inventory

        :param resSpec: The resource configuration for the vApp container (same as for a regular resource
        pool).

        :param configSpec: The specification of the vApp specific meta-data.

        :param vmFolder: The parent folder for the vApp. This must be null if this is a child vApp.


        :rtype: ManagedObjectReference to a VirtualApp 

        '''
        
        return self.delegate("CreateVApp")(name,resSpec,configSpec,vmFolder)
        

    def DestroyChildren(self):
        '''Removes all child resource pools recursively. All virtual machines and vApps
        associated with the child resource pools get associated with this resource
        pool.Note that resource pools contained in child vApps are not
        affected.The privilege checks performed are the following.*
        Resource.DeletePool privilege must be held on this object and each of it's
        immediate children to be destroyed. * If VMs are being moved, the
        privilege Resource.AssignVMToPool must be held on this resource pool as
        well as on any virtual machines being moved. * If vApps are being moved,
        the privilege Resource.AssignVAppToPool must be held on this resource pool
        as well as on any vApps being moved.
        '''
        
        return self.delegate("DestroyChildren")()
        

    def ImportVApp(self, spec, folder, host):
        '''Creates a new entity in this resource pool. The import process consists of two
        steps:

        :param spec: An ImportSpec describing what to import.

        :param folder: The folder to which the entity will be attached.

        :param host: The target host on which the entity will run. This must specify a host that is a
        member of the ComputeResource indirectly specified by the pool. For a
        stand-alone host or a cluster with DRS, host can be omitted, and the
        system selects a default.


        :rtype: ManagedObjectReference to a HttpNfcLease 

        '''
        
        return self.delegate("ImportVApp")(spec,folder,host)
        

    def MoveIntoResourcePool(self, list):
        '''Moves a set of resource pools, vApps or virtual machines into this pool. The
        pools, vApps and virtual machines must be part of the cluster or
        standalone host that contains this pool.For each entity being moved, the
        move is subject to the following privilege checks:* If the object being
        moved is a ResourcePool, then Resource.MovePool must be held on the pool
        being moved and it's former parent pool or vApp. If the target is a vApp,
        the privilege VApp.AssignResourcePool must be held on it. If the target is
        a ResourcePool, Resource.MovePool must be held on it. * If the object
        being moved is a VirtualApp, VApp.Move must be held on the vApp being
        moved and it's former parent pool or vApp. If the target entity is a
        resource pool, Resource.AssignVAppToPool must be held on the target. If
        the target is a vApp, the privilege VApp.AssignVApp must be held on the
        target vApp. * If the object being moved is a VirtualMachine, then if the
        target is a ResourcePool, Resource.AssignVMToPool is required on the
        VirtualMachine and the target pool. If the target is a vApp, VApp.AssignVM
        is required on both the VirtualMachine and the target pool.This operation
        is typically used by clients when they implement a drag-and-drop interface
        to move a set of objects into a folder.This operation is only
        transactional with respect to each individual entity. The set of entities
        is moved sequentially, as specified in the list, and committed one at a
        time. If a failure is detected, then the method terminates with an
        exception.The root resource pool cannot be moved.

        :param list: A list of ResourcePool and VirtualMachine objects.

        '''
        
        return self.delegate("MoveIntoResourcePool")(list)
        

    def QueryResourceConfigOption(self):
        '''Get a value range and default values for ResourceConfigSpec.

        :rtype: ResourceConfigOption 

        '''
        
        return self.delegate("QueryResourceConfigOption")()
        

    def RefreshRuntime(self):
        '''Refreshes the resource usage data that is available in ResourcePoolRuntimeInfo.
        The latest runtime resource usage of this resource pool may not be
        available immediately after operations that alter resource usage, such as
        powering on a virtual machine. Invoke this method when resource usage may
        have recently changed, and the most up-to-date value in the
        ResourcePoolRuntimeInfo is needed.
        '''
        
        return self.delegate("RefreshRuntime")()
        

    def RegisterChildVM_Task(self, path, name, host):
        '''Adds an existing virtual machine to this resource pool or vApp.This operation only
        works for vApps or resource pools that are children of vApps. To register
        a VM in a folder, see RegisterVM_Task.Any % (percent) character used in
        this name parameter must be escaped, unless it is used to start an escape
        sequence. Clients may also escape any other characters in this name
        parameter.

        :param path: A datastore path to the virtual machine. If the path ends with ".vmtx", indicating
        that it refers to a VM template, an InvalidArgument fault is thrown.

        :param name: The name to be assigned to the virtual machine. If this parameter is not set, the
        displayName configuration parameter of the virtual machine is used. An
        entity name must be a non-empty string of less than 80 characters. The
        slash (/), backslash (\) and percent (%) will be escaped using the URL
        syntax. For example, %2F.

        :param host: The target host on which the virtual machine will run. This parameter must specify
        a host that is a member of the ComputeResource to which this resource pool
        belongs. For a stand-alone host or a cluster with DRS, the parameter can
        be omitted, and the system selects a default.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("RegisterChildVM_Task")(path,name,host)
        

    def UpdateChildResourceConfiguration(self):
        '''Changes resource configuration of a set of children of this resource pool. The
        method allows bulk modifications of the set of the direct children
        (virtual machines and resource pools).Bulk modifications are not
        transactional. Each modification is made individually. If a failure is
        encountered while applying the changes, then the processing stops, meaning
        at least one and as many as all of the changes are not applied.A set can
        include a subset of the resources. Children that are not mentioned in the
        list are not changed.For each ResourceConfigSpec, the following privilege
        checks apply:* If the ResourceConfigSpec refers to a child resource pool
        or a child vApp, the privileges required are the same as would be required
        for calling UpdateConfig on that entity. * If the ResourceConfigSpec
        refers to a virtual machine, VirtualMachine.Config.Resource must be held
        on the virtual machine.
        '''
        
        return self.delegate("UpdateChildResourceConfiguration")()
        

    def UpdateConfig(self, name, config):
        '''Updates the configuration of the resource pool.Any % (percent) character used in
        this name parameter must be escaped, unless it is used to start an escape
        sequence. Clients may also escape any other characters in this name
        parameter.The privilege checks for this operation are as follows:* If this
        is a resource pool, the privilege Resource.EditPool is required on this
        and on the parent pool or vApp. * If this is a vApp, the privilege
        VApp.ResourceConfig is required on this and on the parent pool or vApp.

        :param name: If set, then the new name of the resource pool.

        :param config: If set, then the new resource allocation for this resource pool.

        '''
        
        return self.delegate("UpdateConfig")(name,config)
        
