
================================================================================
HostInternetScsiHbaAuthenticationCapabilities
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_internet_scsi_hba.HostInternetScsiHba`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_internet_scsi_hba_authentication_capabilities.HostInternetScsiHbaAuthenticationCapabilities
    
    .. py:attribute:: chapAuthSettable
    
        True if this host bus adapter supports changing the configuration state of CHAP authentication. CHAP is mandatory, however some adapter may not allow disabling this authentication method.
        
    
    .. py:attribute:: krb5AuthSettable
    
        Always false in this version of the API.
        
    
    .. py:attribute:: mutualChapSettable
    
        When chapAuthSettable is TRUE, this describes if Mutual CHAP configuration is allowed as well.
        
    
    .. py:attribute:: spkmAuthSettable
    
        Always false in this version of the API.
        
    
    .. py:attribute:: srpAuthSettable
    
        Always false in this version of the API.
        
    
    .. py:attribute:: targetChapSettable
    
        When targetChapSettable is TRUE, this describes if CHAP configuration is allowed on targets associated with the adapter.
        
    
    .. py:attribute:: targetMutualChapSettable
    
        When targetMutualChapSettable is TRUE, this describes if Mutual CHAP configuration is allowed on targets associated with the adapter.
        
    