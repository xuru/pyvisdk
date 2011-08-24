
================================================================================
HostInternetScsiHbaDiscoveryCapabilities
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_internet_scsi_hba.HostInternetScsiHba`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_internet_scsi_hba_discovery_capabilities.HostInternetScsiHbaDiscoveryCapabilities
    
    .. py:attribute:: iSnsDiscoverySettable
    
        True if this host bus adapter supports iSNS
        
    
    .. py:attribute:: sendTargetsDiscoverySettable
    
        True if this host bus adapter supports changing the configuration state of send targets discovery. Send targets is mandatory, however some adapters may not allow disabling this discovery method.
        
    
    .. py:attribute:: slpDiscoverySettable
    
        True if this host bus adapter supports SLP
        
    
    .. py:attribute:: staticTargetDiscoverySettable
    
        True if this host bus adapter supports static discovery
        
    