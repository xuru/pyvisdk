
================================================================================
HostDiskPartitionSpec
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.update_disk_partitions.UpdateDiskPartitions`
    
.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_diagnostic_partition_create_spec.HostDiagnosticPartitionCreateSpec`,
    :py:class:`~pyvisdk.do.host_disk_partition_info.HostDiskPartitionInfo`,
    :py:class:`~pyvisdk.do.vmfs_datastore_create_spec.VmfsDatastoreCreateSpec`,
    :py:class:`~pyvisdk.do.vmfs_datastore_expand_spec.VmfsDatastoreExpandSpec`,
    :py:class:`~pyvisdk.do.vmfs_datastore_extend_spec.VmfsDatastoreExtendSpec`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_disk_dimensions_chs.HostDiskDimensionsChs`,
    :py:class:`~pyvisdk.do.host_disk_partition_attributes.HostDiskPartitionAttributes`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_disk_partition_spec.HostDiskPartitionSpec
    
    .. py:attribute:: chs
    
        Disk dimensions expressed as cylinder, head, sector (CHS) coordinates.
        
    
    .. py:attribute:: partition
    
        List of partitions on the disk.
        
    
    .. py:attribute:: totalSectors
    
        Disk dimensions expressed in total number of 512-byte sectors.
        
    