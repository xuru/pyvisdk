
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
    
    
    
    def AddDVPortgroup_Task(self):
        '''Add a DistributedVirtualPortgroup to the switch.
        :rtype: ManagedObjectReference to a Task
        :returns: 
        '''
        return self.delegate("AddDVPortgroup_Task")()
    
    def EnableNetworkResourceManagement(self):
        '''Enable/Disable network I/O control on the vNetwork Distributed Switch.
        :rtype: None
        :returns: 
        '''
        return self.delegate("EnableNetworkResourceManagement")()
    
    def FetchDVPortKeys(self):
        '''Return the keys of ports that meet the criteria. Queried against host, the
        property reports only the connected ports currently on the host.
        :rtype: 
        :returns: 
        '''
        return self.delegate("FetchDVPortKeys")()
    
    def FetchDVPorts(self):
        '''Return the ports that meet the criteria.
        :rtype: 
        :returns: 
        '''
        return self.delegate("FetchDVPorts")()
    
    def MergeDvs_Task(self):
        '''Merge an existing DistributedVirtualSwitch (source) to this switch
        (destination). The host members and the connected entity of the source switch
        will be transferred to the destination switch. This operation disconnects the
        entities from the source switch, tears down its host proxy VirtualSwitches,
        creates new ones for the destination switch, and reconnects the entities to the
        destination switch.In summary, this operation does the following:* Adds the
        maxPorts of the source switch to the maxPorts of the destination switch. * The
        host members of the source switch leave the source switch and join the
        destination switch with the same pNIC and VirtualSwitch (if applicable). A set
        of new uplink ports, compliant with the uplinkPortPolicy, is created as the
        hosts join the destination switch. * The portgroups on the source switch are
        copied over to destination switch, by calculating the effective default port
        config and creating a portgroup of the same name in the destination switch. If
        the name already exists, the copied portgroup uses names like "Copy of switch-
        portgroup-name" scheme to avoid conflict. The same number of ports are created
        inside each copied portgroup. * The standalone DVPorts are not copied, unless
        there is a Virtual Machine or host vNIC connecting to it. In that case, the
        operation calculates the effective port config and creates a port in the
        designation DVS with the same name. Name conflict is resolved by numbers like
        "original-port-name(1)". The uplink ports are not copied over. * The Virtual
        Machine host vNICs are disconnected from the source switch and reconnected with
        the destination switch, either to the copied standalone port or portgroup. *
        (Applicable to VmwareDistributedVirtualSwitch object only) Unless the PVLAN map
        contains exactly the same entries between the source and destination switches,
        the operation raises a fault if pvlanId is set in any port, portgroup, or
        switch that will be copied.
        :rtype: ManagedObjectReference to a Task
        :returns: 
        '''
        return self.delegate("MergeDvs_Task")()
    
    def MoveDVPort_Task(self):
        '''Move the ports out of their current portgroup into the specified portgroup. If
        the moving of any of the ports results in a violation of the portgroup policy,
        or type of the source or destination portgroup, the operation raises a fault. A
        conflict port cannot be moved.
        :rtype: ManagedObjectReference to a Task
        :returns: 
        '''
        return self.delegate("MoveDVPort_Task")()
    
    def PerformDvsProductSpecOperation_Task(self):
        '''Push the proxy VirtualSwitch module of the specified product info to the host
        members of the switch at a fixed location known by the host.
        :rtype: ManagedObjectReference to a Task
        :returns: 
        '''
        return self.delegate("PerformDvsProductSpecOperation_Task")()
    
    def QueryUsedVlanIdInDvs(self):
        '''Return the used VLAN ID (PVLAN excluded) in the switch.
        :rtype: 
        :returns: 
        '''
        return self.delegate("QueryUsedVlanIdInDvs")()
    
    def ReconfigureDVPort_Task(self):
        '''Reconfigure individual ports.
        :rtype: ManagedObjectReference to a Task
        :returns: 
        '''
        return self.delegate("ReconfigureDVPort_Task")()
    
    def ReconfigureDvs_Task(self):
        '''Reconfigure the switch.Reconfiguring the switch may require any of the
        following privileges, depending on what is being changed:* DVSwitch.PolicyOp if
        policy is set. * DVSwitch.PortSetting if defaultPortConfig is set. *
        DVSwitch.HostOp if policy is set. The user will also need the
        Host.Config.Network privilege on the host. * DVSwitch.Modify for anything else.
        :rtype: ManagedObjectReference to a Task
        :returns: 
        '''
        return self.delegate("ReconfigureDvs_Task")()
    
    def RectifyDvsHost_Task(self):
        '''Update the switch configuration on the host to bring them in sync with the
        current configuration in vCenter Server.
        :rtype: ManagedObjectReference to a Task
        :returns: 
        '''
        return self.delegate("RectifyDvsHost_Task")()
    
    def RefreshDVPortState(self):
        '''Refresh port states.
        :rtype: None
        :returns: 
        '''
        return self.delegate("RefreshDVPortState")()
    
    def UpdateDvsCapability(self):
        '''Set the capability of the switch.
        :rtype: None
        :returns: 
        '''
        return self.delegate("UpdateDvsCapability")()
    
    def UpdateNetworkResourcePool(self):
        '''Update the network resource pool configuration.
        :rtype: None
        :returns: 
        '''
        return self.delegate("UpdateNetworkResourcePool")()