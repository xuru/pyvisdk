
================================================================================
VirtualDiskSparseVer1BackingInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.virtual_disk_sparse_ver1_backing_info.VirtualDiskSparseVer1BackingInfo`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.virtual_device_file_backing_info.VirtualDeviceFileBackingInfo`
    
.. class:: pyvisdk.do.virtual_disk_sparse_ver1_backing_info.VirtualDiskSparseVer1BackingInfo
    
    .. py:attribute:: contentId
    
        Content ID of the virtual disk file, if available.
        
    
    .. py:attribute:: diskMode
    
        The disk persistence mode. Valid values are: * persistent * nonpersistent * undoable * independent_persistent * independent_nonpersistent * append
        
    
    .. py:attribute:: parent
    
        The parent of this virtual disk file, if this is a delta disk backing. This will be unset if this is not a delta disk backing.
        
    
    .. py:attribute:: spaceUsedInKB
    
        The space in use for this sparse disk. This information is provided when retrieving configuration information for an existing virtual machine. The client cannot modify this information using reconfigure on a virtual machine.
        
    
    .. py:attribute:: split
    
        Flag to indicate the type of virtual disk file: split or monolithic. If true, the virtual disk is stored in multiple files, each 2GB.
        
    
    .. py:attribute:: writeThrough
    
        Flag to indicate whether writes should go directly to the file system or should be buffered.
        
    