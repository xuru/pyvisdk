
================================================================================
HostHostBusAdapter
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_multipath_info_path.HostMultipathInfoPath`,
    :py:class:`~pyvisdk.do.host_plug_store_topology_adapter.HostPlugStoreTopologyAdapter`,
    :py:class:`~pyvisdk.do.host_scsi_topology_interface.HostScsiTopologyInterface`,
    :py:class:`~pyvisdk.do.host_storage_device_info.HostStorageDeviceInfo`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Extended by
    
    :py:class:`~pyvisdk.do.host_block_hba.HostBlockHba`,
    :py:class:`~pyvisdk.do.host_fibre_channel_hba.HostFibreChannelHba`,
    :py:class:`~pyvisdk.do.host_internet_scsi_hba.HostInternetScsiHba`,
    :py:class:`~pyvisdk.do.host_parallel_scsi_hba.HostParallelScsiHba`
    
.. class:: pyvisdk.do.host_host_bus_adapter.HostHostBusAdapter
    
    .. py:attribute:: bus
    
        The host bus number.
        
    
    .. py:attribute:: device
    
        The device name of host bus adapter.
        
    
    .. py:attribute:: driver
    
        The name of the driver.
        
    
    .. py:attribute:: key
    
        The linkable identifier.
        
    
    .. py:attribute:: model
    
        The model name of the host bus adapter.
        
    
    .. py:attribute:: pci
    
        The Peripheral Connect Interface (PCI) ID of the device representing the host bus adapter.
        
    
    .. py:attribute:: status
    
        The operational status of the adapter. Valid values include "online", "offline", and "fault".
        
    