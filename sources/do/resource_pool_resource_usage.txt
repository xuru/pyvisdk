
================================================================================
ResourcePoolResourceUsage
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.resource_pool_runtime_info.ResourcePoolRuntimeInfo`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.resource_pool_resource_usage.ResourcePoolResourceUsage
    
    .. py:attribute:: maxUsage
    
        Current upper-bound on usage. The upper-bound is based on the limit configured on this resource pool, as well as limits configured on any parent resource pool.
        
    
    .. py:attribute:: overallUsage
    
        Close to real-time resource usage of all running child virtual machines, including virtual machines in child resource pools.
        
    
    .. py:attribute:: reservationUsed
    
        Total amount of resources that have been used to satisfy the reservation requirements of all descendants of this resource pool (includes both resource pools and virtual machines).
        
    
    .. py:attribute:: reservationUsedForVm
    
        Total amount of resources that have been used to satisfy the reservation requirements of running virtual machines in this resource pool or any of its child resource pools.
        
    
    .. py:attribute:: unreservedForPool
    
        Total amount of resources available to satisfy a reservation for a child resource pool. In the undercommitted state, this is limited by the capacity at the root node. In the overcommitted case, this could be higher since we do not perform the dynamic capacity checks.
        
    
    .. py:attribute:: unreservedForVm
    
        Total amount of resources available to satisfy a reservation for a child virtual machine. In general, this should be the same as unreservedForPool. However, in the overcommitted case, this is limited by the remaining available resources at the root node.
        
    