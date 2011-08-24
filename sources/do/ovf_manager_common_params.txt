
================================================================================
OvfManagerCommonParams
================================================================================


.. describe:: Extended by
    
    :py:class:`~pyvisdk.do.ovf_create_import_spec_params.OvfCreateImportSpecParams`,
    :py:class:`~pyvisdk.do.ovf_parse_descriptor_params.OvfParseDescriptorParams`,
    :py:class:`~pyvisdk.do.ovf_validate_host_params.OvfValidateHostParams`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.key_value.KeyValue`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.ovf_manager_common_params.OvfManagerCommonParams
    
    .. py:attribute:: deploymentOption
    
        The key of the chosen deployment option. If empty, the default option is chosen. The list of possible deployment options is returned in the result of parseDescriptor.
        
    
    .. py:attribute:: locale
    
        The locale-identifier to choose from the descriptor. If empty, the default locale on the server is used.
        
    
    .. py:attribute:: msgBundle
    
        An optional set of localization strings to be used. The server will use these message strings to localize information in the result and in error and warning messages.
        
    