
================================================================================
ClusterFailoverLevelAdmissionControlInfo
================================================================================


.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.cluster_das_admission_control_info.ClusterDasAdmissionControlInfo`
    
.. class:: pyvisdk.do.cluster_failover_level_admission_control_info.ClusterFailoverLevelAdmissionControlInfo
    
    .. py:attribute:: currentFailoverLevel
    
        Current failover level. This is the number of physical host failures that can be tolerated without impacting the ability to satisfy the minimums for all running virtual machines. This represents the current value, as opposed to desired value configured by the user.
        
    