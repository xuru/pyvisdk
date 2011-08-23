
================================================================================
UpdateSet
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.property_filter_update.PropertyFilterUpdate`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.check_for_updates.CheckForUpdates`,
    :py:meth:`~pyvisdk.do.wait_for_updates.WaitForUpdates`,
    :py:meth:`~pyvisdk.do.wait_for_updates_ex.WaitForUpdatesEx`
    
.. class:: pyvisdk.do.update_set.UpdateSet
    
    .. py:attribute:: filterSet
    
        Set of managed object updates detected by specific filters. Updates are reported in sets. Each set is associated with a reference to a filter that detected the updates in the set.
        
    
    .. py:attribute:: truncated
    
        If true, this UpdateSet contains results from a suspended change calculation, which places restrictions on the use of version.
        
    
    .. py:attribute:: version
    
        New data version to pass in the next call to CheckForUpdates, WaitForUpdates, or WaitForUpdatesEx. These versions, although they are opaque, are strongly ordered in the sense that passing a version to WaitForUpdates, CheckForUpdates or WaitForUpdatesEx requests updates that reflect changes in the objects selected by the Filter that happened after the specified version.
        
    