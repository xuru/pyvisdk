
================================================================================
HostDiskPartitionInfo
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_disk_partition_layout.HostDiskPartitionLayout`,
    :py:class:`~pyvisdk.do.host_disk_partition_spec.HostDiskPartitionSpec`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.compute_disk_partition_info.ComputeDiskPartitionInfo`,
    :py:meth:`~pyvisdk.do.compute_disk_partition_info_for_resize.ComputeDiskPartitionInfoForResize`,
    :py:meth:`~pyvisdk.do.retrieve_disk_partition_info.RetrieveDiskPartitionInfo`
    
.. class:: pyvisdk.do.host_disk_partition_info.HostDiskPartitionInfo
    
    .. py:attribute:: deviceName
    
        The device name of the disk to which this partition information corresponds.
        
    
    .. py:attribute:: layout
    
        A convenient format for describing disk layout. This layout specification can be converted to a Specification object.See ComputeDiskPartitionInfo
        
    
    .. py:attribute:: spec
    
        The detailed disk partition specification. Use this specification for manipulating the file system.See RetrieveDiskPartitionInfoSee UpdateDiskPartitions
        
    