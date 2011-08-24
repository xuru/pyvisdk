
================================================================================
VAppPropertyInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.ovf_parse_descriptor_result.OvfParseDescriptorResult`,
    :py:class:`~pyvisdk.do.v_app_property_spec.VAppPropertySpec`,
    :py:class:`~pyvisdk.do.vm_config_info.VmConfigInfo`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.v_app_property_info.VAppPropertyInfo
    
    .. py:attribute:: category
    
        A user-visible description the category the property belongs to.
        
    
    .. py:attribute:: classId
    
        class name for this property
        
    
    .. py:attribute:: defaultValue
    
        This either contains the default value of a field (used if value is empty string), or the expression if the type is "expression". See comment for the
        
    
    .. py:attribute:: description
    
        A description of the field.
        
    
    .. py:attribute:: id
    
        Name of property. In the OVF environment, the property is listed as [classId.]id[.instanceId]. The [classId.]name[.instanceId] must be unique.
        
    
    .. py:attribute:: instanceId
    
        class name for this property
        
    
    .. py:attribute:: key
    
        A unique integer key for the property.
        
    
    .. py:attribute:: label
    
        The display name for the property.
        
    
    .. py:attribute:: type
    
        Describes the valid format of the property.
        
    
    .. py:attribute:: userConfigurable
    
        Whether the property is user-configurable or a system property. This is not used if the type is expression.
        
    
    .. py:attribute:: value
    
        The value of the field at deployment time. For expressions, this will contain the value that has been computed.
        
    