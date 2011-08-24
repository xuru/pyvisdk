
================================================================================
OvfFileItem
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.ovf_create_import_spec_result.OvfCreateImportSpecResult`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.ovf_file_item.OvfFileItem
    
    .. py:attribute:: chunkSize
    
        The chunksize as specified by the OVF specification. If this attribute is set, the "path" attribute is a prefix to each chunk of the complete file. For example, if chunksize is 2000000000 bytes, the actual files might be: myfile.000000000 (2000000000 bytes) myfile.000000001 (2000000000 bytes) myfile.000000002 (1500000000 bytes)
        
    
    .. py:attribute:: cimType
    
        The CIM type of the device for which this file provides backing.
        
    
    .. py:attribute:: compressionMethod
    
        The compression method as specified by the OVF specification (for example "gzip" or "bzip2").
        
    
    .. py:attribute:: create
    
        True if the item is not expected to exist in the infrastructure and should therefore be created by the caller (for example using HTTP PUT).
        
    
    .. py:attribute:: deviceId
    
        Uniquely identifies the device (disk, CD-ROM etc.) within the entity hierarchy.
        
    
    .. py:attribute:: path
    
        The path of the item to upload, relative to the path of the OVF descriptor.
        
    
    .. py:attribute:: size
    
        The complete size of the file, if it is specified in the OVF descriptor.
        
    