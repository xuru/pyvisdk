
================================================================================
HostAuthenticationManagerInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_authentication_manager.HostAuthenticationManager`,
    :py:class:`~pyvisdk.do.host_config_info.HostConfigInfo`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_authentication_store_info.HostAuthenticationStoreInfo`
    
.. describe:: Since
    
    vSphere API 4.1
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_authentication_manager_info.HostAuthenticationManagerInfo
    
    .. py:attribute:: authConfig
    
        An array containing entries for local authentication and host Active Directory authentication. * HostLocalAuthenticationInfo - Local authentication is always enabled. * HostActiveDirectoryInfo - Host Active Directory authentication information includes the name of the domain, membership status, and a list of other domains trusted by the membership domain.
        
    