
================================================================================
ComputeResourceSummary
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.compute_resource.ComputeResource`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.managed_entity_status.ManagedEntityStatus`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Extended by
    
    :py:class:`~pyvisdk.do.cluster_compute_resource_summary.ClusterComputeResourceSummary`
    
.. class:: pyvisdk.do.compute_resource_summary.ComputeResourceSummary
    
    .. py:attribute:: effectiveCpu
    
        Effective CPU resources (in MHz) available to run virtual machines. This is the aggregated effective resource level from all running hosts. Hosts that are in maintenance mode or are unresponsive are not counted. Resources used by the VMware Service Console are not included in the aggregate. This value represents the amount of resources available for the root resource pool for running virtual machines.
        
    
    .. py:attribute:: effectiveMemory
    
        Effective memory resources (in MB) available to run virtual machines. This is the aggregated effective resource level from all running hosts. Hosts that are in maintenance mode or are unresponsive are not counted. Resources used by the VMware Service Console are not included in the aggregate. This value represents the amount of resources available for the root resource pool for running virtual machines.
        
    
    .. py:attribute:: numCpuCores
    
        Number of physical CPU cores. Physical CPU cores are the processors contained by a CPU package.
        
    
    .. py:attribute:: numCpuThreads
    
        Aggregated number of CPU threads.
        
    
    .. py:attribute:: numEffectiveHosts
    
        Total number of effective hosts.
        
    
    .. py:attribute:: numHosts
    
        Total number of hosts.
        
    
    .. py:attribute:: overallStatus
    
        Overall alarm status.
        
    
    .. py:attribute:: totalCpu
    
        Aggregated CPU resources of all hosts, in MHz.
        
    
    .. py:attribute:: totalMemory
    
        Aggregated memory resources of all hosts, in bytes.
        
    