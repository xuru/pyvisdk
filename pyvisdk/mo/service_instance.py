
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ServiceInstance(BaseEntity):
    '''The ServiceInstance managed object is the singleton root object of the
    inventory on both vCenter servers and servers running on standalone host
    agents. The server creates the ServiceInstance automatically, and also
    automatically creates the various manager entities that provide services in the
    virtual environment. Some examples of manager entities are LicenseManager,
    PerformanceManager, and ViewManager. You can access the manager entities
    through the content property.A vSphere API client application begins by
    connecting to a server and obtaining a reference to the ServiceInstance. The
    client can then use the RetrieveServiceContent method to gain access to the
    various vSphere manager entities and to the root folder of the inventory.When
    you create managed objects, the server adds them to the inventory. The
    inventory of managed objects includes instances the following object types:*
    ServiceInstance -- Root of the inventory; created by vSphere. * Datacenter -- A
    container that represents a virtual data center. It contains hosts, network
    entities, virtual machines and virtual applications, and datastores. * Folder
    -- A container used for hierarchical organization of the inventory. *
    VirtualMachine -- A virtual machine. * VirtualApp -- A virtual application. *
    ComputeResource -- A compute resource (either a cluster or a stand-alone host).
    * ResourcePool -- A subset of resources provided by a ComputeResource. *
    HostSystem -- A single host (ESX Server or VMware Server). * Network -- A
    network available to either hosts or virtual machines. *
    DistributedVirtualSwitch -- A distributed virtual switch. *
    DistributedVirtualPortgroup -- A distributed virtual port group. * Datastore --
    Platform-independent, host-independent storage for virtual machine files.The
    following figure shows the organization of managed objects in the vCenter
    hierarchy:Every Datacenter has the following set of dedicated folders. These
    folders are empty until you create entities for the Datacenter.* A folder for
    any combination of VirtualMachine and/or VirtualApp objects. VirtualApp objects
    can be nested, but only the parent VirtualApp can be visible in the folder.
    Virtual machines that are children of virtual applications are not associated
    with a VirtualMachine/VirtualApp folder. * A folder for a ComputeResource
    hierarchy. * A folder for network entities - any combination of Network,
    DistributedVirtualSwitch, and/or DistributedVirtualPortgroup objects. * A
    folder for Datastore objects.The host agent hierarchy has the same general form
    as the vCenter hierarchy, but most of the objects are limited to one instance:'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.ServiceInstance):
        super(ServiceInstance, self).__init__(core, name=name, ref=ref, type=type)

    
    @property
    def capability(self):
        '''API-wide capabilities.'''
        return self.update('capability')
    @property
    def content(self):
        '''The properties of the ServiceInstance managed object. The content property is
        identical to the return value from the RetrieveServiceContent method.'''
        return self.update('content')
    @property
    def serverClock(self):
        '''Contains the time most recently obtained from the server. The time is not
        necessarily current. This property is intended for use with the
        PropertyCollector WaitForUpdates method. The PropertyCollector will provide
        notification if some event occurs that changes the server clock time in a non-
        linear fashion.'''
        return self.update('serverClock')

    
    
    def CurrentTime(self):
        '''Returns the current time on the server. To monitor non-linear time changes, use
        the serverClock property.
        
        '''
        return self.delegate("CurrentTime")()
    
    def QueryVMotionCompatibility(self, vm, host, compatibility=None):
        '''<b>Deprecated.</b> <i>As of vSphere API 4.0, use
        QueryVMotionCompatibilityEx_Task instead.</i> Investigates the general VMotion
        compatibility of a virtual machine with a set of hosts. The virtual machine may
        be in any power state. Hosts may be in any connection state and also may be in
        maintenance mode.
        
        :param vm: The virtual machine that is the designated VMotion candidate.
        
        :param host: The group of hosts to analyze for compatibility.
        
        :param compatibility: The set of compatibility types to investigate. Each is a string chosen from VMotionCompatibilityType. If this argument is not set, then all compatibility types are investigated.
        
        '''
        return self.delegate("QueryVMotionCompatibility")(vm, host, compatibility)
    
    def RetrieveProductComponents(self):
        '''Component information for bundled products
        
        '''
        return self.delegate("RetrieveProductComponents")()
    
    def RetrieveServiceContent(self):
        '''Retrieves the properties of the service instance.
        
        '''
        return self.delegate("RetrieveServiceContent")()
    
    def ValidateMigration(self, vm, state=None, testType=None, pool=None, host=None):
        '''<b>Deprecated.</b> <i>As of vSphere API 4.0, use
        VirtualMachineProvisioningChecker instead.</i> Checks the validity of a set of
        proposed migrations. A migration is the act of changing the assigned execution
        host of a virtual machine, which can result from invoking MigrateVM_Task or
        RelocateVM_Task.
        
        :param vm: The set of virtual machines intended for migration.
        
        :param state: The power state that the virtual machines must have. If this argument is not set, each virtual machine is evaluated according to its current power state.
        
        :param testType: The set of tests to run. If this argument is not set, all tests will be run.
        
        :param pool: The target resource pool for the virtual machines. If the pool parameter is left unset, the target pool for each particular virtual machine's migration will be that virtual machine's current pool. If the virtual machine is a template then either this parameter or the host parameter must be set; additionally if resource tests are requested then this parameter is required.
        
        :param host: The target host on which the virtual machines will run. The host parameter may be left unset if the compute resource associated with the target pool represents a stand-alone host or a DRS-enabled cluster. In the former case the stand-alone host is used as the target host. In the latter case, each connected host in the cluster that is not in maintenance mode is tested as a target host. If the virtual machine is a template then either this parameter or the pool parameter must be set.
        
        '''
        return self.delegate("ValidateMigration")(vm, state, testType, pool, host)