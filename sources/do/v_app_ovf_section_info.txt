
================================================================================
VAppOvfSectionInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.v_app_ovf_section_spec.VAppOvfSectionSpec`,
    :py:class:`~pyvisdk.do.vm_config_info.VmConfigInfo`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.v_app_ovf_section_info.VAppOvfSectionInfo
    
    .. py:attribute:: atEnvelopeLevel
    
        Whether this is a global envelope section
        
    
    .. py:attribute:: contents
    
        The XML fragment including the top-level <Section...> element. The fragment is self-contained will all required namespace definitions.
        
    
    .. py:attribute:: key
    
        A unique key to identify a section.
        
    
    .. py:attribute:: namespace
    
        The namespace for the value in xsi:type attribute.
        
    
    .. py:attribute:: type
    
        The value of the xsi:type attribute not including the namespace prefix.
        
    