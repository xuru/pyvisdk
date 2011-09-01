
================================================================================
HostDiskPartitionAttributes
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_disk_partition_spec.HostDiskPartitionSpec`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_disk_partition_attributes.HostDiskPartitionAttributes
    
    .. py:attribute:: attributes
    
        The attributes on the partition.
        
    
    .. py:attribute:: endSector
    
        The end sector.
        
    
    .. py:attribute:: logical
    
        The flag to indicate whether or not the partition is logical. If true, the partition number should be greater than 4.
        
    
    .. py:attribute:: partition
    
        The partition number. Must be a positive integer.
        
    
    .. py:attribute:: startSector
    
        The start sector.
        
    
    .. py:attribute:: type
    
        Type of data in the partition. If it is a well-known partition type, it will be one of the defined types. If it is not, then it will be reported as a hexadecimal number. For example, "none", "vmfs", "linux", and "0x20" are all valid values.See HostDiskPartitionInfoType
        
    