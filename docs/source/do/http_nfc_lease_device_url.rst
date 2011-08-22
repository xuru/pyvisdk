
================================================================================
HttpNfcLeaseDeviceUrl
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.http_nfc_lease_info.HttpNfcLeaseInfo`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.http_nfc_lease_device_url.HttpNfcLeaseDeviceUrl
    
    .. py:attribute:: datastoreKey
    
        Key for the datastore this disk is on. This is used to look up hosts which can be used to multi-POST disk contents, in the host map of the lease.
        
    
    .. py:attribute:: disk
    
        Optional value to specify if the attached file is a disk in vmdk format.
        
    
    .. py:attribute:: fileSize
    
        Specifies the size of the file backing for this device. This property is only set for non-disk file backings.
        
    
    .. py:attribute:: importKey
    
        Identifies the device based on the names in an ImportSpec. This is only set for import leases.
        
    
    .. py:attribute:: key
    
        The immutable identifier for the device. This is set for both import/export leases.
        
    
    .. py:attribute:: sslThumbprint
    
        SSL thumbprint for the host the URL refers to. Empty if no SSL thumbprint is available or needed.
        
    
    .. py:attribute:: targetId
    
        Id for this target. This only used for multi-POSTing, where a single HTTP POST is applied to multiple targets.
        
    
    .. py:attribute:: url
    
        
        
    