
================================================================================
HostPatchManagerResult
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_patch_manager_status.HostPatchManagerStatus`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.check_host_patch__task.CheckHostPatch_Task`,
    :py:meth:`~pyvisdk.do.install_host_patch_v2__task.InstallHostPatchV2_Task`,
    :py:meth:`~pyvisdk.do.query_host_patch__task.QueryHostPatch_Task`,
    :py:meth:`~pyvisdk.do.scan_host_patch_v2__task.ScanHostPatchV2_Task`,
    :py:meth:`~pyvisdk.do.stage_host_patch__task.StageHostPatch_Task`,
    :py:meth:`~pyvisdk.do.uninstall_host_patch__task.UninstallHostPatch_Task`
    
.. class:: pyvisdk.do.host_patch_manager_result.HostPatchManagerResult
    
    .. py:attribute:: status
    
        The scan results for each patch.
        
    
    .. py:attribute:: version
    
        The version of the scan result schema.
        
    
    .. py:attribute:: xmlResult
    
        The scan results in XML format.
        
    