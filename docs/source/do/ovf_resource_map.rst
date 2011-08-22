
================================================================================
OvfResourceMap
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.ovf_create_import_spec_params.OvfCreateImportSpecParams`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.datastore.Datastore`,
    :py:class:`~pyvisdk.do.resource_config_spec.ResourceConfigSpec`,
    :py:class:`~pyvisdk.do.resource_pool.ResourcePool`
    
.. describe:: Since
    
    vSphere API 4.1
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.ovf_resource_map.OvfResourceMap
    
    .. py:attribute:: datastore
    
        A client can optionally specify a datastore location in the resource map to override the default datastore passed into CreateImportSpec field. This enables importing to different compute resources that do not have shared datastores.
        
    
    .. py:attribute:: parent
    
        The parent resource pool to use for the entity. This must specify a resource pool that is not part of the vApp. If this is specified, a linked child (as opposed to a direct child) is created for the vApp.
        
    
    .. py:attribute:: resourceSpec
    
        An optional resource configuration for the created entity. If not specified, the resource configuration given in the OVF descriptor is used.
        
    
    .. py:attribute:: source
    
        Identifies a source VirtualSystem or VirtualSystemCollection in an OVF descriptor. The source cannot be the root VirtualSystem or VirtualSystemCollection of the OVF. This is a path created by concatenating the OVF ids for each entity, e.g., "vm1", "WebTier/vm2", etc.
        
    