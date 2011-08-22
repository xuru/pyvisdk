
================================================================================
VirtualDeviceFileBackingInfo
================================================================================


.. describe:: Extended by
    
    :py:class:`~pyvisdk.do.virtual_cdrom_iso_backing_info.VirtualCdromIsoBackingInfo`,
    :py:class:`~pyvisdk.do.virtual_disk_flat_ver1_backing_info.VirtualDiskFlatVer1BackingInfo`,
    :py:class:`~pyvisdk.do.virtual_disk_flat_ver2_backing_info.VirtualDiskFlatVer2BackingInfo`,
    :py:class:`~pyvisdk.do.virtual_disk_raw_disk_mapping_ver1_backing_info.VirtualDiskRawDiskMappingVer1BackingInfo`,
    :py:class:`~pyvisdk.do.virtual_disk_sparse_ver1_backing_info.VirtualDiskSparseVer1BackingInfo`,
    :py:class:`~pyvisdk.do.virtual_disk_sparse_ver2_backing_info.VirtualDiskSparseVer2BackingInfo`,
    :py:class:`~pyvisdk.do.virtual_floppy_image_backing_info.VirtualFloppyImageBackingInfo`,
    :py:class:`~pyvisdk.do.virtual_parallel_port_file_backing_info.VirtualParallelPortFileBackingInfo`,
    :py:class:`~pyvisdk.do.virtual_serial_port_file_backing_info.VirtualSerialPortFileBackingInfo`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.datastore.Datastore`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.virtual_device_backing_info.VirtualDeviceBackingInfo`
    
.. class:: pyvisdk.do.virtual_device_file_backing_info.VirtualDeviceFileBackingInfo
    
    .. py:attribute:: datastore
    
        Reference to the datastore managed object where this file is stored. If the file is not located on a datastore, then this reference is null. This is not used for configuration.
        
    
    .. py:attribute:: fileName
    
        Filename for the host file used in this backing.
        
    