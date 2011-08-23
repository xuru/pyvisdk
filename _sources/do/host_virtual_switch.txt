
================================================================================
HostVirtualSwitch
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_network_info.HostNetworkInfo`,
    :py:class:`~pyvisdk.do.host_port_group.HostPortGroup`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_port_group.HostPortGroup`,
    :py:class:`~pyvisdk.do.host_virtual_switch_spec.HostVirtualSwitchSpec`,
    :py:class:`~pyvisdk.do.physical_nic.PhysicalNic`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_virtual_switch.HostVirtualSwitch
    
    .. py:attribute:: key
    
        The virtual switch key.
        
    
    .. py:attribute:: mtu
    
        The maximum transmission unit (MTU) associated with this virtual switch in bytes.
        
    
    .. py:attribute:: name
    
        The name of the virtual switch. Maximum length is 32 characters.
        
    
    .. py:attribute:: numPorts
    
        The number of ports that this virtual switch currently has.
        
    
    .. py:attribute:: numPortsAvailable
    
        The number of ports that are available on this virtual switch. There are a number of networking services that utilize a port on the virtual switch and are not accounted for in the Port array of a PortGroup. For example, each physical NIC attached to a virtual switch consumes one port. This property should be used when attempting to implement admission control for new services attaching to virtual switches.
        
    
    .. py:attribute:: pnic
    
        The set of physical network adapters associated with this bridge.
        
    
    .. py:attribute:: portgroup
    
        The list of port groups configured for this virtual switch.
        
    
    .. py:attribute:: spec
    
        The specification of a PortGroup.
        
    