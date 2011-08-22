
================================================================================
HostVirtualSwitchSpec
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.add_virtual_switch.AddVirtualSwitch`,
    :py:meth:`~pyvisdk.do.update_virtual_switch.UpdateVirtualSwitch`
    
.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_virtual_switch.HostVirtualSwitch`,
    :py:class:`~pyvisdk.do.host_virtual_switch_config.HostVirtualSwitchConfig`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_network_policy.HostNetworkPolicy`,
    :py:class:`~pyvisdk.do.host_virtual_switch_bridge.HostVirtualSwitchBridge`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_virtual_switch_spec.HostVirtualSwitchSpec
    
    .. py:attribute:: bridge
    
        The bridge specification describes how physical network adapters can be bridged to a virtual switch.
        
    
    .. py:attribute:: mtu
    
        The maximum transmission unit (MTU) of the virtual switch in bytes.
        
    
    .. py:attribute:: numPorts
    
        The number of ports that this virtual switch is configured to use. Changing this setting does not take effect until the next reboot. The maximum value is 1024, although other constraints, such as memory limits, may establish a lower effective limit.
        
    
    .. py:attribute:: policy
    
        The virtual switch policy specification. This has a lower precedence than PortGroup. If the policy property is not set and you are creating a virtual switch, then a default policy property setting is used. If the policy property is not set and you are updating a virtual switch, then the policy will be unchanged.
        
    