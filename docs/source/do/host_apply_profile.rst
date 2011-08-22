
================================================================================
HostApplyProfile
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_profile_complete_config_spec.HostProfileCompleteConfigSpec`,
    :py:class:`~pyvisdk.do.host_profile_config_info.HostProfileConfigInfo`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.authentication_profile.AuthenticationProfile`,
    :py:class:`~pyvisdk.do.date_time_profile.DateTimeProfile`,
    :py:class:`~pyvisdk.do.firewall_profile.FirewallProfile`,
    :py:class:`~pyvisdk.do.host_memory_profile.HostMemoryProfile`,
    :py:class:`~pyvisdk.do.network_profile.NetworkProfile`,
    :py:class:`~pyvisdk.do.option_profile.OptionProfile`,
    :py:class:`~pyvisdk.do.security_profile.SecurityProfile`,
    :py:class:`~pyvisdk.do.service_profile.ServiceProfile`,
    :py:class:`~pyvisdk.do.storage_profile.StorageProfile`,
    :py:class:`~pyvisdk.do.user_group_profile.UserGroupProfile`,
    :py:class:`~pyvisdk.do.user_profile.UserProfile`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.apply_profile.ApplyProfile`
    
.. class:: pyvisdk.do.host_apply_profile.HostApplyProfile
    
    .. py:attribute:: authentication
    
        Authentication Configuration
        
    
    .. py:attribute:: datetime
    
        Date and time configuration
        
    
    .. py:attribute:: firewall
    
        Firewall configuration
        
    
    .. py:attribute:: memory
    
        Memory configuration for the host. This may not be valid all versions of the host.
        
    
    .. py:attribute:: network
    
        The network profile. If set, the network configuration on the host is overwritten with that specified in the networkProfile
        
    
    .. py:attribute:: option
    
        Set of profiles representing advanced config options.
        
    
    .. py:attribute:: security
    
        Security Configuration of the host. It can include configurations like administrator passwords and so on.
        
    
    .. py:attribute:: service
    
        Host configuration part which specifies the services
        
    
    .. py:attribute:: storage
    
        Storage part of the configuration.
        
    
    .. py:attribute:: userAccount
    
        Set of userAccounts that need to be configured on the host
        
    
    .. py:attribute:: usergroupAccount
    
        Set of UserGroups that need to be configured on the host
        
    