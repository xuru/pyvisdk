
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.managed_entity import ManagedEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DistributedVirtualSwitch(ManagedEntity):
    '''The interface to the distributed virtual switch objects.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.DistributedVirtualSwitch):
        # MUST define these
        super(DistributedVirtualSwitch, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def capability(self):
        '''
        The capability of the switch. Queried against hosts, the property should always
        return configModificationSupported as false.
        '''
        return self.update('capability')

    @property
    def config(self):
        '''
        The configuration of the switch.
        '''
        return self.update('config')

    @property
    def networkResourcePool(self):
        '''
        The network resource pool information for the switch.
        '''
        return self.update('networkResourcePool')

    @property
    def portgroup(self):
        '''
        The portgroups that are defined on the switch.
        '''
        return self.update('portgroup')

    @property
    def summary(self):
        '''
        The summary of the switch.
        '''
        return self.update('summary')

    @property
    def uuid(self):
        '''
        The generated UUID of the switch. Unique across vCenter Server inventory and
        instances.
        '''
        return self.update('uuid')


    def UpdateDvsCapability(self, capability):
        '''Set the capability of the switch.

        :param capability: The capability of the switch.

        '''
        
        return self.delegate("UpdateDvsCapability")(capability)
        

    def MoveDVPort_Task(self, portKey):
        '''Move the ports out of their current portgroup into the specified portgroup. If the
        moving of any of the ports results in a violation of the portgroup policy,
        or type of the source or destination portgroup, the operation raises a
        fault. A conflict port cannot be moved.

        :param portKey: The keys of the ports to be moved into the portgroup.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("MoveDVPort_Task")(portKey)
        

    def UpdateNetworkResourcePool(self, configSpec):
        '''Update the network resource pool configuration.

        :param configSpec: the network resource pool configuration specification.

        '''
        
        return self.delegate("UpdateNetworkResourcePool")(configSpec)
        

    def EnableNetworkResourceManagement(self, enable):
        '''Enable/Disable network I/O control on the vNetwork Distributed Switch.

        :param enable: If true, enables I/O control. If false, disables network I/O control.

        '''
        
        return self.delegate("EnableNetworkResourceManagement")(enable)
        

    def AddDVPortgroup_Task(self, spec):
        '''Add a DistributedVirtualPortgroup to the switch.

        :param spec: The specification for the portgroup.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("AddDVPortgroup_Task")(spec)
        

    def FetchDVPorts(self):
        '''Return the ports that meet the criteria.

        :rtype: DistributedVirtualPort[] 

        '''
        
        return self.delegate("FetchDVPorts")()
        

    def ReconfigureDVPort_Task(self, port):
        '''Reconfigure individual ports.

        :param port: The specification of the ports.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("ReconfigureDVPort_Task")(port)
        

    def ReconfigureDvs_Task(self, spec):
        '''Reconfigure the switch.Reconfiguring the switch may require any of the following
        privileges, depending on what is being changed:

        :param spec: The configuration of the switch


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("ReconfigureDvs_Task")(spec)
        

    def FetchDVPortKeys(self):
        '''Return the keys of ports that meet the criteria. Queried against host, the
        property reports only the connected ports currently on the host.

        :rtype: xsd:string[] 

        '''
        
        return self.delegate("FetchDVPortKeys")()
        

    def RectifyDvsHost_Task(self):
        '''Update the switch configuration on the host to bring them in sync with the current
        configuration in vCenter Server.

        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("RectifyDvsHost_Task")()
        

    def QueryUsedVlanIdInDvs(self):
        '''Return the used VLAN ID (PVLAN excluded) in the switch.

        :rtype: xsd:int[] 

        '''
        
        return self.delegate("QueryUsedVlanIdInDvs")()
        

    def PerformDvsProductSpecOperation_Task(self, operation):
        '''Push the proxy VirtualSwitch module of the specified product info to the host
        members of the switch at a fixed location known by the host.

        :param operation: The operation. See DistributedVirtualSwitchProductSpecOperationType for valid values. For VmwareDistributedVirtualSwitch, only upgrade is valid.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("PerformDvsProductSpecOperation_Task")(operation)
        

    def MergeDvs_Task(self):
        '''Merge an existing DistributedVirtualSwitch (source) to this switch (destination).
        The host members and the connected entity of the source switch will be
        transferred to the destination switch. This operation disconnects the
        entities from the source switch, tears down its host proxy
        VirtualSwitches, creates new ones for the destination switch, and
        reconnects the entities to the destination switch.In summary, this
        operation does the following:

        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("MergeDvs_Task")()
        

    def RefreshDVPortState(self):
        '''Refresh port states.
        '''
        
        return self.delegate("RefreshDVPortState")()
        
