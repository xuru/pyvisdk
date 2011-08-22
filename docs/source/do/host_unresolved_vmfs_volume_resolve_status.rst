
================================================================================
HostUnresolvedVmfsVolumeResolveStatus
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_unresolved_vmfs_volume.HostUnresolvedVmfsVolume`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_unresolved_vmfs_volume_resolve_status.HostUnresolvedVmfsVolumeResolveStatus
    
    .. py:attribute:: incompleteExtents
    
        Is the list of extents for the volume a partial list? A volume can only be resignatured if all extents composing that volume are available. Hence, a volume with a partial extent list cannot be resignatured.
        
    
    .. py:attribute:: multipleCopies
    
        Are there multiple copies of extents for this volume? If any extent of the volume has multiple copies then the extents to be resolved must be explicitly specified when resolving this volume.
        
    
    .. py:attribute:: resolvable
    
        Can this volume be resolved? There may be other reasons a volume cannot be resolved other than the fact that it is incomplete. This boolean will authoritatively indicate if the server can resolve this volume.
        
    