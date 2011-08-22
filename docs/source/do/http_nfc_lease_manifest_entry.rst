
================================================================================
HttpNfcLeaseManifestEntry
================================================================================


.. describe:: Since
    
    vSphere API 4.1
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.http_nfc_lease_get_manifest.HttpNfcLeaseGetManifest`
    
.. class:: pyvisdk.do.http_nfc_lease_manifest_entry.HttpNfcLeaseManifestEntry
    
    .. py:attribute:: capacity
    
        The capacity of the disk, if the file is a virtual disk backing.
        
    
    .. py:attribute:: disk
    
        True if the downloaded file is a virtual disk backing.
        
    
    .. py:attribute:: key
    
        Key used to match this entry with the corresponding DeviceUrl entry in info.
        
    
    .. py:attribute:: populatedSize
    
        The populated size of the disk, if the file is a virtual disk backing.
        
    
    .. py:attribute:: sha1
    
        SHA-1 checksum of the data stream sent from the server. This can be used to verify that the bytes received by the client match those sent by the HttpNfc server.
        
    
    .. py:attribute:: size
    
        Size of the downloaded file.
        
    