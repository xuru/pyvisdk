
================================================================================
HostInternetScsiHbaDiscoveryProperties
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.update_internet_scsi_discovery_properties.UpdateInternetScsiDiscoveryProperties`
    
.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_internet_scsi_hba.HostInternetScsiHba`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_internet_scsi_hba_discovery_properties.HostInternetScsiHbaDiscoveryProperties
    
    .. py:attribute:: iSnsDiscoveryEnabled
    
        True if iSNS is currently enabled
        
    
    .. py:attribute:: iSnsDiscoveryMethod
    
        The iSNS discovery method in use when iSNS is enabled. Must be one of the values of InternetScsiSnsDiscoveryMethod
        
    
    .. py:attribute:: iSnsHost
    
        For STATIC iSNS, this is the iSNS server address
        
    
    .. py:attribute:: sendTargetsDiscoveryEnabled
    
        True if send targets discovery is enabled
        
    
    .. py:attribute:: slpDiscoveryEnabled
    
        True if SLP is enabled
        
    
    .. py:attribute:: slpDiscoveryMethod
    
        The current SLP discovery method when SLP is enabled. Must be one of the values of SlpDiscoveryMethod
        
    
    .. py:attribute:: slpHost
    
        When the SLP discovery method is set to MANUAL, this property reflects the hostname, and optionally port number of the SLP DA.
        
    
    .. py:attribute:: staticTargetDiscoveryEnabled
    
        True if static target discovery is enabled
        
    