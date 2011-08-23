
================================================================================
ClusterDrsMigration
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.cluster_compute_resource.ClusterComputeResource`,
    :py:class:`~pyvisdk.do.cluster_drs_recommendation.ClusterDrsRecommendation`,
    :py:class:`~pyvisdk.do.cluster_migration_action.ClusterMigrationAction`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_system.HostSystem`,
    :py:class:`~pyvisdk.do.virtual_machine.VirtualMachine`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.cluster_drs_migration.ClusterDrsMigration
    
    .. py:attribute:: cpuLoad
    
        Current CPU load for the virtual machine, in MHz. This property is only populated for recommendations.
        
    
    .. py:attribute:: destination
    
        Destination host.
        
    
    .. py:attribute:: destinationCpuLoad
    
        Current CPU load on the destination host, in MHz.
        
    
    .. py:attribute:: destinationMemoryLoad
    
        Current memory usage on the destination host, in bytes.
        
    
    .. py:attribute:: key
    
        A unique key that identifies this recommendation. This is used as an argument to ComputeResource.applyRecommendation.
        
    
    .. py:attribute:: memoryLoad
    
        Current memory load for the virtual machine, in bytes. This field is only populated for recommendations.
        
    
    .. py:attribute:: source
    
        Source host.
        
    
    .. py:attribute:: sourceCpuLoad
    
        Current CPU load on the source host, in MHz.
        
    
    .. py:attribute:: sourceMemoryLoad
    
        Current memory usage on the source host, in bytes.
        
    
    .. py:attribute:: time
    
        The time this recommendation was computed.
        
    
    .. py:attribute:: vm
    
        The virtual machine selected for migration.
        
    