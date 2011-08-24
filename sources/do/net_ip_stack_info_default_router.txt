
================================================================================
NetIpStackInfoDefaultRouter
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.net_ip_stack_info.NetIpStackInfo`
    
.. describe:: Since
    
    vSphere API 4.1
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.net_ip_stack_info_default_router.NetIpStackInfoDefaultRouter
    
    .. py:attribute:: device
    
        This value will contain the name of the interface as reported by the operationg system.
        
    
    .. py:attribute:: ipAddress
    
        Unicast IP address of a next-hop router.
        
    
    .. py:attribute:: lifetime
    
        When this entry will no longer valid. For IPv6 this value see For IPv6 RFC 2462 sections 4.2 and 6.3.4.
        
    
    .. py:attribute:: preference
    
        Value of this entry compared to others that this IP stack uses when making selection to route traffic on the default route when there are multiple default routers. Value must be one of NetIpStackInfoPreference
        
    