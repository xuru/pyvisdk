
================================================================================
PortGroupProfile
================================================================================


.. describe:: Extended by
    
    :py:class:`~pyvisdk.do.host_port_group_profile.HostPortGroupProfile`,
    :py:class:`~pyvisdk.do.service_console_port_group_profile.ServiceConsolePortGroupProfile`,
    :py:class:`~pyvisdk.do.vm_port_group_profile.VmPortGroupProfile`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.network_policy_profile.NetworkPolicyProfile`,
    :py:class:`~pyvisdk.do.virtual_switch_selection_profile.VirtualSwitchSelectionProfile`,
    :py:class:`~pyvisdk.do.vlan_profile.VlanProfile`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.apply_profile.ApplyProfile`
    
.. class:: pyvisdk.do.port_group_profile.PortGroupProfile
    
    .. py:attribute:: key
    
        The linkable identifier.
        
    
    .. py:attribute:: name
    
        The name of the portgroup.
        
    
    .. py:attribute:: networkPolicy
    
        The network policy applicable on the port group.
        
    
    .. py:attribute:: vlan
    
        The vlan Id of the portGroup.
        
    
    .. py:attribute:: vswitch
    
        The virtual switch that the protgroup is connected to.
        
    