
================================================================================
NetIpStackInfo
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.net_ip_stack_info_default_router.NetIpStackInfoDefaultRouter`,
    :py:class:`~pyvisdk.do.net_ip_stack_info_net_to_media.NetIpStackInfoNetToMedia`
    
.. describe:: Since
    
    vSphere API 4.1
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.net_ip_stack_info.NetIpStackInfo
    
    .. py:attribute:: defaultRouter
    
        Zero one or more entries of discovered IP routers that are directly reachable from a an interface on this system. This property maps to RFC 4293 ipDefaultRouterTable.
        
    
    .. py:attribute:: neighbor
    
        Zero, one or more entries of neighbors discovered using ARP or NDP. This information is used to help diagnose connectivity or performance issues. This property maps to RFC 4293 ipNetToPhysicalTable.
        
    