
================================================================================
PropertyChange
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.object_update.ObjectUpdate`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.property_change_op.PropertyChangeOp`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.property_change.PropertyChange
    
    .. py:attribute:: name
    
        Property or nested property to which the change applies. Nested properties are specified by paths; for example, * foo.bar * foo.arProp["key val"] * foo.arProp["key val"].baz
        
    
    .. py:attribute:: op
    
        Change operation for the property. Valid values are:
        
    
    .. py:attribute:: val
    
        New value for the property when "op" is either "add" or "assign".
        
    