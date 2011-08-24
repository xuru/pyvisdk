
================================================================================
ResourceConfigSpec
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.create_resource_pool.CreateResourcePool`,
    :py:meth:`~pyvisdk.do.create_v_app.CreateVApp`,
    :py:meth:`~pyvisdk.do.update_child_resource_configuration.UpdateChildResourceConfiguration`,
    :py:meth:`~pyvisdk.do.update_config.UpdateConfig`
    
.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_system_resource_info.HostSystemResourceInfo`,
    :py:class:`~pyvisdk.do.ovf_resource_map.OvfResourceMap`,
    :py:class:`~pyvisdk.do.resource_pool.ResourcePool`,
    :py:class:`~pyvisdk.do.resource_pool_summary.ResourcePoolSummary`,
    :py:class:`~pyvisdk.do.v_app_clone_spec.VAppCloneSpec`,
    :py:class:`~pyvisdk.do.v_app_clone_spec_resource_map.VAppCloneSpecResourceMap`,
    :py:class:`~pyvisdk.do.virtual_app_import_spec.VirtualAppImportSpec`,
    :py:class:`~pyvisdk.do.virtual_machine.VirtualMachine`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.managed_entity.ManagedEntity`,
    :py:class:`~pyvisdk.do.resource_allocation_info.ResourceAllocationInfo`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.resource_config_spec.ResourceConfigSpec
    
    .. py:attribute:: changeVersion
    
        The changeVersion is a unique identifier for a given version of the configuration. Each change to the configuration will update this value. This is typically implemented as an ever increasing count or a time-stamp. However, a client should always treat this as an opaque string.
        
    
    .. py:attribute:: cpuAllocation
    
        Resource allocation for CPU.
        
    
    .. py:attribute:: entity
    
        Reference to the entity with this resource specification: either a VirtualMachine or a ResourcePool.
        
    
    .. py:attribute:: lastModified
    
        Timestamp when the resources were last modified. This is ignored when the object is used to update a configuration.
        
    
    .. py:attribute:: memoryAllocation
    
        Resource allocation for memory.
        
    