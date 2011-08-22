
================================================================================
OvfCreateDescriptorResult
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.localized_method_fault.LocalizedMethodFault`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.create_descriptor.CreateDescriptor`
    
.. class:: pyvisdk.do.ovf_create_descriptor_result.OvfCreateDescriptorResult
    
    .. py:attribute:: error
    
        Errors that happened during processing.
        
    
    .. py:attribute:: includeImageFiles
    
        Returns true if there are ISO or Floppy images attached to one or more VMs.
        
    
    .. py:attribute:: ovfDescriptor
    
        The OVF descriptor for the entity.
        
    
    .. py:attribute:: warning
    
        Non-fatal warnings from the processing.
        
    