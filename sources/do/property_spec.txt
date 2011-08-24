
================================================================================
PropertySpec
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.property_filter_spec.PropertyFilterSpec`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.property_spec.PropertySpec
    
    .. py:attribute:: all
    
        Specifies whether or not all properties of the object are read. If this property is set to true, the pathSet property is ignored.
        
    
    .. py:attribute:: pathSet
    
        Specifies which managed object properties are retrieved. If the pathSet is empty, then the PropertyCollector retrieves references to the managed objects and no managed object properties are collected.
        
    
    .. py:attribute:: type
    
        Name of the managed object type being collected.
        
    