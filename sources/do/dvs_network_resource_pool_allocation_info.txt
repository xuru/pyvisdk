
================================================================================
DVSNetworkResourcePoolAllocationInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.dvs_network_resource_pool.DVSNetworkResourcePool`,
    :py:class:`~pyvisdk.do.dvs_network_resource_pool_config_spec.DVSNetworkResourcePoolConfigSpec`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.shares_info.SharesInfo`
    
.. describe:: Since
    
    vSphere API 4.1
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.dvs_network_resource_pool_allocation_info.DVSNetworkResourcePoolAllocationInfo
    
    .. py:attribute:: limit
    
        The maximum allowed usage for network clients belonging to this resource pool per host. The utilization of network clients belonging to this resource pool will not exceed the specified limit even if there are available network resources. If set to -1, then there is no limit on the network resource usage for clients belonging to this resource pool. Units are in Mbits/sec. When setting the allocation of a particular resource pool, if the property is unset, it is treated as no change and the property is not updated. An unset limit value while reading back the allocation information of a network resource pool indicates that there is no limit on the network resource usage for the clients belonging to this resource group.
        
    
    .. py:attribute:: shares
    
        The share settings associated with the network resource pool to facilitate proportional sharing of the physical network resources. If the property is unset when setting the allocation of a particular resource pool, it is treated as unset and the property is not updated. The property is always set when reading back the allocation information of a network resource pool.
        
    