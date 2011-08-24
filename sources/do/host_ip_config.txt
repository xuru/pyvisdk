
================================================================================
HostIpConfig
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.update_ip_config.UpdateIpConfig`
    
.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_virtual_nic_spec.HostVirtualNicSpec`,
    :py:class:`~pyvisdk.do.host_v_motion_info.HostVMotionInfo`,
    :py:class:`~pyvisdk.do.host_v_motion_system.HostVMotionSystem`,
    :py:class:`~pyvisdk.do.physical_nic_spec.PhysicalNicSpec`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_ip_config_ip_v6_address_configuration.HostIpConfigIpV6AddressConfiguration`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_ip_config.HostIpConfig
    
    .. py:attribute:: dhcp
    
        The flag to indicate whether or not DHCP (dynamic host control protocol) is enabled. If this property is set to true, the ipAddress and the subnetMask strings cannot be set explicitly.
        
    
    .. py:attribute:: ipAddress
    
        The IP address currently used by the network adapter. All IP addresses are specified using IPv4 dot notation. For example, "192.168.0.1". Subnet addresses and netmasks are specified using the same notation.
        
    
    .. py:attribute:: ipV6Config
    
        The ipv6 configuration
        
    
    .. py:attribute:: subnetMask
    
        The subnet mask.
        
    