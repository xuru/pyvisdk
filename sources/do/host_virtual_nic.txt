
================================================================================
HostVirtualNic
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_network_info.HostNetworkInfo`,
    :py:class:`~pyvisdk.do.host_v_motion_net_config.HostVMotionNetConfig`,
    :py:class:`~pyvisdk.do.virtual_nic_manager_net_config.VirtualNicManagerNetConfig`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_port_group_port.HostPortGroupPort`,
    :py:class:`~pyvisdk.do.host_virtual_nic_spec.HostVirtualNicSpec`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_virtual_nic.HostVirtualNic
    
    .. py:attribute:: device
    
        Device name.
        
    
    .. py:attribute:: key
    
        The linkable identifier.
        
    
    .. py:attribute:: port
    
        The port on the port group that the virtual network adapter is using when it is enabled.
        
    
    .. py:attribute:: portgroup
    
        If the vnic is connecting to a vSwitch, this property is the name of portgroup connected. If the vnic is connecting to a DistributedVirtualSwitch, this property is an empty string.
        
    
    .. py:attribute:: spec
    
        The configurable properties for the virtual network adapter object.
        
    