
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.managed_entity import ManagedEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ResourcePool(ManagedEntity):
    '''Represents a set of physical resources: a single host, a subset of a host's
        resources, or resources spanning multiple hosts. Resource pools can be
        subdivided by creating child resource pools. In order to run, a virtual
        machine must be associated as a child of a resource pool.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.ResourcePool):
        # MUST define these
        super(ResourcePool, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def childConfiguration(self):
        '''
        The resource configuration of all direct children (VirtualMachine and
        ResourcePool) of this resource group.
        '''
        return self.update('childConfiguration')

    @property
    def config(self):
        '''
        Configuration of this resource pool.
        '''
        return self.update('config')

    @property
    def owner(self):
        '''
        The ComputeResource to which this set of one or more nested resource pools belong.
        '''
        return self.update('owner')

    @property
    def resourcePool(self):
        '''
        The set of child resource pools.
        '''
        return self.update('resourcePool')

    @property
    def runtime(self):
        '''
        Runtime information about a resource pool. The ResourcePoolResourceUsage
        information within ResourcePoolRuntimeInfo can be transiently stale. Use
        RefreshRuntime method to update the information.
        '''
        return self.update('runtime')

    @property
    def summary(self):
        '''
        Basic information about a resource pool.
        '''
        return self.update('summary')

    @property
    def vm(self):
        '''
        The set of virtual machines associated with this resource pool.
        '''
        return self.update('vm')


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
        

    def CreateVApp(self, configSpec, resSpec, name):
        '''Creates a new vApp container.Any % (percent) character used in this name parameter
        must be escaped, unless it is used to start an escape sequence. Clients
        may also escape any other characters in this name parameter.

        :param configSpec: The specification of the vApp specific meta-data.

        :param resSpec: The resource configuration for the vApp container (same as for a regular resource pool).

        :param name: The name of the vApp container in the inventory


        :rtype: ManagedObjectReference to a VirtualApp 

        '''
        
        return self.delegate("CreateVApp")(configSpec,resSpec,name)
        

    def CreateChildVM_Task(self, config):
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


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("CreateChildVM_Task")(config)
        

    def ImportVApp(self, spec):
        '''Creates a new entity in this resource pool. The import process consists of two
        steps:

        :param spec: An ImportSpec describing what to import.


        :rtype: ManagedObjectReference to a HttpNfcLease 

        '''
        
        return self.delegate("ImportVApp")(spec)
        

    def UpdateConfig(self):
        '''Updates the configuration of the resource pool.Any % (percent) character used in
        this name parameter must be escaped, unless it is used to start an escape
        sequence. Clients may also escape any other characters in this name
        parameter.The privilege checks for this operation are as follows:
        '''
        
        return self.delegate("UpdateConfig")()
        

    def UpdateChildResourceConfiguration(self, spec):
        '''Changes resource configuration of a set of children of this resource pool. The
        method allows bulk modifications of the set of the direct children
        (virtual machines and resource pools).Bulk modifications are not
        transactional. Each modification is made individually. If a failure is
        encountered while applying the changes, then the processing stops, meaning
        at least one and as many as all of the changes are not applied.A set can
        include a subset of the resources. Children that are not mentioned in the
        list are not changed.For each ResourceConfigSpec, the following privilege
        checks apply:

        :param spec: 

        '''
        
        return self.delegate("UpdateChildResourceConfiguration")(spec)
        

    def CreateResourcePool(self, name, spec):
        '''Creates a new resource pool.In the ResourceConfigSpec, all values in
        ResourceAllocationInfo must be supplied; they are not optional.Any %
        (percent) character used in this name parameter must be escaped, unless it
        is used to start an escape sequence. Clients may also escape any other
        characters in this name parameter.

        :param name: 

        :param spec: 


        :rtype: ManagedObjectReference to a ResourcePool 

        '''
        
        return self.delegate("CreateResourcePool")(name,spec)
        

    def RegisterChildVM_Task(self, path):
        '''Adds an existing virtual machine to this resource pool or vApp.This operation only
        works for vApps or resource pools that are children of vApps. To register
        a VM in a folder, see RegisterVM_Task.Any % (percent) character used in
        this name parameter must be escaped, unless it is used to start an escape
        sequence. Clients may also escape any other characters in this name
        parameter.

        :param path: A datastore path to the virtual machine. If the path ends with ".vmtx", indicating that it refers to a VM template, an InvalidArgument fault is thrown.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("RegisterChildVM_Task")(path)
        

    def DestroyChildren(self):
        '''Removes all child resource pools recursively. All virtual machines and vApps
        associated with the child resource pools get associated with this resource
        pool.Note that resource pools contained in child vApps are not
        affected.The privilege checks performed are the following.
        '''
        
        return self.delegate("DestroyChildren")()
        

    def MoveIntoResourcePool(self):
        '''Moves a set of resource pools, vApps or virtual machines into this pool. The
        pools, vApps and virtual machines must be part of the cluster or
        standalone host that contains this pool.For each entity being moved, the
        move is subject to the following privilege checks:This operation is
        typically used by clients when they implement a drag-and-drop interface to
        move a set of objects into a folder.This operation is only transactional
        with respect to each individual entity. The set of entities is moved
        sequentially, as specified in the list, and committed one at a time. If a
        failure is detected, then the method terminates with an exception.The root
        resource pool cannot be moved.
        '''
        
        return self.delegate("MoveIntoResourcePool")()
        
