
================================================================================
OvfCreateImportSpecResult
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.import_spec.ImportSpec`,
    :py:class:`~pyvisdk.do.ovf_file_item.OvfFileItem`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.create_import_spec.CreateImportSpec`
    
.. class:: pyvisdk.do.ovf_create_import_spec_result.OvfCreateImportSpecResult
    
    .. py:attribute:: error
    
        Errors that happened during processing. Something will be wrong with the ImportSpec, or it is not present.
        
    
    .. py:attribute:: fileItem
    
        The files that must be uploaded by the caller as part of importing the entity.
        
    
    .. py:attribute:: importSpec
    
        The ImportSpec contains information about which VirtualMachines and VirtualApps are present in the entity and how they relate to each other.
        
    
    .. py:attribute:: warning
    
        Non-fatal warnings from the processing. The ImportSpec will be valid, but the user may choose to reject it based on these warnings.
        
    