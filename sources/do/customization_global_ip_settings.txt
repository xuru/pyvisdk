
================================================================================
CustomizationGlobalIPSettings
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.customization_spec.CustomizationSpec`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.customization_global_ip_settings.CustomizationGlobalIPSettings
    
    .. py:attribute:: dnsServerList
    
        List of DNS servers, for a virtual network adapter with a static IP address. If this list is empty, then the guest operating system is expected to use a DHCP server to get its DNS server settings. These settings configure the virtual machine to use the specified DNS servers. These DNS server settings are listed in order of preference.
        
    
    .. py:attribute:: dnsSuffixList
    
        List of name resolution suffixes for the virtual network adapter. This list applies to both Windows and Linux guest customization. For Linux, this setting is global, whereas in Windows, this setting is listed on a per-adapter basis, even though the setting is global in Windows.
        
    