
================================================================================
HostNicTeamingPolicy
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_network_policy.HostNetworkPolicy`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_nic_failure_criteria.HostNicFailureCriteria`,
    :py:class:`~pyvisdk.do.host_nic_order_policy.HostNicOrderPolicy`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_nic_teaming_policy.HostNicTeamingPolicy
    
    .. py:attribute:: failureCriteria
    
        Failover detection policy for this network adapter team. The bridge must be BondBridge for this property to be valid.
        
    
    .. py:attribute:: nicOrder
    
        Failover order policy for network adapters on this switch. The bridge must be BondBridge for this property to be valid.
        
    
    .. py:attribute:: notifySwitches
    
        Flag to specify whether or not to notify the physical switch if a link fails. If this property is true, ESX Server will respond to the failure by sending a RARP packet from a different physical adapter, causing the switch to update its cache.
        
    
    .. py:attribute:: policy
    
        Network adapter teaming policy includes failover and load balancing, It can be one of the following: *
        
    
    .. py:attribute:: reversePolicy
    
        The flag to indicate whether or not the teaming policy is applied to inbound frames as well. For example, if the policy is explicit failover, a broadcast request goes through uplink1 and comes back through uplink2. Then if the reverse policy is set, the frame is dropped when it is received from uplink2. This reverse policy is useful to prevent the virtual machine from getting reflections.
        
    
    .. py:attribute:: rollingOrder
    
        The flag to indicate whether or not to use a rolling policy when restoring links. For example, assume the explicit link order is (vmnic9, vmnic0), therefore vmnic9 goes down, vmnic0 comes up. However, when vmnic9 comes backup, if rollingOrder is set to be true, vmnic0 continues to be used, otherwise, vmnic9 is restored as specified in the explicitly order.
        
    