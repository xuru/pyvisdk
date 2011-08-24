
================================================================================
NetworkProfile
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_apply_profile.HostApplyProfile`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.dvs_host_v_nic_profile.DvsHostVNicProfile`,
    :py:class:`~pyvisdk.do.dvs_profile.DvsProfile`,
    :py:class:`~pyvisdk.do.dvs_service_console_v_nic_profile.DvsServiceConsoleVNicProfile`,
    :py:class:`~pyvisdk.do.host_port_group_profile.HostPortGroupProfile`,
    :py:class:`~pyvisdk.do.ip_route_profile.IpRouteProfile`,
    :py:class:`~pyvisdk.do.network_profile_dns_config_profile.NetworkProfileDnsConfigProfile`,
    :py:class:`~pyvisdk.do.physical_nic_profile.PhysicalNicProfile`,
    :py:class:`~pyvisdk.do.service_console_port_group_profile.ServiceConsolePortGroupProfile`,
    :py:class:`~pyvisdk.do.virtual_switch_profile.VirtualSwitchProfile`,
    :py:class:`~pyvisdk.do.vm_port_group_profile.VmPortGroupProfile`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.apply_profile.ApplyProfile`
    
.. class:: pyvisdk.do.network_profile.NetworkProfile
    
    .. py:attribute:: consoleIpRouteConfig
    
        Profile representing the Ip Route configuration for the Service Console gateway.
        
    
    .. py:attribute:: dnsConfig
    
        Profile representing the DNS configuration
        
    
    .. py:attribute:: dvsHostNic
    
        List of Host Vnics connected to a Distributed Virtual Switch
        
    
    .. py:attribute:: dvsServiceConsoleNic
    
        List of Service Console Vnics connected to a Distributed Virtual Switch
        
    
    .. py:attribute:: dvswitch
    
        Distributed Virtual Switches which this host is part of
        
    
    .. py:attribute:: hostPortGroup
    
        The set of portgroups for use by the Host
        
    
    .. py:attribute:: ipRouteConfig
    
        Profile representing the Ip Route configuration for the VMKernel gateway.
        
    
    .. py:attribute:: pnic
    
        Profile representing the Physical Nic configurations.
        
    
    .. py:attribute:: serviceConsolePortGroup
    
        The set of portgroups for use by Service Console. This field is considered only when applying the profile on hosts which have a ServiceConsole.
        
    
    .. py:attribute:: vmPortGroup
    
        The set of portgroups for use by Virtual Machines
        
    
    .. py:attribute:: vswitch
    
        The set of virtual switches.
        
    