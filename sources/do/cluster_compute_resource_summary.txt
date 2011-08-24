
================================================================================
ClusterComputeResourceSummary
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.cluster_das_admission_control_info.ClusterDasAdmissionControlInfo`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.compute_resource_summary.ComputeResourceSummary`
    
.. class:: pyvisdk.do.cluster_compute_resource_summary.ClusterComputeResourceSummary
    
    .. py:attribute:: admissionControlInfo
    
        Information about the current amount of resources available for a VMware HA cluster. The actual type of admissionControlInfo will depend on what kind of ClusterDasAdmissionControlPolicy was used to configure the cluster.
        
    
    .. py:attribute:: currentBalance
    
        The current balance, in terms of standard deviation, for a DRS cluster. Units are thousandths. For example, 12 represents 0.012.
        
    
    .. py:attribute:: currentEVCModeKey
    
        The Enhanced VMotion Compatibility mode that is currently in effect for all hosts in this cluster; unset if no EVC mode is active.
        
    
    .. py:attribute:: currentFailoverLevel
    
        Current failover level. This is the number of physical host failures that can be tolerated without impacting the ability to satisfy the minimums for all running virtual machines. This represents the current value, as opposed to desired value configured by the user.
        
    
    .. py:attribute:: numVmotions
    
        Total number of migrations with VMotion that have been done internal to this cluster.
        
    
    .. py:attribute:: targetBalance
    
        The target balance, in terms of standard deviation, for a DRS cluster. Units are thousandths. For example, 12 represents 0.012.
        
    