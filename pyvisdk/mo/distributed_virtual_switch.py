
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
        '''The capability of the switch. Queried against hosts, the property should always
        return configModificationSupported as false.
        '''
        return self.update('capability')

    @property
    def config(self):
        '''The configuration of the switch.
        '''
        return self.update('config')

    @property
    def networkResourcePool(self):
        '''The network resource pool information for the switch.
        '''
        return self.update('networkResourcePool')

    @property
    def portgroup(self):
        '''The portgroups that are defined on the switch.
        '''
        return self.update('portgroup')

    @property
    def summary(self):
        '''The summary of the switch.
        '''
        return self.update('summary')

    @property
    def uuid(self):
        '''The generated UUID of the switch. Unique across vCenter Server inventory and
        instances.
        '''
        return self.update('uuid')


    def AddDVPortgroup_Task(self, configSpec):
        '''Add a DistributedVirtualPortgroup to the switch.

        :param configSpec: the network resource pool configuration specification.

        '''
        
        return self.delegate("AddDVPortgroup_Task")(configSpec)
        

    def EnableNetworkResourceManagement(self, configSpec):
        '''Enable/Disable network I/O control on the vNetwork Distributed Switch.

        :param configSpec: the network resource pool configuration specification.

        '''
        
        return self.delegate("EnableNetworkResourceManagement")(configSpec)
        

    def FetchDVPortKeys(self, configSpec):
        '''Return the keys of ports that meet the criteria. Queried against host, the
        property reports only the connected ports currently on the host.

        :param configSpec: the network resource pool configuration specification.

        '''
        
        return self.delegate("FetchDVPortKeys")(configSpec)
        

    def FetchDVPorts(self, configSpec):
        '''Return the ports that meet the criteria.

        :param configSpec: the network resource pool configuration specification.

        '''
        
        return self.delegate("FetchDVPorts")(configSpec)
        

    def MergeDvs_Task(self, configSpec):
        '''Merge an existing DistributedVirtualSwitch (source) to this switch (destination).
        The host members and the connected entity of the source switch will be
        transferred to the destination switch. This operation disconnects the
        entities from the source switch, tears down its host proxy
        VirtualSwitches, creates new ones for the destination switch, and
        reconnects the entities to the destination switch.In summary, this
        operation does the following:

        :param configSpec: the network resource pool configuration specification.

        '''
        
        return self.delegate("MergeDvs_Task")(configSpec)
        

    def MoveDVPort_Task(self, configSpec):
        '''Move the ports out of their current portgroup into the specified portgroup. If the
        moving of any of the ports results in a violation of the portgroup policy,
        or type of the source or destination portgroup, the operation raises a
        fault. A conflict port cannot be moved.

        :param configSpec: the network resource pool configuration specification.

        '''
        
        return self.delegate("MoveDVPort_Task")(configSpec)
        

    def PerformDvsProductSpecOperation_Task(self, configSpec):
        '''Push the proxy VirtualSwitch module of the specified product info to the host
        members of the switch at a fixed location known by the host.

        :param configSpec: the network resource pool configuration specification.

        '''
        
        return self.delegate("PerformDvsProductSpecOperation_Task")(configSpec)
        

    def QueryUsedVlanIdInDvs(self, configSpec):
        '''Return the used VLAN ID (PVLAN excluded) in the switch.

        :param configSpec: the network resource pool configuration specification.

        '''
        
        return self.delegate("QueryUsedVlanIdInDvs")(configSpec)
        

    def ReconfigureDVPort_Task(self, configSpec):
        '''Reconfigure individual ports.

        :param configSpec: the network resource pool configuration specification.

        '''
        
        return self.delegate("ReconfigureDVPort_Task")(configSpec)
        

    def ReconfigureDvs_Task(self, configSpec):
        '''Reconfigure the switch.Reconfiguring the switch may require any of the following
        privileges, depending on what is being changed:

        :param configSpec: the network resource pool configuration specification.

        '''
        
        return self.delegate("ReconfigureDvs_Task")(configSpec)
        

    def RectifyDvsHost_Task(self, configSpec):
        '''Update the switch configuration on the host to bring them in sync with the current
        configuration in vCenter Server.

        :param configSpec: the network resource pool configuration specification.

        '''
        
        return self.delegate("RectifyDvsHost_Task")(configSpec)
        

    def RefreshDVPortState(self, configSpec):
        '''Refresh port states.

        :param configSpec: the network resource pool configuration specification.

        '''
        
        return self.delegate("RefreshDVPortState")(configSpec)
        

    def UpdateDvsCapability(self, configSpec):
        '''Set the capability of the switch.

        :param configSpec: the network resource pool configuration specification.

        '''
        
        return self.delegate("UpdateDvsCapability")(configSpec)
        

    def UpdateNetworkResourcePool(self, configSpec):
        '''Update the network resource pool configuration.

        :param configSpec: the network resource pool configuration specification.

        '''
        
        return self.delegate("UpdateNetworkResourcePool")(configSpec)
        
