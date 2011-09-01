
==================================================================================================
ClusterDasVmSettingsIsolationResponse
==================================================================================================

.. describe:: ClusterDasVmSettingsIsolationResponse

    The ClusterDasVmSettingsIsolationResponse enum defines values that indicate whether or not the virtual machine should be powered off if a host determines that it is isolated from the rest of the cluster.Host network isolation occurs when a host is still running, but it can no longer communicate with other hosts in the cluster. With default settings, if a host stops receiving heartbeats from all other hosts in the cluster for more than 12 seconds, it attempts to ping its isolation addresses. If this also fails, the host declares itself as isolated from the network. When the isolated host's network connection is not restored after 15 seconds, the other hosts in the cluster treat it as failed and HA attempts to fail over its virtual machines.By default, the isolated host powers off its virtual machines so that HA can restart them on other hosts in the cluster. You can override the isolation response default with a cluster-wide setting (defaultVmSettings) or a virtual machine setting (isolationResponse).* All isolation reponse values are valid for the isolationResponse property specified in a single virtual machine HA configuration. * All values except for are valid for the cluster-wide default HA configuration for virtual machines (defaultVmSettings).If you ensure that your network infrastructure is sufficiently redundant and that at least one network path is available at all times, host network isolation should be a rare occurrence.
    
    
    .. py:data:: ClusterDasVmSettingsIsolationResponse.clusterIsolationResponse
    
        Use the default isolation reponse defined for the cluster that contains this virtual machine.
        
    
    .. py:data:: ClusterDasVmSettingsIsolationResponse.none
    
        Do not power off the virtual machine in the event of a host network isolation.
        
    
    .. py:data:: ClusterDasVmSettingsIsolationResponse.powerOff
    
        Power off the virtual machine in the event of a host network isolation.
        
    
    .. py:data:: ClusterDasVmSettingsIsolationResponse.shutdown
    
        Shut down the virtual machine guest operating system in the event of a host network isolation. If the guest operating system fails to shutdown within five minutes, HA will initiate a forced power off. VI API 2.5u2
        
    