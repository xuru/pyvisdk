
================================================================================
VirtualDiskFlatVer2BackingInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.virtual_disk_flat_ver2_backing_info.VirtualDiskFlatVer2BackingInfo`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.virtual_device_file_backing_info.VirtualDeviceFileBackingInfo`
    
.. class:: pyvisdk.do.virtual_disk_flat_ver2_backing_info.VirtualDiskFlatVer2BackingInfo
    
    .. py:attribute:: changeId
    
        The change ID of the virtual disk for the corresponding snapshot or virtual machine. This can be used to track incremental changes to a virtual disk. See QueryChangedDiskAreas.
        
    
    .. py:attribute:: contentId
    
        Content ID of the virtual disk file, if available.
        
    
    .. py:attribute:: diskMode
    
        The disk persistence mode. Valid modes are: * persistent * independent_persistent * independent_nonpersistent * nonpersistent * undoable * append
        
    
    .. py:attribute:: eagerlyScrub
    
        Flag to indicate to the underlying filesystem whether the virtual disk backing file should be scrubbed completely at this time.
        
    
    .. py:attribute:: parent
    
        The parent of this virtual disk file, if this is a delta disk backing. This will be unset if this is not a delta disk backing.
        
    
    .. py:attribute:: split
    
        Flag to indicate the type of virtual disk file: split or monolithic. If true, the virtual disk is stored in multiple files, each 2GB.
        
    
    .. py:attribute:: thinProvisioned
    
        Flag to indicate to the underlying filesystem, whether the virtual disk backing file should be allocated lazily (using thin provisioning). This flag is only used for file systems that support configuring the provisioning policy on a per file basis, such as VMFS3.
        
    
    .. py:attribute:: uuid
    
        Disk UUID for the virtual disk, if available.
        
    
    .. py:attribute:: writeThrough
    
        Flag to indicate whether writes should go directly to the file system or should be buffered.
        
    