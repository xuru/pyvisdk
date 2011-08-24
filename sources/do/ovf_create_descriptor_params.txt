
================================================================================
OvfCreateDescriptorParams
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.create_descriptor.CreateDescriptor`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.ovf_file.OvfFile`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.ovf_create_descriptor_params.OvfCreateDescriptorParams
    
    .. py:attribute:: description
    
        The contents of the Annontation section of the top-level OVF Entity. If unset, any existing annotation on the entity is left unchanged.
        
    
    .. py:attribute:: includeImageFiles
    
        Controls whether attached image files should be included in the descriptor. This applies to image files attached to VirtualCdrom and VirtualFloppy.
        
    
    .. py:attribute:: name
    
        The ovf:id to use for the top-level OVF Entity. If unset, the entity's product name is used if available. Otherwise, the VI entity name is used.
        
    
    .. py:attribute:: ovfFiles
    
        Contains information about the files of the entity, if they have already been downloaded. Needed to construct the References section of the descriptor.
        
    