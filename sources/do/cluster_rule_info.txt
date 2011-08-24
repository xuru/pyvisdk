
================================================================================
ClusterRuleInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.cluster_config_info.ClusterConfigInfo`,
    :py:class:`~pyvisdk.do.cluster_config_info_ex.ClusterConfigInfoEx`,
    :py:class:`~pyvisdk.do.cluster_rule_spec.ClusterRuleSpec`,
    :py:class:`~pyvisdk.do.rule_violation.RuleViolation`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.managed_entity_status.ManagedEntityStatus`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Extended by
    
    :py:class:`~pyvisdk.do.cluster_affinity_rule_spec.ClusterAffinityRuleSpec`,
    :py:class:`~pyvisdk.do.cluster_anti_affinity_rule_spec.ClusterAntiAffinityRuleSpec`,
    :py:class:`~pyvisdk.do.cluster_vm_host_rule_info.ClusterVmHostRuleInfo`
    
.. class:: pyvisdk.do.cluster_rule_info.ClusterRuleInfo
    
    .. py:attribute:: enabled
    
        Flag to indicate whether or not the rule is enabled. Set this property when you configure the rule. The default value is false (disabled). If there is a rule conflict, the Server can override the setting to disable a rule.
        
    
    .. py:attribute:: inCompliance
    
        Flag to indicate whether or not the placement of Virtual Machines is currently in compliance with this rule. The Server does not currently use this property.
        
    
    .. py:attribute:: key
    
        Unique ID for rules. When adding a new rule, do not specify this property. The Server will assign the key.
        
    
    .. py:attribute:: mandatory
    
        Flag to indicate whether compliance with this rule is mandatory or optional. The default value is false (optional). * A mandatory rule will prevent a virtual machine from being powered on or migrated to a host that does not satisfy the rule. * An optional rule specifies a preference. DRS takes an optional rule into consideration when it places a virtual machine in the cluster. DRS will act on an optional rule as long as it does not impact the ability of the host to satisfy current CPU or memory requirements for virtual machines on the system. (As long as the operation does not cause any host to be more than 100% utilized.)
        
    
    .. py:attribute:: name
    
        Name of the rule.
        
    
    .. py:attribute:: status
    
        Flag to indicate whether or not the rule is currently satisfied.
        
    
    .. py:attribute:: userCreated
    
        Flag to indicate whether the rule is created by the user or the system.
        
    