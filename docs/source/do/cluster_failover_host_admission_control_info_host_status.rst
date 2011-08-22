
================================================================================
ClusterFailoverHostAdmissionControlInfoHostStatus
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.cluster_failover_host_admission_control_info.ClusterFailoverHostAdmissionControlInfo`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_system.HostSystem`,
    :py:class:`~pyvisdk.do.managed_entity_status.ManagedEntityStatus`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.cluster_failover_host_admission_control_info_host_status.ClusterFailoverHostAdmissionControlInfoHostStatus
    
    .. py:attribute:: host
    
        The failover host.
        
    
    .. py:attribute:: status
    
        The status of the failover host. The status is green for a connected host with no VMware HA errors and no virtual machines running on it. The status is yellow for a connected host with no VMware HA errors and some virtual machines running on it. The status red for a disconnected or not responding host, a host that is in maintenance or standby mode or that has a VMware HA error on it.
        
    