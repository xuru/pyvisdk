
================================================================================
HostPlugStoreTopologyPath
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_plug_store_topology.HostPlugStoreTopology`,
    :py:class:`~pyvisdk.do.host_plug_store_topology_adapter.HostPlugStoreTopologyAdapter`,
    :py:class:`~pyvisdk.do.host_plug_store_topology_device.HostPlugStoreTopologyDevice`,
    :py:class:`~pyvisdk.do.host_plug_store_topology_plugin.HostPlugStoreTopologyPlugin`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_plug_store_topology_adapter.HostPlugStoreTopologyAdapter`,
    :py:class:`~pyvisdk.do.host_plug_store_topology_device.HostPlugStoreTopologyDevice`,
    :py:class:`~pyvisdk.do.host_plug_store_topology_target.HostPlugStoreTopologyTarget`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_plug_store_topology_path.HostPlugStoreTopologyPath
    
    .. py:attribute:: adapter
    
        The adapter that provided the Path.
        
    
    .. py:attribute:: channelNumber
    
        The channel number for a path if applicable.
        
    
    .. py:attribute:: device
    
        The device that claimed the Path if any.
        
    
    .. py:attribute:: key
    
        The identifier for the Path.
        
    
    .. py:attribute:: lunNumber
    
        The LUN number for a path if applicable.
        
    
    .. py:attribute:: name
    
        Name of path. Use this property to correlate this path object to other path objects.
        
    
    .. py:attribute:: target
    
        The target of the Path if any.
        
    
    .. py:attribute:: targetNumber
    
        The target number for a path if applicable. The target number is not guaranteed to be consistent across reboots or rescans of the adapter.
        
    