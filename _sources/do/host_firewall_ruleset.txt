
================================================================================
HostFirewallRuleset
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_firewall_info.HostFirewallInfo`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_firewall_rule.HostFirewallRule`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_firewall_ruleset.HostFirewallRuleset
    
    .. py:attribute:: enabled
    
        Flag indicating whether the ruleset is enabled. If the ruleset is enabled, all ports specified in the ruleset are opened by the firewall.
        
    
    .. py:attribute:: key
    
        Brief identifier for the ruleset.
        
    
    .. py:attribute:: label
    
        Display label for the ruleset.
        
    
    .. py:attribute:: required
    
        Flag indicating whether the ruleset is required and cannot be disabled.
        
    
    .. py:attribute:: rule
    
        List of rules within the ruleset.
        
    
    .. py:attribute:: service
    
        Managed service (if any) that uses this ruleset. Must be one of the services listed in service.
        
    