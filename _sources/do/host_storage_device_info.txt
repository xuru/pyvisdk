
================================================================================
HostStorageDeviceInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_config_info.HostConfigInfo`,
    :py:class:`~pyvisdk.do.host_config_spec.HostConfigSpec`,
    :py:class:`~pyvisdk.do.host_storage_system.HostStorageSystem`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_host_bus_adapter.HostHostBusAdapter`,
    :py:class:`~pyvisdk.do.host_multipath_info.HostMultipathInfo`,
    :py:class:`~pyvisdk.do.host_plug_store_topology.HostPlugStoreTopology`,
    :py:class:`~pyvisdk.do.host_scsi_topology.HostScsiTopology`,
    :py:class:`~pyvisdk.do.scsi_lun.ScsiLun`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_storage_device_info.HostStorageDeviceInfo
    
    .. py:attribute:: hostBusAdapter
    
        The list of host bus adapters available on the host.
        
    
    .. py:attribute:: multipathInfo
    
        The multipath configuration that controls multipath policy for ScsiLuns. This data object exists only if path information is available and is configurable.
        
    
    .. py:attribute:: plugStoreTopology
    
        The plug-store topology on the host system. This data object exists only if the plug-store system is available and configurable.
        
    
    .. py:attribute:: scsiLun
    
        The list of SCSI logical units available on the host.
        
    
    .. py:attribute:: scsiTopology
    
        Storage topology view of SCSI storage devices. This data object exists only if storage topology information is available. See the ScsiTopology data object type for more information.
        
    
    .. py:attribute:: softwareInternetScsiEnabled
    
        Indicates if the software iSCSI initiator is enabled on this system
        
    