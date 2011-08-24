
================================================================================
WaitOptions
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.wait_for_updates_ex.WaitForUpdatesEx`
    
.. describe:: Since
    
    vSphere API 4.1
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.wait_options.WaitOptions
    
    .. py:attribute:: maxObjectUpdates
    
        The maximum number of ObjectUpdate entries that should be returned in a single result from WaitForUpdatesEx. See truncated
        
    
    .. py:attribute:: maxWaitSeconds
    
        The number of seconds the PropertyCollector should wait before returning null. Returning updates may take longer if the actual calculation time exceeds maxWaitSeconds. Additionally PropertyCollector policy may cause it to return null sooner than maxWaitSeconds.
        
    