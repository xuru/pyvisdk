
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.mo.managed_entity import ManagedEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DistributedVirtualSwitch(ManagedEntity):
    '''The interface to the distributed virtual switch objects.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.DistributedVirtualSwitch):
        super(DistributedVirtualSwitch, self).__init__(core, name=name, ref=ref, type=type)

    
    @property
    def capability(self):
        '''The capability of the switch. Queried against hosts, the property should always
        return configModificationSupported as false.'''
        return self.update('capability')
    @property
    def config(self):
        '''The configuration of the switch.'''
        return self.update('config')
    @property
    def networkResourcePool(self):
        '''The network resource pool information for the switch.'''
        return self.update('networkResourcePool')
    @property
    def portgroup(self):
        '''The portgroups that are defined on the switch.'''
        return self.update('portgroup')
    @property
    def summary(self):
        '''The summary of the switch.'''
        return self.update('summary')
    @property
    def uuid(self):
        '''The generated UUID of the switch. Unique across vCenter Server inventory and
        instances.'''
        return self.update('uuid')

    
    
    def AddDVPortgroup_Task(self, spec):
        '''Add a DistributedVirtualPortgroup to the switch.
        
        :param spec: The specification for the portgroup.
        
        '''
        return self.delegate("AddDVPortgroup_Task")(spec)
    
    def AddNetworkResourcePool(self, configSpec):
        '''Add a network resource pool.
        
        :param configSpec: the network resource pool configuration specification.
        
        '''
        return self.delegate("AddNetworkResourcePool")(configSpec)
    
    def EnableNetworkResourceManagement(self, enable):
        '''Enable/Disable network I/O control on the vSphere Distributed Switch.
        
        :param enable: If true, enables I/O control. If false, disables network I/O control.
        
        '''
        return self.delegate("EnableNetworkResourceManagement")(enable)
    
    def FetchDVPortKeys(self, criteria=None):
        '''Return the keys of ports that meet the criteria. Queried against host, the
        property reports only the connected ports currently on the host.
        
        :param criteria: The port selection criteria. If unset, the operation returns the keys of all the ports in the switch.
        
        '''
        return self.delegate("FetchDVPortKeys")(criteria)
    
    def FetchDVPorts(self, criteria=None):
        '''Return the ports that meet the criteria.
        
        :param criteria: The port selection criteria. If unset, the operation returns the keys of all the ports in the portgroup.
        
        '''
        return self.delegate("FetchDVPorts")(criteria)
    
    def MergeDvs_Task(self, dvs):
        '''Merge an existing DistributedVirtualSwitch (source) to this switch
        (destination). The host members and the connected entity of the source switch
        will be transferred to the destination switch. This operation disconnects the
        entities from the source switch, tears down its host proxy VirtualSwitches,
        creates new ones for the destination switch, and reconnects the entities to the
        destination switch.Merge an existing DistributedVirtualSwitch (source) to this
        switch (destination). The host members and the connected entity of the source
        switch will be transferred to the destination switch. This operation
        disconnects the entities from the source switch, tears down its host proxy
        VirtualSwitches, creates new ones for the destination switch, and reconnects
        the entities to the destination switch.Merge an existing
        DistributedVirtualSwitch (source) to this switch (destination). The host
        members and the connected entity of the source switch will be transferred to
        the destination switch. This operation disconnects the entities from the source
        switch, tears down its host proxy VirtualSwitches, creates new ones for the
        destination switch, and reconnects the entities to the destination switch.
        
        :param dvs: The switch (source) to be merged
        
        '''
        return self.delegate("MergeDvs_Task")(dvs)
    
    def MoveDVPort_Task(self, portKey, destinationPortgroupKey=None):
        '''Move the ports out of their current portgroup into the specified portgroup. If
        the moving of any of the ports results in a violation of the portgroup policy,
        or type of the source or destination portgroup, the operation raises a fault. A
        conflict port cannot be moved.
        
        :param portKey: The keys of the ports to be moved into the portgroup.
        
        :param destinationPortgroupKey: The key of the portgroup to be moved into. If unset, the port will be moved under the switch.
        
        '''
        return self.delegate("MoveDVPort_Task")(portKey, destinationPortgroupKey)
    
    def PerformDvsProductSpecOperation_Task(self, operation, productSpec=None):
        '''This method updates the DistributedVirtualSwitch product specifications.
        
        :param operation: The operation. See DistributedVirtualSwitchProductSpecOperationType for valid values. For VmwareDistributedVirtualSwitch, only upgrade is valid.
        
        :param productSpec: The product info of the implementation.
        
        '''
        return self.delegate("PerformDvsProductSpecOperation_Task")(operation, productSpec)
    
    def QueryUsedVlanIdInDvs(self):
        '''Return the used VLAN ID (PVLAN excluded) in the switch.
        
        '''
        return self.delegate("QueryUsedVlanIdInDvs")()
    
    def ReconfigureDVPort_Task(self, port):
        '''Reconfigure individual ports.
        
        :param port: The specification of the ports.
        
        '''
        return self.delegate("ReconfigureDVPort_Task")(port)
    
    def ReconfigureDvs_Task(self, spec):
        '''Reconfigure the switch.Reconfigure the switch.Reconfigure the switch.
        
        :param spec: The configuration of the switch
        
        '''
        return self.delegate("ReconfigureDvs_Task")(spec)
    
    def RectifyDvsHost_Task(self, hosts=None):
        '''<b>Deprecated.</b> <i>as of vSphere API 5.0. Use RectifyDvsOnHost_Task instead.
        Update the switch configuration on the host to bring them in sync with the
        current configuration in vCenter Server.</i> deprecated as of vSphere API 5.0.
        Use RectifyDvsOnHost_Task instead. Update the switch configuration on the host
        to bring them in sync with the current configuration in vCenter Server.
        
        :param hosts: The hosts to be rectified.
        
        '''
        return self.delegate("RectifyDvsHost_Task")(hosts)
    
    def RefreshDVPortState(self, portKeys=None):
        '''Refresh port states.
        
        :param portKeys: The keys of the ports to be refreshed. If not set, all port states are refreshed.
        
        '''
        return self.delegate("RefreshDVPortState")(portKeys)
    
    def RemoveNetworkResourcePool(self, key):
        '''Remove a network resource pool.
        
        :param key: the network resource pool key
        
        '''
        return self.delegate("RemoveNetworkResourcePool")(key)
    
    def UpdateDvsCapability(self, capability):
        '''Set the capability of the switch.
        
        :param capability: The capability of the switch.
        
        '''
        return self.delegate("UpdateDvsCapability")(capability)
    
    def UpdateNetworkResourcePool(self, configSpec):
        '''Update the network resource pool configuration.
        
        :param configSpec: the network resource pool configuration specification.
        
        '''
        return self.delegate("UpdateNetworkResourcePool")(configSpec)