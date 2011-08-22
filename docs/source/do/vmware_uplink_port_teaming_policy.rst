
================================================================================
VmwareUplinkPortTeamingPolicy
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.v_mware_dvs_port_setting.VMwareDVSPortSetting`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.bool_policy.BoolPolicy`,
    :py:class:`~pyvisdk.do.dvs_failure_criteria.DVSFailureCriteria`,
    :py:class:`~pyvisdk.do.string_policy.StringPolicy`,
    :py:class:`~pyvisdk.do.v_mware_uplink_port_order_policy.VMwareUplinkPortOrderPolicy`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.inheritable_policy.InheritablePolicy`
    
.. class:: pyvisdk.do.vmware_uplink_port_teaming_policy.VmwareUplinkPortTeamingPolicy
    
    .. py:attribute:: failureCriteria
    
        Failover detection policy for the uplink port team.
        
    
    .. py:attribute:: notifySwitches
    
        Flag to specify whether or not to notify the physical switch if a link fails. Also see notifySwitches
        
    
    .. py:attribute:: policy
    
        Network adapter teaming policy. The policy defines the way traffic from the clients of the team is routed through the different uplinks in the team. The policies supported on the vDS platform is one of nicTeamingPolicy.
        
    
    .. py:attribute:: reversePolicy
    
        The flag to indicate whether or not the teaming policy is applied to inbound frames as well. Also see reversePolicy
        
    
    .. py:attribute:: rollingOrder
    
        The flag to indicate whether or not to use a rolling policy when restoring links. Also see rollingOrder
        
    
    .. py:attribute:: uplinkPortOrder
    
        Failover order policy for uplink ports on the hosts.
        
    