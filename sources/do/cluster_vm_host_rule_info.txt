
================================================================================
ClusterVmHostRuleInfo
================================================================================


.. describe:: Since
    
    vSphere API 4.1
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.cluster_rule_info.ClusterRuleInfo`
    
.. class:: pyvisdk.do.cluster_vm_host_rule_info.ClusterVmHostRuleInfo
    
    .. py:attribute:: affineHostGroupName
    
        Name of the affine host group (ClusterHostGroup.name). The affine host group identifies hosts on which vmGroupName virtual machines can be powered-on. The value of the mandatory property determines how the Server interprets the rule.
        
    
    .. py:attribute:: antiAffineHostGroupName
    
        Name of the anti-affine host group (ClusterHostGroup.name). The anti-affine host group identifies hosts on which vmGroupName virtual machines should not be powered-on. The value of the mandatory property determines how the Server interprets the rule.
        
    
    .. py:attribute:: vmGroupName
    
        Virtual group name (ClusterVmGroup.name). The virtual group may contain one or more virtual machines.
        
    