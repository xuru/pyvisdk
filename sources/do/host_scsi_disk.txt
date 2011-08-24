
================================================================================
HostScsiDisk
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_diagnostic_partition_create_option.HostDiagnosticPartitionCreateOption`,
    :py:class:`~pyvisdk.do.virtual_machine_scsi_disk_device_info.VirtualMachineScsiDiskDeviceInfo`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_disk_dimensions_lba.HostDiskDimensionsLba`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.scsi_lun.ScsiLun`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.query_available_disks_for_vmfs.QueryAvailableDisksForVmfs`
    
.. class:: pyvisdk.do.host_scsi_disk.HostScsiDisk
    
    .. py:attribute:: capacity
    
        The size of SCSI disk using the Logical Block Addressing scheme.
        
    
    .. py:attribute:: devicePath
    
        The device path of the ScsiDisk. This device path is a file path that can be opened to create partitions on the disk.
        
    