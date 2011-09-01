
================================================================================
VirtualDiskSparseVer2BackingInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.virtual_disk_sparse_ver2_backing_info.VirtualDiskSparseVer2BackingInfo`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.virtual_device_file_backing_info.VirtualDeviceFileBackingInfo`
    
.. class:: pyvisdk.do.virtual_disk_sparse_ver2_backing_info.VirtualDiskSparseVer2BackingInfo
    
    .. py:attribute:: changeId
    
        The change ID of the virtual disk for the corresponding snapshot or virtual machine. This can be used to track incremental changes to a virtual disk. See QueryChangedDiskAreas.
        
    
    .. py:attribute:: contentId
    
        Content ID of the virtual disk file, if available.
        
    
    .. py:attribute:: diskMode
    
        The disk persistence mode. Valid modes are: * persistent * independent_persistent * independent_nonpersistent See VirtualDiskMode
        
    
    .. py:attribute:: parent
    
        The parent of this virtual disk file, if this is a delta disk backing. This will be unset if this is not a delta disk backing.
        
    
    .. py:attribute:: spaceUsedInKB
    
        The space in use for this sparse disk. This information is provided when retrieving configuration information for an exisiting virtual machine. The client cannot modify this information using reconfigure on a virtual machine.
        
    
    .. py:attribute:: split
    
        Flag to indicate the type of virtual disk file: split or monolithic. If true, the virtual disk is stored in multiple files, each 2GB.
        
    
    .. py:attribute:: uuid
    
        Disk UUID for the virtual disk, if available.
        
    
    .. py:attribute:: writeThrough
    
        Flag to indicate whether writes should go directly to the file system or should be buffered.
        
    