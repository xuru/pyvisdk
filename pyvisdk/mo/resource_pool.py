
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
    described in more detail below:* GREEN (aka undercommitted): We have a tree
    that is in a state. Every node has a reservation greater than the sum of the
    reservations for its children. We have enough capacity at the root to satisfy
    all the resources reserved by the children. All operations performed on the
    tree, such as powering on virtual machines, creating new resource pools, or
    reconfiguring resource settings, will ensure that the above constraints are
    maintained. * RED (aka. inconsistent): One or more nodes in the tree has
    children whose reservations are greater than the node is configured to support.
    For example, i) a resource pool with a fixed reservation has a running virtual
    machine with a reservation that is higher than the reservation on resource pool
    itself., or ii) the child reservations are greater than the limit.In this
    state, the DRS algorithm is disabled until the resource pool tree's
    configuration has been brought back into a consistent state. We also restrict
    the resources that such invalid nodes request from their parents to the
    configured reservation/limit, in an attempt to isolate the problem to a small
    subtree. For the rest of the tree, we determine whether the cluster is
    undercommitted or overcommitted according to the existing rules and perform
    admission control accordingly.Note that since all changes to the resource
    settings are validated on the VirtualCenter server, the system cannot be
    brought into this state by simply manipulating a cluster resource pool tree
    through VirtualCenter. It can only happen if a virtual machine gets powered on
    directly on a host that is part of a DRS cluster.* YELLOW (aka overcommitted):
    In this state, the tree is consistent internally, but the root resource pool
    does not have the capacity at to meet the reservation of its children. We can
    only go from GREEN -> YELLOW if we lose resources at the root. For example,
    hosts becomes unavailable or is put into maintenance mode. Note that we will
    always have enough capacity at the root to run all currently powered on VMs.
    However, we may not be able to satisfy all resource pool reservations in the
    tree. In this state, the reservation configured for a resource pool is no
    longer guaranteed, but the limits are still enforced. This provides additional
    flexibility for bringing the tree back into a consistent state, without risking
    bringing the tree into a RED state. In more detail: * Resource Pool The root is
    considered to have unlimited capacity. You can reserve resources without any
    check except the requirement that the tree remains consistent. This means that
    nodes whose parents are all configured with expandable reservations and no
    limit will have unlimited available resources. However, if there is an ancestor
    with a fixed reservation or an expandable reservation with a limit somewhere,
    then the node will be limited by the reservation/limit of the ancestor. *
    Virtual Machine Virtual machines are limited by ancestors with a fixed
    reservation and the capacity at the root.Destroying a ResourcePoolWhen a
    ResourcePool is destroyed, all the virtual machines are reassigned to its
    parent pool. The root resource pool cannot be destroyed, and invoking destroy
    on it will throw an InvalidType fault.Any vApps in the ResourcePool will be
    moved to the ResourcePool's parent before the pool is destroyed.The
    Resource.DeletePool privilege must be held on the pool as well as the parent of
    the resource pool. Also, the Resource.AssignVMToPool privilege must be held on
    the resource pool's parent pool and any virtual machines that are reassigned.'''

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

    
    
    def CreateChildVM_Task(self, config, host=None):
        '''Creates a new virtual machine in a vApp container.Creates a new virtual machine
        in a vApp container.Creates a new virtual machine in a vApp container.Creates a
        new virtual machine in a vApp container.Creates a new virtual machine in a vApp
        container.
        
        :param config: The configuration of the virtual machine hardware.
        
        :param host: The target host on which the virtual machine will run. This must specify a host that is a member of the ComputeResource indirectly specified by the pool. For a stand-alone host or a cluster with DRS, host can be omitted, and the system selects a default.
        
        '''
        return self.delegate("CreateChildVM_Task")(config, host)
    
    def CreateResourcePool(self, name, spec):
        '''Creates a new resource pool.Creates a new resource pool.Creates a new resource
        pool.
        
        :param name: 
        
        :param spec: 
        
        '''
        return self.delegate("CreateResourcePool")(name, spec)
    
    def CreateVApp(self, name, resSpec, configSpec, vmFolder=None):
        '''Creates a new vApp container.Creates a new vApp container.
        
        :param name: The name of the vApp container in the inventory
        
        :param resSpec: The resource configuration for the vApp container (same as for a regular resource pool).
        
        :param configSpec: The specification of the vApp specific meta-data.
        
        :param vmFolder: The parent folder for the vApp. This must be null if this is a child vApp.
        
        '''
        return self.delegate("CreateVApp")(name, resSpec, configSpec, vmFolder)
    
    def DestroyChildren(self):
        '''Removes all child resource pools recursively. All virtual machines and vApps
        associated with the child resource pools get associated with this resource
        pool.Removes all child resource pools recursively. All virtual machines and
        vApps associated with the child resource pools get associated with this
        resource pool.Removes all child resource pools recursively. All virtual
        machines and vApps associated with the child resource pools get associated with
        this resource pool.Removes all child resource pools recursively. All virtual
        machines and vApps associated with the child resource pools get associated with
        this resource pool.
        
        '''
        return self.delegate("DestroyChildren")()
    
    def ImportVApp(self, spec, folder=None, host=None):
        '''Creates a new entity in this resource pool. The import process consists of two
        steps:
        
        :param spec: An ImportSpec describing what to import.
        
        :param folder: The folder to which the entity will be attached.
        
        :param host: The target host on which the entity will run. This must specify a host that is a member of the ComputeResource indirectly specified by the pool. For a stand-alone host or a cluster with DRS, host can be omitted, and the system selects a default.
        
        '''
        return self.delegate("ImportVApp")(spec, folder, host)
    
    def MoveIntoResourcePool(self, list):
        '''Moves a set of resource pools, vApps or virtual machines into this pool. The
        pools, vApps and virtual machines must be part of the cluster or standalone
        host that contains this pool.Moves a set of resource pools, vApps or virtual
        machines into this pool. The pools, vApps and virtual machines must be part of
        the cluster or standalone host that contains this pool.Moves a set of resource
        pools, vApps or virtual machines into this pool. The pools, vApps and virtual
        machines must be part of the cluster or standalone host that contains this
        pool.Moves a set of resource pools, vApps or virtual machines into this pool.
        The pools, vApps and virtual machines must be part of the cluster or standalone
        host that contains this pool.Moves a set of resource pools, vApps or virtual
        machines into this pool. The pools, vApps and virtual machines must be part of
        the cluster or standalone host that contains this pool.Moves a set of resource
        pools, vApps or virtual machines into this pool. The pools, vApps and virtual
        machines must be part of the cluster or standalone host that contains this
        pool.
        
        :param list: A list of ResourcePool and VirtualMachine objects.
        
        '''
        return self.delegate("MoveIntoResourcePool")(list)
    
    def QueryResourceConfigOption(self):
        '''Get a value range and default values for ResourceConfigSpec.
        
        '''
        return self.delegate("QueryResourceConfigOption")()
    
    def RefreshRuntime(self):
        '''Refreshes the resource usage data that is available in ResourcePoolRuntimeInfo.
        The latest runtime resource usage of this resource pool may not be available
        immediately after operations that alter resource usage, such as powering on a
        virtual machine. Invoke this method when resource usage may have recently
        changed, and the most up-to-date value in the ResourcePoolRuntimeInfo is
        needed.
        
        '''
        return self.delegate("RefreshRuntime")()
    
    def RegisterChildVM_Task(self, path, name=None, host=None):
        '''Adds an existing virtual machine to this resource pool or vApp.Adds an existing
        virtual machine to this resource pool or vApp.Adds an existing virtual machine
        to this resource pool or vApp.
        
        :param path: A datastore path to the virtual machine. If the path ends with ".vmtx", indicating that it refers to a VM template, an InvalidArgument fault is thrown.
        
        :param name: The name to be assigned to the virtual machine. If this parameter is not set, the displayName configuration parameter of the virtual machine is used. An entity name must be a non-empty string of less than 80 characters. The slash (/), backslash (\) and percent (%) will be escaped using the URL syntax. For example, %2F.
        
        :param host: The target host on which the virtual machine will run. This parameter must specify a host that is a member of the ComputeResource to which this resource pool belongs. For a stand-alone host or a cluster with DRS, the parameter can be omitted, and the system selects a default.
        
        '''
        return self.delegate("RegisterChildVM_Task")(path, name, host)
    
    def UpdateChildResourceConfiguration(self, spec):
        '''Changes resource configuration of a set of children of this resource pool. The
        method allows bulk modifications of the set of the direct children (virtual
        machines and resource pools).Changes resource configuration of a set of
        children of this resource pool. The method allows bulk modifications of the set
        of the direct children (virtual machines and resource pools).Changes resource
        configuration of a set of children of this resource pool. The method allows
        bulk modifications of the set of the direct children (virtual machines and
        resource pools).Changes resource configuration of a set of children of this
        resource pool. The method allows bulk modifications of the set of the direct
        children (virtual machines and resource pools).Changes resource configuration
        of a set of children of this resource pool. The method allows bulk
        modifications of the set of the direct children (virtual machines and resource
        pools).
        
        :param spec: 
        
        '''
        return self.delegate("UpdateChildResourceConfiguration")(spec)
    
    def UpdateConfig(self, name=None, config=None):
        '''Updates the configuration of the resource pool.Updates the configuration of the
        resource pool.Updates the configuration of the resource pool.Updates the
        configuration of the resource pool.
        
        :param name: If set, then the new name of the resource pool.
        
        :param config: If set, then the new resource allocation for this resource pool.
        
        '''
        return self.delegate("UpdateConfig")(name, config)