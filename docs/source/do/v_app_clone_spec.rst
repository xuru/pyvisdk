
================================================================================
VAppCloneSpec
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.clone_v_app__task.CloneVApp_Task`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.datastore.Datastore`,
    :py:class:`~pyvisdk.do.folder.Folder`,
    :py:class:`~pyvisdk.do.host_system.HostSystem`,
    :py:class:`~pyvisdk.do.key_value.KeyValue`,
    :py:class:`~pyvisdk.do.resource_config_spec.ResourceConfigSpec`,
    :py:class:`~pyvisdk.do.v_app_clone_spec_network_mapping_pair.VAppCloneSpecNetworkMappingPair`,
    :py:class:`~pyvisdk.do.v_app_clone_spec_resource_map.VAppCloneSpecResourceMap`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.v_app_clone_spec.VAppCloneSpec
    
    .. py:attribute:: host
    
        The target host for the virtual machines. This is often not a required parameter. If not specified, the behavior is as follows: * If the target pool represents a stand-alone host, that host is used. * If the target pool represents a DRS-enabled cluster, a host selected by DRS is used. * If the target pool represents a cluster without DRS enabled or a DRS-enabled cluster in manual mode, an InvalidArgument exception is thrown.
        
    
    .. py:attribute:: location
    
        Location where the destination vApp must be stored
        
    
    .. py:attribute:: networkMapping
    
        Network mappings. See NetworkMappingPair.
        
    
    .. py:attribute:: property_
    
        A set of property values to override.
        
    
    .. py:attribute:: provisioning
    
        Specify how the VMs in the vApp should be provisioned.
        
    
    .. py:attribute:: resourceMapping
    
        The resource configuration for the cloned vApp.
        
    
    .. py:attribute:: resourceSpec
    
        The resource configuration for the vApp.
        
    
    .. py:attribute:: vmFolder
    
        The VM Folder to associate the vApp with
        
    