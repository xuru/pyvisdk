
================================================================================
HostPatchManagerPatchManagerOperationSpec
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.check_host_patch__task.CheckHostPatch_Task`,
    :py:meth:`~pyvisdk.do.install_host_patch_v2__task.InstallHostPatchV2_Task`,
    :py:meth:`~pyvisdk.do.query_host_patch__task.QueryHostPatch_Task`,
    :py:meth:`~pyvisdk.do.scan_host_patch_v2__task.ScanHostPatchV2_Task`,
    :py:meth:`~pyvisdk.do.stage_host_patch__task.StageHostPatch_Task`,
    :py:meth:`~pyvisdk.do.uninstall_host_patch__task.UninstallHostPatch_Task`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_patch_manager_patch_manager_operation_spec.HostPatchManagerPatchManagerOperationSpec
    
    .. py:attribute:: cmdOption
    
        Possible command line options when calling esxupdate.
        
    
    .. py:attribute:: password
    
        The password used for the proxy server. This is passed with ssl through a trusted channel.
        
    
    .. py:attribute:: port
    
        The port of the possible proxy for esxupdate to use to connect to a server. The patch and metadata may be cached within the proxy server.
        
    
    .. py:attribute:: proxy
    
        The name of the possible proxy for esxupdate to use to connect to a server. The patch and metadata may be cached within the proxy server.
        
    
    .. py:attribute:: userName
    
        The user name used for the proxy server.
        
    