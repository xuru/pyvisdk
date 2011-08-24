
================================================================================
HostVirtualNicSpec
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.add_service_console_virtual_nic.AddServiceConsoleVirtualNic`,
    :py:meth:`~pyvisdk.do.add_virtual_nic.AddVirtualNic`,
    :py:meth:`~pyvisdk.do.update_service_console_virtual_nic.UpdateServiceConsoleVirtualNic`,
    :py:meth:`~pyvisdk.do.update_virtual_nic.UpdateVirtualNic`
    
.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_virtual_nic.HostVirtualNic`,
    :py:class:`~pyvisdk.do.host_virtual_nic_config.HostVirtualNicConfig`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.distributed_virtual_switch_port_connection.DistributedVirtualSwitchPortConnection`,
    :py:class:`~pyvisdk.do.host_ip_config.HostIpConfig`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_virtual_nic_spec.HostVirtualNicSpec
    
    .. py:attribute:: distributedVirtualPort
    
        The DistributedVirtualPort that is connected to the vnic.
        
    
    .. py:attribute:: ip
    
        The IP configuration on the virtual network adapter.
        
    
    .. py:attribute:: mac
    
        The media access control (MAC) address of the virtual network adapter.
        
    
    .. py:attribute:: mtu
    
        The maximum transmission unit for packets size in bytes for the virtual nic. This property is applicable to vmkernel virtual nics and will be ignored if specified for service console virtual nics. If not specified, the system default value shall be used.
        
    
    .. py:attribute:: portgroup
    
        The Portgroup to which the Vnic connects. While reconfiguring a virtual nic, this field indicates the new portgroup the virtualnic should connect to. This can be specified only if distributedVirtualPort is not specified.
        
    
    .. py:attribute:: tsoEnabled
    
        Flag enabling or disabling tcp segmentation offset for a virtual nic. This property is applicable to vmkernel virtual nics and will be ignored if specified for service console vitual nics. If not specified, a default value of true shall be used.
        
    