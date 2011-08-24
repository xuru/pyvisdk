
================================================================================
HostInternetScsiHbaDigestCapabilities
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_internet_scsi_hba.HostInternetScsiHba`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_internet_scsi_hba_digest_capabilities.HostInternetScsiHbaDigestCapabilities
    
    .. py:attribute:: dataDigestSettable
    
        True if this host bus adapter supports the configuration of the use of data digest. Defaults to false, in which case no data digests will be used.
        
    
    .. py:attribute:: headerDigestSettable
    
        True if this host bus adapter supports the configuration of the use of header digest. Defaults to false, in which case no header digests will be used.
        
    
    .. py:attribute:: targetDataDigestSettable
    
        True if configuration of the use of data digest is supported on the targets associated with the host bus adapter. Defaults to false, in which case no data digests will be used.
        
    
    .. py:attribute:: targetHeaderDigestSettable
    
        True if configuration of the use of header digest is supported on the targets associated with the host bus adapter. Defaults to false, in which case no header digests will be used.
        
    