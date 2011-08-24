
================================================================================
HostDigestInfo
================================================================================


.. describe:: Extended by
    
    :py:class:`~pyvisdk.do.host_tpm_digest_info.HostTpmDigestInfo`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_digest_info.HostDigestInfo
    
    .. py:attribute:: digestMethod
    
        Method in which the digest value is calculated. The set of possible values is described in HostDigestInfoDigestMethodType.
        
    
    .. py:attribute:: digestValue
    
        The variable length byte array containing the digest value calculated by the specified digestMethod.
        
    
    .. py:attribute:: objectName
    
        The name of the object from which this digest value is calcaulated.
        
    