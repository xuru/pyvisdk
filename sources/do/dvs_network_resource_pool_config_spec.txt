
================================================================================
DVSNetworkResourcePoolConfigSpec
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.update_network_resource_pool.UpdateNetworkResourcePool`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.dvs_network_resource_pool_allocation_info.DVSNetworkResourcePoolAllocationInfo`
    
.. describe:: Since
    
    vSphere API 4.1
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.dvs_network_resource_pool_config_spec.DVSNetworkResourcePoolConfigSpec
    
    .. py:attribute:: allocationInfo
    
        The network resource allocation for the network resource pool.
        
    
    .. py:attribute:: configVersion
    
        The configVersion is a unique identifier for a given version of the configuration. Each change to the configuration will update this value. This is typically implemented as a non-decreasing count or a time-stamp. However, a client should always treat this as an opaque string.
        
    
    .. py:attribute:: key
    
        The key of the network resource pool.
        
    