
================================================================================
StorageIOAllocationInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.virtual_disk.VirtualDisk`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.shares_info.SharesInfo`
    
.. describe:: Since
    
    vSphere API 4.1
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.storage_io_allocation_info.StorageIOAllocationInfo
    
    .. py:attribute:: limit
    
        The utilization of a virtual machine will not exceed this limit, even if there are available resources. This is typically used to ensure a consistent performance of virtual machines independent of available resources. If set to -1, then there is no fixed limit on resource usage (only bounded by available resources and shares). The unit is number of I/O per second. While setting the limit for storage I/O resource, if the property is unset, it is treated as no change and the property is not updated. While reading back the limit information of storage I/O resource, if the property is unset, a default value of -1 will be returned, which indicates that there is no limit on resource usage.
        
    
    .. py:attribute:: shares
    
        Shares are used in case of resource contention. The value should be within a range of 200 to 4000. While setting shares for storage I/O resource, if the property is unset, it is treated as no change and the property is not updated. While reading back the shares information of storage I/O resource, if the property is unset, a default value of level = normal, shares = 1000 will be returned.
        
    