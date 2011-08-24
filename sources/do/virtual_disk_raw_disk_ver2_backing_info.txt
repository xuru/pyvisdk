
================================================================================
VirtualDiskRawDiskVer2BackingInfo
================================================================================


.. describe:: Extended by
    
    :py:class:`~pyvisdk.do.virtual_disk_partitioned_raw_disk_ver2_backing_info.VirtualDiskPartitionedRawDiskVer2BackingInfo`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.virtual_device_device_backing_info.VirtualDeviceDeviceBackingInfo`
    
.. class:: pyvisdk.do.virtual_disk_raw_disk_ver2_backing_info.VirtualDiskRawDiskVer2BackingInfo
    
    .. py:attribute:: changeId
    
        The change ID of the virtual disk for the corresponding snapshot or virtual machine. This can be used to track incremental changes to a virtual disk. See QueryChangedDiskAreas.
        
    
    .. py:attribute:: descriptorFileName
    
        The name of the raw disk descriptor file.
        
    
    .. py:attribute:: uuid
    
        Disk UUID for the virtual disk, if available.
        
    