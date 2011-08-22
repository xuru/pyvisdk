
================================================================================
PropertyFilterSpec
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.create_filter.CreateFilter`,
    :py:meth:`~pyvisdk.do.retrieve_properties.RetrieveProperties`,
    :py:meth:`~pyvisdk.do.retrieve_properties_ex.RetrievePropertiesEx`
    
.. describe:: Property of
    
    :py:class:`~pyvisdk.do.property_filter.PropertyFilter`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.object_spec.ObjectSpec`,
    :py:class:`~pyvisdk.do.property_spec.PropertySpec`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.property_filter_spec.PropertyFilterSpec
    
    .. py:attribute:: objectSet
    
        Set of specifications that determine the objects to filter.
        
    
    .. py:attribute:: propSet
    
        Set of properties to include in the filter, specified for each object type.
        
    
    .. py:attribute:: reportMissingObjectsInResults
    
        Control how to report missing objects during filter creation.
        
    