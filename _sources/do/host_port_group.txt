
================================================================================
HostPortGroup
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_network_info.HostNetworkInfo`,
    :py:class:`~pyvisdk.do.host_virtual_switch.HostVirtualSwitch`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_network_policy.HostNetworkPolicy`,
    :py:class:`~pyvisdk.do.host_port_group_port.HostPortGroupPort`,
    :py:class:`~pyvisdk.do.host_port_group_spec.HostPortGroupSpec`,
    :py:class:`~pyvisdk.do.host_virtual_switch.HostVirtualSwitch`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_port_group.HostPortGroup
    
    .. py:attribute:: computedPolicy
    
        Computed network policies that are applicable for a port group. The inheritance scheme for PortGroup requires knowledge about the NetworkPolicy for a port group and its parent virtual switch as well as the logic for computing the results. This information is provided as a convenience so that callers need not duplicate the inheritance logic to determine the proper values for a network policy.
        
    
    .. py:attribute:: key
    
        The linkable identifier.
        
    
    .. py:attribute:: port
    
        The ports that currently exist and are used on this port group.
        
    
    .. py:attribute:: spec
    
        The specification of a port group.
        
    
    .. py:attribute:: vswitch
    
        The virtual switch that contains this port group.
        
    