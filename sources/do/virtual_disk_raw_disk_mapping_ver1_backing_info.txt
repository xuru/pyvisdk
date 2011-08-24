
================================================================================
VirtualDiskRawDiskMappingVer1BackingInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.virtual_disk_raw_disk_mapping_ver1_backing_info.VirtualDiskRawDiskMappingVer1BackingInfo`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.virtual_device_file_backing_info.VirtualDeviceFileBackingInfo`
    
.. class:: pyvisdk.do.virtual_disk_raw_disk_mapping_ver1_backing_info.VirtualDiskRawDiskMappingVer1BackingInfo
    
    .. py:attribute:: changeId
    
        The change ID of the virtual disk for the corresponding snapshot or virtual machine. This can be used to track incremental changes to a virtual disk. See QueryChangedDiskAreas.
        
    
    .. py:attribute:: compatibilityMode
    
        The compatibility mode of the raw disk mapping (RDM). This must be specified when a new virtual disk with an RDM backing is created. On subsequent virtual machine reconfigurations, this property should be handled as follows, depending on the version of the host:
        
    
    .. py:attribute:: contentId
    
        Content ID of the virtual disk file, if available.
        
    
    .. py:attribute:: deviceName
    
        The host-specific device the LUN is being accessed through. If the target LUN is not available on the host then it is empty. For example, this could happen if it has accidentally been masked out.
        
    
    .. py:attribute:: diskMode
    
        The disk mode. Valid values are: * persistent * independent_persistent * independent_nonpersistent * nonpersistent * undoable * append
        
    
    .. py:attribute:: lunUuid
    
        Unique identifier of the LUN accessed by the raw disk mapping.
        
    
    .. py:attribute:: parent
    
        The parent of this virtual disk file, if this is a delta disk backing. This will be unset if this is not a delta disk backing.
        
    
    .. py:attribute:: uuid
    
        Disk UUID for the virtual disk, if available. Disk UUID is not available if the raw disk mapping is in physical compatibility mode.
        
    