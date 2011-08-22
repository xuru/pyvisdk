
================================================================================
HostInternetScsiHbaAuthenticationProperties
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.update_internet_scsi_authentication_properties.UpdateInternetScsiAuthenticationProperties`
    
.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_internet_scsi_hba.HostInternetScsiHba`,
    :py:class:`~pyvisdk.do.host_internet_scsi_hba_send_target.HostInternetScsiHbaSendTarget`,
    :py:class:`~pyvisdk.do.host_internet_scsi_hba_static_target.HostInternetScsiHbaStaticTarget`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_internet_scsi_hba_authentication_properties.HostInternetScsiHbaAuthenticationProperties
    
    .. py:attribute:: chapAuthEnabled
    
        True if CHAP is currently enabled
        
    
    .. py:attribute:: chapAuthenticationType
    
        The preference for CHAP or non-CHAP protocol if CHAP is enabled
        
    
    .. py:attribute:: chapInherited
    
        CHAP settings are inherited
        
    
    .. py:attribute:: chapName
    
        The CHAP user name if enabled
        
    
    .. py:attribute:: chapSecret
    
        The CHAP secret if enabled
        
    
    .. py:attribute:: mutualChapAuthenticationType
    
        The preference for CHAP or non-CHAP protocol if CHAP is enabled
        
    
    .. py:attribute:: mutualChapInherited
    
        Mutual-CHAP settings are inherited
        
    
    .. py:attribute:: mutualChapName
    
        When Mutual-CHAP is enabled, the user name that target needs to use to authenticate with the initiator
        
    
    .. py:attribute:: mutualChapSecret
    
        When Mutual-CHAP is enabled, the secret that target needs to use to authenticate with the initiator
        
    