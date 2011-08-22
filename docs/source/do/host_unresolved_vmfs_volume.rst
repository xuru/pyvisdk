
================================================================================
HostUnresolvedVmfsVolume
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_unresolved_vmfs_extent.HostUnresolvedVmfsExtent`,
    :py:class:`~pyvisdk.do.host_unresolved_vmfs_volume_resolve_status.HostUnresolvedVmfsVolumeResolveStatus`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.query_unresolved_vmfs_volume.QueryUnresolvedVmfsVolume`,
    :py:meth:`~pyvisdk.do.query_unresolved_vmfs_volumes.QueryUnresolvedVmfsVolumes`
    
.. class:: pyvisdk.do.host_unresolved_vmfs_volume.HostUnresolvedVmfsVolume
    
    .. py:attribute:: extent
    
        List of detected copies of VMFS extents.
        
    
    .. py:attribute:: resolveStatus
    
        Information related to how the volume might be resolved.
        
    
    .. py:attribute:: totalBlocks
    
        Total number of blocks in this volume.
        
    
    .. py:attribute:: vmfsLabel
    
        The detected VMFS label name
        
    
    .. py:attribute:: vmfsUuid
    
        The detected VMFS UUID
        
    