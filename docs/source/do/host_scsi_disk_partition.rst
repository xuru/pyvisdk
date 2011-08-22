
================================================================================
HostScsiDiskPartition
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.attach_vmfs_extent.AttachVmfsExtent`,
    :py:meth:`~pyvisdk.do.compute_disk_partition_info_for_resize.ComputeDiskPartitionInfoForResize`,
    :py:meth:`~pyvisdk.do.expand_vmfs_extent.ExpandVmfsExtent`,
    :py:meth:`~pyvisdk.do.select_active_partition.SelectActivePartition`
    
.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_diagnostic_partition.HostDiagnosticPartition`,
    :py:class:`~pyvisdk.do.host_diagnostic_partition_create_spec.HostDiagnosticPartitionCreateSpec`,
    :py:class:`~pyvisdk.do.host_unresolved_vmfs_extent.HostUnresolvedVmfsExtent`,
    :py:class:`~pyvisdk.do.host_vmfs_spec.HostVmfsSpec`,
    :py:class:`~pyvisdk.do.host_vmfs_volume.HostVmfsVolume`,
    :py:class:`~pyvisdk.do.vmfs_datastore_create_spec.VmfsDatastoreCreateSpec`,
    :py:class:`~pyvisdk.do.vmfs_datastore_expand_spec.VmfsDatastoreExpandSpec`,
    :py:class:`~pyvisdk.do.vmfs_datastore_extend_spec.VmfsDatastoreExtendSpec`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_scsi_disk_partition.HostScsiDiskPartition
    
    .. py:attribute:: diskName
    
        The SCSI disk device on which a VMware File System (VMFS) extent resides.
        
    
    .. py:attribute:: partition
    
        The partition number of the partition on the ScsiDisk.
        
    