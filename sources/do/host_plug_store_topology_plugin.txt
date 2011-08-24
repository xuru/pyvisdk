
================================================================================
HostPlugStoreTopologyPlugin
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_plug_store_topology.HostPlugStoreTopology`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_plug_store_topology_device.HostPlugStoreTopologyDevice`,
    :py:class:`~pyvisdk.do.host_plug_store_topology_path.HostPlugStoreTopologyPath`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_plug_store_topology_plugin.HostPlugStoreTopologyPlugin
    
    .. py:attribute:: claimedPath
    
        The set of paths claimed by this plugin. Not every claimed path will necessarily appear as part of a Device. Claimed paths will only appear under Devices if the device identifier of the path matches up with the device identifier exposed by the Device.
        
    
    .. py:attribute:: device
    
        The set of devices formed by this plugin.
        
    
    .. py:attribute:: key
    
        The identifier of the plugin.
        
    
    .. py:attribute:: name
    
        The name of the plugin.
        
    