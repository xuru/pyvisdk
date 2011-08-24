
================================================================================
SharesInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.dvs_network_resource_pool_allocation_info.DVSNetworkResourcePoolAllocationInfo`,
    :py:class:`~pyvisdk.do.resource_allocation_info.ResourceAllocationInfo`,
    :py:class:`~pyvisdk.do.storage_io_allocation_info.StorageIOAllocationInfo`,
    :py:class:`~pyvisdk.do.virtual_disk.VirtualDisk`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.shares_level.SharesLevel`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.shares_info.SharesInfo
    
    .. py:attribute:: level
    
        The allocation level. The level is a simplified view of shares. Levels map to a pre-determined set of numeric values for shares. If the shares value does not map to a predefined size, then the level is set as custom.
        
    
    .. py:attribute:: shares
    
        The number of shares allocated. Used to determine resource allocation in case of resource contention. This value is only set if level is set to custom. If level is not set to custom, this value is ignored. Therefore, only shares with custom values can be compared.
        
    