
================================================================================
ObjectUpdate
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.property_filter_update.PropertyFilterUpdate`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.missing_property.MissingProperty`,
    :py:class:`~pyvisdk.do.object_update_kind.ObjectUpdateKind`,
    :py:class:`~pyvisdk.do.property_change.PropertyChange`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.object_update.ObjectUpdate
    
    .. py:attribute:: changeSet
    
        Optional set of changes to the object. Present only if the "kind" is either "modify" or "enter".
        
    
    .. py:attribute:: kind
    
        Kind of update that caused the filter to report a change.
        
    
    .. py:attribute:: missingSet
    
        Properties whose value could not be retrieved and their associated faults. Present only if the "kind" is either "modify" or "enter".
        
    
    .. py:attribute:: obj
    
        Reference to the managed object to which this update applies.
        
    