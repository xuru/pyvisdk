
================================================================================
CustomizationSpecInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.customization_spec_item.CustomizationSpecItem`,
    :py:class:`~pyvisdk.do.customization_spec_manager.CustomizationSpecManager`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.customization_spec_info.CustomizationSpecInfo
    
    .. py:attribute:: changeVersion
    
        The changeVersion is a unique identifier for a given version of the configuration. Each change to the configuration will update this value. This is typically implemented as an ever increasing count or a time-stamp. However, a client should always treat this as an opaque string.
        
    
    .. py:attribute:: description
    
        Description of the specification.
        
    
    .. py:attribute:: lastUpdateTime
    
        Time when the specification was last modified. This time is ignored when the CustomizationSpecItem containing this is used as an input to CustomizationSpecManager.create.
        
    
    .. py:attribute:: name
    
        Unique name of the specification.
        
    
    .. py:attribute:: type
    
        Guest operating system for this specification (Linux or Windows).
        
    