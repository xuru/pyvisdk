
================================================================================
VirtualDiskFlatVer1BackingInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.virtual_disk_flat_ver1_backing_info.VirtualDiskFlatVer1BackingInfo`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.virtual_device_file_backing_info.VirtualDeviceFileBackingInfo`
    
.. class:: pyvisdk.do.virtual_disk_flat_ver1_backing_info.VirtualDiskFlatVer1BackingInfo
    
    .. py:attribute:: contentId
    
        Content ID of the virtual disk file, if available.
        
    
    .. py:attribute:: diskMode
    
        The disk persistence mode. Valid modes are: * persistent * nonpersistent * undoable
        
    
    .. py:attribute:: parent
    
        The parent of this virtual disk file, if this is a delta disk backing. This will be unset if this is not a delta disk backing.
        
    
    .. py:attribute:: split
    
        Flag to indicate the type of virtual disk file: split or monolithic. If true, the virtual disk is stored in multiple files, each 2GB.
        
    
    .. py:attribute:: writeThrough
    
        Flag to indicate whether writes should go directly to the file system or should be buffered.
        
    