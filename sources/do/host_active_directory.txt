
================================================================================
HostActiveDirectory
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_config_spec.HostConfigSpec`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_active_directory_spec.HostActiveDirectorySpec`
    
.. describe:: Since
    
    vSphere API 4.1
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_active_directory.HostActiveDirectory
    
    .. py:attribute:: changeOperation
    
        Configuration change operation to apply to the host. You can specify the following values: * add: Add the host to the domain. The ESX Server will use the HostActiveDirectorySpec information (domain, account user name and password) to call JoinDomain_Task. * remove: Remove the host from its current domain. The ESX Server will call LeaveCurrentDomain_Task, specifying
        
    
    .. py:attribute:: spec
    
        Active Directory domain access information (domain and account user name and password).
        
    