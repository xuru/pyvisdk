
================================================================================
DiagnosticManagerBundleInfo
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_system.HostSystem`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.generate_log_bundles__task.GenerateLogBundles_Task`
    
.. class:: pyvisdk.do.diagnostic_manager_bundle_info.DiagnosticManagerBundleInfo
    
    .. py:attribute:: system
    
        The host to which this diagnostic bundle belongs. If this is for the default server, then it is not set.
        
    
    .. py:attribute:: url
    
        The location from which the diagnostic bundle can be downloaded. The host part of the URL is returned as '*' if the hostname to be used is the name of the server to which the call was made. For example, if the call is made to vcsrv1.domain1.com, and the bundle is available for download from http://vcsrv1.domain1.com/diagnostics/bundle.zip, the URL returned may be http:// * /diagnostics/bundle.zip. The client replaces the asterisk with the server name on which it invoked the call.
        
    