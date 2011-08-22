
================================================================================
PhysicalNicSpec
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.physical_nic.PhysicalNic`,
    :py:class:`~pyvisdk.do.physical_nic_config.PhysicalNicConfig`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_ip_config.HostIpConfig`,
    :py:class:`~pyvisdk.do.physical_nic_link_info.PhysicalNicLinkInfo`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.physical_nic_spec.PhysicalNicSpec
    
    .. py:attribute:: ip
    
        The IP configuration on the physical network adapter (applies only to a hosted network adapter). The data object will be NULL on an ESX Server system.
        
    
    .. py:attribute:: linkSpeed
    
        The link speed and duplexity that this physical network adapter is currently configured to use. If this property is not set, the physical network adapter autonegotiates its proper settings.
        
    