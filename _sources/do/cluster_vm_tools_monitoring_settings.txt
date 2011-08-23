
================================================================================
ClusterVmToolsMonitoringSettings
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.cluster_das_vm_settings.ClusterDasVmSettings`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.cluster_vm_tools_monitoring_settings.ClusterVmToolsMonitoringSettings
    
    .. py:attribute:: clusterSettings
    
        Flag indicating whether to use the cluster settings or the per VM settings
        
    
    .. py:attribute:: enabled
    
        Flag indicating whether or not the Virtual Machine Health Monitoring service is enabled.
        
    
    .. py:attribute:: failureInterval
    
        If no heartbeat has been received for at least the specified number of seconds, the virtual machine is declared as failed.
        
    
    .. py:attribute:: maxFailures
    
        Maximum number of failures and automated resets allowed during the time that maxFailureWindow specifies. If maxFailureWindow is -1 (no window), this represents the absolute number of failures after which automated response is stopped.
        
    
    .. py:attribute:: maxFailureWindow
    
        The number of seconds for the window during which up to maxFailures resets can occur before automated responses stop.
        
    
    .. py:attribute:: minUpTime
    
        The number of seconds for the virtual machine's heartbeats to stabilize after the virtual machine has been powered on. This time should include the guest operating system boot-up time. The virtual machine monitoring will begin only after this period.
        
    
    .. py:attribute:: vmMonitoring
    
        Indicates the type of vm monitoring configured. This can be one fo three values disabled, vmMonitoringOnly or vmAndAppMonitoring The default value is vmMonitoringDisabled Please see ClusterDasConfigInfoVmMonitoringState
        
    