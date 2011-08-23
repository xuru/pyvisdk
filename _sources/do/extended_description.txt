
================================================================================
ExtendedDescription
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.profile_metadata.ProfileMetadata`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.key_any_value.KeyAnyValue`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.description.Description`
    
.. class:: pyvisdk.do.extended_description.ExtendedDescription
    
    .. py:attribute:: messageArg
    
        Provides named arguments that can be used to localize the message in the catalog.
        
    
    .. py:attribute:: messageCatalogKeyPrefix
    
        Key to the localized message string in the catalog. If the localized string contains parameters, values to the parameters will be provided in #messageArg. E.g: If the message in the catalog is "IP address is {address}", value for "address" will be provided by #messageArg. Both summary and label in Description will have a corresponding entry in the message catalog with the keys .summary and .label respectively. Description.summary and Description.label will contain the strings in server locale.
        
    