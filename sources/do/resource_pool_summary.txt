
================================================================================
ResourcePoolSummary
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.resource_pool.ResourcePool`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.resource_config_spec.ResourceConfigSpec`,
    :py:class:`~pyvisdk.do.resource_pool_quick_stats.ResourcePoolQuickStats`,
    :py:class:`~pyvisdk.do.resource_pool_runtime_info.ResourcePoolRuntimeInfo`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Extended by
    
    :py:class:`~pyvisdk.do.virtual_app_summary.VirtualAppSummary`
    
.. class:: pyvisdk.do.resource_pool_summary.ResourcePoolSummary
    
    .. py:attribute:: config
    
        Current configuration of the resource pool.
        
    
    .. py:attribute:: configuredMemoryMB
    
        Total configured memory of all virtual machines in the resource pool, in MB.
        
    
    .. py:attribute:: name
    
        Name of resource pool.
        
    
    .. py:attribute:: quickStats
    
        A set of statistics that are typically updated with near real-time regularity. This data object type does not support notification, for scalability reasons. Therefore, changes in QuickStats do not generate property collector updates. To monitor statistics values, use the statistics and alarms modules instead.
        
    
    .. py:attribute:: runtime
    
        Current runtime state of the resource pool.
        
    