
================================================================================
HostResignatureRescanResult
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.datastore.Datastore`,
    :py:class:`~pyvisdk.do.host_vmfs_rescan_result.HostVmfsRescanResult`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.resignature_unresolved_vmfs_volume__task.ResignatureUnresolvedVmfsVolume_Task`
    
.. class:: pyvisdk.do.host_resignature_rescan_result.HostResignatureRescanResult
    
    .. py:attribute:: rescan
    
        List of VMFS Rescan operation results
        
    
    .. py:attribute:: result
    
        When an UnresolvedVmfsVolume has been resignatured, we want to return the newly created VMFS Datastore.
        
    