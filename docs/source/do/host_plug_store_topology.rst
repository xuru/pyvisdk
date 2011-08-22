
================================================================================
HostPlugStoreTopology
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_storage_device_info.HostStorageDeviceInfo`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_plug_store_topology_adapter.HostPlugStoreTopologyAdapter`,
    :py:class:`~pyvisdk.do.host_plug_store_topology_device.HostPlugStoreTopologyDevice`,
    :py:class:`~pyvisdk.do.host_plug_store_topology_path.HostPlugStoreTopologyPath`,
    :py:class:`~pyvisdk.do.host_plug_store_topology_plugin.HostPlugStoreTopologyPlugin`,
    :py:class:`~pyvisdk.do.host_plug_store_topology_target.HostPlugStoreTopologyTarget`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_plug_store_topology.HostPlugStoreTopology
    
    .. py:attribute:: adapter
    
        List of host bus adapters in the plug store inventory.
        
    
    .. py:attribute:: device
    
        List of devices in the plug store inventory.
        
    
    .. py:attribute:: path
    
        List of paths in the plug store inventory.
        
    
    .. py:attribute:: plugin
    
        List of plugins in the plug store inventory.
        
    
    .. py:attribute:: target
    
        Partial list of targets as seen by the host. The list of targets may not be exhaustive on the host.
        
    