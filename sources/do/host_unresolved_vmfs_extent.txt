
================================================================================
HostUnresolvedVmfsExtent
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_unresolved_vmfs_volume.HostUnresolvedVmfsVolume`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_scsi_disk_partition.HostScsiDiskPartition`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_unresolved_vmfs_extent.HostUnresolvedVmfsExtent
    
    .. py:attribute:: device
    
        The device information
        
    
    .. py:attribute:: devicePath
    
        The device path of an VMFS extent
        
    
    .. py:attribute:: endBlock
    
        Index of the last block that this extent provides.
        
    
    .. py:attribute:: isHeadExtent
    
        Is this a copy of the head extent of the VMFS volume?
        
    
    .. py:attribute:: ordinal
    
        A number indicating the order of an extent in a volume. An extent with a lower ordinal value than another extent provides a range of blocks to a volume at an earlier block address range. Extents with the same ordinal provide the same range of blocks to a volume. A zero ordinal indicates that the extent is a head extent.
        
    
    .. py:attribute:: reason
    
        Reason as to why the partition is marked as copy of a VMFS volume's extent. Possible reasons are the disk id is not matching with what the scsi inq is saying or disk uuid is not matching
        
    
    .. py:attribute:: startBlock
    
        Index of the first block that this extent provides.
        
    
    .. py:attribute:: vmfsUuid
    
        The UUID of the VMFS volume read from to the partition.
        
    