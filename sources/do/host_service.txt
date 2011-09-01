
================================================================================
HostService
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_service_info.HostServiceInfo`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_service.HostService
    
    .. py:attribute:: key
    
        Brief identifier for the service.
        
    
    .. py:attribute:: label
    
        Display label for the service.
        
    
    .. py:attribute:: policy
    
        Service activation policy.See Policy
        
    
    .. py:attribute:: required
    
        Flag indicating whether the service is required and cannot be disabled.
        
    
    .. py:attribute:: ruleset
    
        List of firewall rulesets used by this service. Must come from the list of rulesets in ruleset.
        
    
    .. py:attribute:: running
    
        Flag indicating whether the service is currently running.
        
    
    .. py:attribute:: uninstallable
    
        Flag indicating whether the service can be uninstalled.
        
    