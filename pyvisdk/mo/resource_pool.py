
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.mo.managed_entity import ManagedEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ResourcePool(ManagedEntity):
    '''Represents a set of physical resources: a single host, a subset of a host's
    resources, or resources spanning multiple hosts. Resource pools can be
    subdivided by creating child resource pools. In order to run, a virtual machine
    must be associated as a child of a resource pool.In a parent/child hierarchy of
    resource pools and virtual machines, the single resource pool that has no
    parent pool is known as the .ConfigurationA resource pool is configured with a
    set of CPU (in MHz) and memory (in MB) resources. These resources are specified
    in absolute terms with a resource reservation and a resource limit, along with
    a shares setting. The shares are used during resource contention, to ensure
    graceful degradation.For the root resource pool, the values of the reservation
    and the limit are set by the system and are not configurable. The reservation
    and limit are set to the same value, indicating the total amount of resources
    the system has available to run virtual machines. This is computed as the
    aggregated CPU and memory resources provided by the set of current available
    hosts in the parent compute resource minus the overhead of the virtualization
    layer.Since the resource pool configuration is absolute (in MHz or MB), the
    configuration can become invalid when resources are removed. This can happen if
    a host is removed from the cluster, if a host becomes unavailable, or if a host
    is placed in maintenance mode. When this happens, the system flags
    misconfigured resource pools and displays the reservations and limits that are
    in effect. Further, in a DRS enabled cluster, the tree can be misconfigured if
    the user bypasses VirtualCenter and powers on VMs directly on the host.There
    are three states that the resource pool tree can be in: undercommited (green),
    overcommited (yellow), and inconsistent (red). Depending on the state,
    different resource pool configuration policies are enforced. The states are
    described in more detail below:In this state, the DRS algorithm is disabled
    until the resource pool tree's configuration has been brought back into a
    consistent state. We also restrict the resources that such invalid nodes
    request from their parents to the configured reservation/limit, in an attempt
    to isolate the problem to a small subtree. For the rest of the tree, we
    determine whether the cluster is undercommitted or overcommitted according to
    the existing rules and perform admission control accordingly.Note that since
    all changes to the resource settings are validated on the VirtualCenter server,
    the system cannot be brought into this state by simply manipulating a cluster
    resource pool tree through VirtualCenter. It can only happen if a virtual
    machine gets powered on directly on a host that is part of a DRS
    cluster.Destroying a ResourcePoolWhen a ResourcePool is destroyed, all the
    virtual machines are reassigned to its parent pool. The root resource pool
    cannot be destroyed, and invoking destroy on it will throw an InvalidType
    fault.Any vApps in the ResourcePool will be moved to the ResourcePool's parent
    before the pool is destroyed.The Resource.DeletePool privilege must be held on
    the pool as well as the parent of the resource pool. Also, the
    Resource.AssignVMToPool privilege must be held on the resource pool's parent
    pool and any virtual machines that are reassigned.'''
    
    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.ResourcePool):
        super(ResourcePool, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def childConfiguration(self):
        '''The resource configuration of all direct children (VirtualMachine and
    ResourcePool) of this resource group.'''
        return self.update('childConfiguration')
    @property
    def config(self):
        '''Configuration of this resource pool.'''
        return self.update('config')
    @property
    def owner(self):
        '''The ComputeResource to which this set of one or more nested resource pools
    belong.'''
        return self.update('owner')
    @property
    def resourcePool(self):
        '''The set of child resource pools.'''
        return self.update('resourcePool')
    @property
    def runtime(self):
        '''Runtime information about a resource pool. The ResourcePoolResourceUsage
    information within ResourcePoolRuntimeInfo can be transiently stale. Use
    RefreshRuntime method to update the information.'''
        return self.update('runtime')
    @property
    def summary(self):
        '''Basic information about a resource pool.'''
        return self.update('summary')
    @property
    def vm(self):
        '''The set of virtual machines associated with this resource pool.'''
        return self.update('vm')
    
    
    
    def CreateChildVM_Task(self):
        '''Creates a new virtual machine in a vApp container.This method supports creating
        a virtual machine directly in a vApp. A virtual machine in a vApp is not
        associated with a VM folder and therefore cannot be created using the method on
        a Folder.This method can only be called directly on a vApp or on a resource
        pool that is a child of a vApp.The privilege VirtualMachine.Inventory.Create is
        required on this entity. Further, if this is a resource pool, the privilege
        Resource.AssignVMToPool is required. If this is a vApp, the privilege
        VApp.AssignVM is required.Depending on the properties of the virtual machine
        bring created, additional privileges may be required. See CreateVM_Task for a
        description of these privileges.
        :rtype: ManagedObjectReference to a Task
        :returns: 
        '''
        return self.delegate("CreateChildVM_Task")()
    
    def CreateResourcePool(self):
        '''Creates a new resource pool.In the ResourceConfigSpec, all values in
        ResourceAllocationInfo must be supplied; they are not optional.Any % (percent)
        character used in this name parameter must be escaped, unless it is used to
        start an escape sequence. Clients may also escape any other characters in this
        name parameter.
        :rtype: ManagedObjectReference to a ResourcePool
        :returns: 
        '''
        return self.delegate("CreateResourcePool")()
    
    def CreateVApp(self):
        '''Creates a new vApp container.Any % (percent) character used in this name
        parameter must be escaped, unless it is used to start an escape sequence.
        Clients may also escape any other characters in this name parameter.
        :rtype: ManagedObjectReference to a VirtualApp
        :returns: 
        '''
        return self.delegate("CreateVApp")()
    
    def DestroyChildren(self):
        '''Removes all child resource pools recursively. All virtual machines and vApps
        associated with the child resource pools get associated with this resource
        pool.Note that resource pools contained in child vApps are not affected.The
        privilege checks performed are the following.
        :rtype: None
        :returns: 
        '''
        return self.delegate("DestroyChildren")()
    
    def ImportVApp(self):
        '''Creates a new entity in this resource pool. The import process consists of two
        steps:
        :rtype: ManagedObjectReference to a HttpNfcLease
        :returns: 
        '''
        return self.delegate("ImportVApp")()
    
    def MoveIntoResourcePool(self):
        '''Moves a set of resource pools, vApps or virtual machines into this pool. The
        pools, vApps and virtual machines must be part of the cluster or standalone
        host that contains this pool.For each entity being moved, the move is subject
        to the following privilege checks:This operation is typically used by clients
        when they implement a drag-and-drop interface to move a set of objects into a
        folder.This operation is only transactional with respect to each individual
        entity. The set of entities is moved sequentially, as specified in the list,
        and committed one at a time. If a failure is detected, then the method
        terminates with an exception.The root resource pool cannot be moved.
        :rtype: None
        :returns: 
        '''
        return self.delegate("MoveIntoResourcePool")()
    
    def QueryResourceConfigOption(self):
        '''Get a value range and default values for ResourceConfigSpec.
        :rtype: 
        :returns: 
        '''
        return self.delegate("QueryResourceConfigOption")()
    
    def RefreshRuntime(self):
        '''Refreshes the resource usage data that is available in ResourcePoolRuntimeInfo.
        The latest runtime resource usage of this resource pool may not be available
        immediately after operations that alter resource usage, such as powering on a
        virtual machine. Invoke this method when resource usage may have recently
        changed, and the most up-to-date value in the ResourcePoolRuntimeInfo is
        needed.
        :rtype: None
        :returns: 
        '''
        return self.delegate("RefreshRuntime")()
    
    def RegisterChildVM_Task(self):
        '''Adds an existing virtual machine to this resource pool or vApp.This operation
        only works for vApps or resource pools that are children of vApps. To register
        a VM in a folder, see RegisterVM_Task.Any % (percent) character used in this
        name parameter must be escaped, unless it is used to start an escape sequence.
        Clients may also escape any other characters in this name parameter.
        :rtype: ManagedObjectReference to a Task
        :returns: 
        '''
        return self.delegate("RegisterChildVM_Task")()
    
    def UpdateChildResourceConfiguration(self):
        '''Changes resource configuration of a set of children of this resource pool. The
        method allows bulk modifications of the set of the direct children (virtual
        machines and resource pools).Bulk modifications are not transactional. Each
        modification is made individually. If a failure is encountered while applying
        the changes, then the processing stops, meaning at least one and as many as all
        of the changes are not applied.A set can include a subset of the resources.
        Children that are not mentioned in the list are not changed.For each
        ResourceConfigSpec, the following privilege checks apply:
        :rtype: None
        :returns: 
        '''
        return self.delegate("UpdateChildResourceConfiguration")()
    
    def UpdateConfig(self):
        '''Updates the configuration of the resource pool.Any % (percent) character used
        in this name parameter must be escaped, unless it is used to start an escape
        sequence. Clients may also escape any other characters in this name
        parameter.The privilege checks for this operation are as follows:
        :rtype: None
        :returns: 
        '''
        return self.delegate("UpdateConfig")()