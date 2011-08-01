
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ServiceInstance(BaseEntity):
    '''The ServiceInstance managed object is the singleton root object of the inventory
        on both vCenter servers and servers running on standalone host agents. The
        server creates the ServiceInstance automatically, and also automatically
        creates the various manager entities that provide services in the virtual
        environment. Some examples of manager entities are LicenseManager,
        PerformanceManager, and ViewManager. You can access the manager entities
        through the content property.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.ServiceInstance):
        # MUST define these
        super(ServiceInstance, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def serverClock(self):
        '''
        Contains the time most recently obtained from the server. The time is not
        necessarily current. This property is intended for use with the
        PropertyCollector WaitForUpdates method. The PropertyCollector will
        provide notification if some event occurs that changes the server clock
        time in a non-linear fashion.
        '''
        return self.update('serverClock')


    def ValidateMigration(self):
        '''Deprecated. As of vSphere API 4.0, use VirtualMachineProvisioningChecker instead.
        Checks the validity of a set of proposed migrations. A migration is the
        act of changing the assigned execution host of a virtual machine, which
        can result from invoking MigrateVM_Task or RelocateVM_Task.

        :rtype: Event[] 

        '''
        
        return self.delegate("ValidateMigration")()
        

    def RetrieveProductComponents(self):
        '''Component information for bundled products

        :rtype: ProductComponentInfo[] 

        '''
        
        return self.delegate("RetrieveProductComponents")()
        

    def QueryVMotionCompatibility(self):
        '''Deprecated. As of vSphere API 4.0, use QueryVMotionCompatibilityEx_Task instead.
        Investigates the general VMotion compatibility of a virtual machine with a
        set of hosts. The virtual machine may be in any power state. Hosts may be
        in any connection state and also may be in maintenance mode.

        :rtype: HostVMotionCompatibility[] 

        '''
        
        return self.delegate("QueryVMotionCompatibility")()
        

    def RetrieveServiceContent(self):
        '''Retrieves the properties of the service instance.

        :rtype: ServiceContent 

        '''
        
        return self.delegate("RetrieveServiceContent")()
        

    def CurrentTime(self):
        '''Returns the current time on the server. To monitor non-linear time changes, use
        the serverClock property.

        :rtype: xsd:dateTime 

        '''
        
        return self.delegate("CurrentTime")()
        
