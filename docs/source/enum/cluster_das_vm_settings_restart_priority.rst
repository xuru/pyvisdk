
==================================================================================================
ClusterDasVmSettingsRestartPriority
==================================================================================================

.. describe:: ClusterDasVmSettingsRestartPriority

    The ClusterDasVmSettingsRestartPriority enum defines virtual machine restart priority values to resolve resource contention. The priority determines the preference that HA gives to a virtual machine if sufficient capacity is not available to power on all failed virtual machines. For example, high priority virtual machines on a host get preference over low priority virtual machines.All priority values are valid for the restart priority specified in a single virtual machine HA configuration (dasSettings). All values except for are valid for the cluster-wide default HA configuration for virtual machines (defaultVmSettings).
    
    
    .. py:data:: ClusterDasVmSettingsRestartPriority.clusterRestartPriority
    
        Virtual machines with this priority use the default restart priority defined for the cluster that contains this virtual machine.
        
    
    .. py:data:: ClusterDasVmSettingsRestartPriority.disabled
    
        VMware HA is disabled for this virtual machine.
        
    
    .. py:data:: ClusterDasVmSettingsRestartPriority.high
    
        Virtual machines with this priority have a higher chance of powering on after a failure if there is insufficient capacity on hosts to meet all virtual machine needs.
        
    
    .. py:data:: ClusterDasVmSettingsRestartPriority.low
    
        Virtual machines with this priority have a lower chance of powering on after a failure if there is insufficient capacity on hosts to meet all virtual machine needs.
        
    
    .. py:data:: ClusterDasVmSettingsRestartPriority.medium
    
        Virtual machines with this priority have an intermediate chance of powering on after a failure if there is insufficient capacity on hosts to meet all virtual machine needs.
        
    