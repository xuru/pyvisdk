
================================================================================
VAppCloneSpecResourceMap
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.v_app_clone_spec.VAppCloneSpec`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.datastore.Datastore`,
    :py:class:`~pyvisdk.do.managed_entity.ManagedEntity`,
    :py:class:`~pyvisdk.do.resource_config_spec.ResourceConfigSpec`,
    :py:class:`~pyvisdk.do.resource_pool.ResourcePool`
    
.. describe:: Since
    
    vSphere API 4.1
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.v_app_clone_spec_resource_map.VAppCloneSpecResourceMap
    
    .. py:attribute:: location
    
        A client can optionally specify a datastore in the resource map to override the default datastore location set in location field. This enables cloning to different compute resources that do not have shared datastores.
        
    
    .. py:attribute:: parent
    
        Resource pool to use for the cloned entity of source. This must specify a resource pool that is not part of the vApp. If this is specified, a linked child (as opposed to a direct child) is created for the vApp.
        
    
    .. py:attribute:: resourceSpec
    
        An optional resource configuration for the cloned entity of the source. If not specified, the same resource configuration as the source is used.
        
    
    .. py:attribute:: source
    
        Source entity
        
    