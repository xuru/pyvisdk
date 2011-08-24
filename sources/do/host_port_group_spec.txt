
================================================================================
HostPortGroupSpec
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.add_port_group.AddPortGroup`,
    :py:meth:`~pyvisdk.do.update_port_group.UpdatePortGroup`
    
.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_port_group.HostPortGroup`,
    :py:class:`~pyvisdk.do.host_port_group_config.HostPortGroupConfig`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_network_policy.HostNetworkPolicy`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_port_group_spec.HostPortGroupSpec
    
    .. py:attribute:: name
    
        The name of the port group.
        
    
    .. py:attribute:: policy
    
        Policies on the port group take precedence over the ones specified on the virtual switch.
        
    
    .. py:attribute:: vlanId
    
        The VLAN ID for ports using this port group. Possible values: * A value of 0 specifies that you do not want the port group associated with a VLAN. * A value from 1 to 4094 specifies a VLAN ID for the port group. * A value of 4095 specifies that the port group should use trunk mode, which allows the guest operating system to manage its own VLAN tags.
        
    
    .. py:attribute:: vswitchName
    
        The identifier of the virtual switch on which this port group is located.
        
    