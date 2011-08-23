
================================================================================
ClusterPowerOnVmResult
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.fault_tolerance_secondary_op_result.FaultToleranceSecondaryOpResult`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.cluster_attempted_vm_info.ClusterAttemptedVmInfo`,
    :py:class:`~pyvisdk.do.cluster_not_attempted_vm_info.ClusterNotAttemptedVmInfo`,
    :py:class:`~pyvisdk.do.cluster_recommendation.ClusterRecommendation`
    
.. describe:: Since
    
    VI API 2.5
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.power_on_multi_vm__task.PowerOnMultiVM_Task`
    
.. class:: pyvisdk.do.cluster_power_on_vm_result.ClusterPowerOnVmResult
    
    .. py:attribute:: attempted
    
        The list of virtual machines the Virtual Center has attempted to power on. For a virtual machine not managed by DRS, a task ID is also returned.
        
    
    .. py:attribute:: notAttempted
    
        The list of virtual machines DRS can not find suitable hosts for powering on. There is one fault associated with each virtual machine.
        
    
    .. py:attribute:: recommendations
    
        The list of recommendations that need the client to approve manually.
        
    