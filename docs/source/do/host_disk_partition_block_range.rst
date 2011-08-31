
================================================================================
HostDiskPartitionBlockRange
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.compute_disk_partition_info_for_resize.ComputeDiskPartitionInfoForResize`
    
.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_disk_partition_layout.HostDiskPartitionLayout`,
    :py:class:`~pyvisdk.do.vmfs_datastore_multiple_extent_option.VmfsDatastoreMultipleExtentOption`,
    :py:class:`~pyvisdk.do.vmfs_datastore_single_extent_option.VmfsDatastoreSingleExtentOption`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_disk_dimensions_lba.HostDiskDimensionsLba`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_disk_partition_block_range.HostDiskPartitionBlockRange
    
    .. py:attribute:: end
    
        The end block address of the disk range. The block numbers start from zero. The range is inclusive of the end address.
        
    
    .. py:attribute:: partition
    
        Partition number. This number is a hint from the server indicating what the partition number for this block range is if the range corresponds to a partition. The partition number should correlate to the one in the partition specification. If sent back to the server, this property is ignored.
        
    
    .. py:attribute:: start
    
        The starting block address of the disk range. The block numbers start from zero. The range is inclusive of the end address.
        
    
    .. py:attribute:: type
    
        The type of data in the partition.See type
        
    