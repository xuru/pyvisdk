
================================================================================
HostUnresolvedVmfsResolutionSpec
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.resolve_multiple_unresolved_vmfs_volumes.ResolveMultipleUnresolvedVmfsVolumes`
    
.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_unresolved_vmfs_resolution_result.HostUnresolvedVmfsResolutionResult`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_unresolved_vmfs_resolution_spec.HostUnresolvedVmfsResolutionSpec
    
    .. py:attribute:: extentDevicePath
    
        List of device paths each specifying a VMFS extent.
        
    
    .. py:attribute:: uuidResolution
    
        When set to Resignature, new Uuid is assigned to the VMFS volume. When set to 'forceMount', existing uuid is assigned to the Vmfs volume and Vmfs volumes metadata doesn't change.See VmfsUuidResolution
        
    