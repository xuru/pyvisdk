
================================================================================
HostUnresolvedVmfsResolutionResult
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_unresolved_vmfs_resolution_spec.HostUnresolvedVmfsResolutionSpec`,
    :py:class:`~pyvisdk.do.host_vmfs_volume.HostVmfsVolume`,
    :py:class:`~pyvisdk.do.localized_method_fault.LocalizedMethodFault`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.resolve_multiple_unresolved_vmfs_volumes.ResolveMultipleUnresolvedVmfsVolumes`
    
.. class:: pyvisdk.do.host_unresolved_vmfs_resolution_result.HostUnresolvedVmfsResolutionResult
    
    .. py:attribute:: fault
    
        'fault' would be set if the operation was not successful
        
    
    .. py:attribute:: spec
    
        The original UnresolvedVmfsResolutionSpec which user had specified
        
    
    .. py:attribute:: vmfs
    
        Newly created VmfsVolume
        
    