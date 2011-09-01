
================================================================================
VirtualDiskSpec
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.copy_virtual_disk__task.CopyVirtualDisk_Task`,
    :py:meth:`~pyvisdk.do.create_virtual_disk__task.CreateVirtualDisk_Task`
    
.. describe:: Extended by
    
    :py:class:`~pyvisdk.do.device_backed_virtual_disk_spec.DeviceBackedVirtualDiskSpec`,
    :py:class:`~pyvisdk.do.file_backed_virtual_disk_spec.FileBackedVirtualDiskSpec`
    
.. describe:: Since
    
    VI API 2.5
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.virtual_disk_spec.VirtualDiskSpec
    
    .. py:attribute:: adapterType
    
        The type of the virtual disk adapter for the new virtual disk.See VirtualDiskAdapterType
        
    
    .. py:attribute:: diskType
    
        The type of the new virtual disk.See VirtualDiskType
        
    