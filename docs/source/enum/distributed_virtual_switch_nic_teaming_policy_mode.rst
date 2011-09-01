
==================================================================================================
DistributedVirtualSwitchNicTeamingPolicyMode
==================================================================================================

.. describe:: DistributedVirtualSwitchNicTeamingPolicyMode

    List of possible teaming modes supported by the vNetwork Distributed Switch. The different policy modes define the way traffic is routed through the different uplink ports in a team.
    
    
    .. py:data:: DistributedVirtualSwitchNicTeamingPolicyMode.failover_explicit
    
        Use explicit failover order
        
    
    .. py:data:: DistributedVirtualSwitchNicTeamingPolicyMode.loadbalance_ip
    
        Routing based on IP hash
        
    
    .. py:data:: DistributedVirtualSwitchNicTeamingPolicyMode.loadbalance_loadbased
    
        Routing based by dynamically balancing traffic through the NICs in a team. This is the recommended teaming policy when the network I/O control feature is enabled for the vNetwork Distributed Switch.
        
    
    .. py:data:: DistributedVirtualSwitchNicTeamingPolicyMode.loadbalance_srcid
    
        Route based on the source of the port ID
        
    
    .. py:data:: DistributedVirtualSwitchNicTeamingPolicyMode.loadbalance_srcmac
    
        Route based on source MAC hash
        
    