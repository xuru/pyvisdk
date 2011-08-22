
================================================================================
CustomizationIPSettings
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.customization_adapter_mapping.CustomizationAdapterMapping`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.customization_ip_generator.CustomizationIpGenerator`,
    :py:class:`~pyvisdk.do.customization_ip_settings_ip_v6_address_spec.CustomizationIPSettingsIpV6AddressSpec`,
    :py:class:`~pyvisdk.do.customization_net_bios_mode.CustomizationNetBIOSMode`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.customization_ip_settings.CustomizationIPSettings
    
    .. py:attribute:: dnsDomain
    
        A DNS domain suffix such as vmware.com.
        
    
    .. py:attribute:: dnsServerList
    
        A list of server IP addresses to use for DNS lookup in a Windows guest operating system. In Windows, these settings are adapter-specific, whereas in Linux, they are global. As a result, the Linux guest customization process ignores this setting and looks for its DNS servers in the globalIPSettings object.
        
    
    .. py:attribute:: gateway
    
        For a virtual network adapter with a static IP address, this data object type contains a list of gateways, in order of preference.
        
    
    .. py:attribute:: ip
    
        Specification to obtain a unique IP address for this virtual network adapter.
        
    
    .. py:attribute:: ipV6Spec
    
        This contains the IpGenerator, subnet mask and gateway info for all the ipv6 addresses associated with the virtual network adapter.
        
    
    .. py:attribute:: netBIOS
    
        NetBIOS setting for Windows.
        
    
    .. py:attribute:: primaryWINS
    
        The IP address of the primary WINS server. This property is ignored for Linux guest operating systems.
        
    
    .. py:attribute:: secondaryWINS
    
        The IP address of the secondary WINS server. This property is ignored for Linux guest operating systems.
        
    
    .. py:attribute:: subnetMask
    
        Subnet mask for this virtual network adapter.
        
    