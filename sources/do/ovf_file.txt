
================================================================================
OvfFile
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.ovf_create_descriptor_params.OvfCreateDescriptorParams`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.ovf_file.OvfFile
    
    .. py:attribute:: capacity
    
        The capacity of the disk backed by this file. This should only be set if the device backed by this file is a disk. This value will be written in the "capacity" attribute of the corresponding "Disk" element in the OVF descriptor.
        
    
    .. py:attribute:: chunkSize
    
        The chunksize chosen by the caller.
        
    
    .. py:attribute:: compressionMethod
    
        The compression method the caller chose to employ for this file.
        
    
    .. py:attribute:: deviceId
    
        The ID of the device backed by this file. This ID uniquely identifies the device within the entity hierarchy.
        
    
    .. py:attribute:: path
    
        The path chosen by the caller for this file. This path becomes the value of the "href" attribute of the corresponding "File" element in the OVF descriptor.
        
    
    .. py:attribute:: populatedSize
    
        The populated size of the disk backed by this file. This should only be set if the device backed by this file is a disk. This value will be written in the "populatedSize" attribute of the corresponding "Disk" element in the OVF descriptor.
        
    
    .. py:attribute:: size
    
        The file size, as observed by the caller during download.
        
    