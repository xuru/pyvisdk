
================================================================================
ConfigTarget
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.distributed_virtual_portgroup_info.DistributedVirtualPortgroupInfo`,
    :py:class:`~pyvisdk.do.distributed_virtual_switch_info.DistributedVirtualSwitchInfo`,
    :py:class:`~pyvisdk.do.resource_pool_runtime_info.ResourcePoolRuntimeInfo`,
    :py:class:`~pyvisdk.do.virtual_machine_cdrom_info.VirtualMachineCdromInfo`,
    :py:class:`~pyvisdk.do.virtual_machine_datastore_info.VirtualMachineDatastoreInfo`,
    :py:class:`~pyvisdk.do.virtual_machine_floppy_info.VirtualMachineFloppyInfo`,
    :py:class:`~pyvisdk.do.virtual_machine_ide_disk_device_info.VirtualMachineIdeDiskDeviceInfo`,
    :py:class:`~pyvisdk.do.virtual_machine_legacy_network_switch_info.VirtualMachineLegacyNetworkSwitchInfo`,
    :py:class:`~pyvisdk.do.virtual_machine_network_info.VirtualMachineNetworkInfo`,
    :py:class:`~pyvisdk.do.virtual_machine_parallel_info.VirtualMachineParallelInfo`,
    :py:class:`~pyvisdk.do.virtual_machine_pci_passthrough_info.VirtualMachinePciPassthroughInfo`,
    :py:class:`~pyvisdk.do.virtual_machine_scsi_disk_device_info.VirtualMachineScsiDiskDeviceInfo`,
    :py:class:`~pyvisdk.do.virtual_machine_scsi_passthrough_info.VirtualMachineScsiPassthroughInfo`,
    :py:class:`~pyvisdk.do.virtual_machine_serial_info.VirtualMachineSerialInfo`,
    :py:class:`~pyvisdk.do.virtual_machine_sound_info.VirtualMachineSoundInfo`,
    :py:class:`~pyvisdk.do.virtual_machine_usb_info.VirtualMachineUsbInfo`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.query_config_target.QueryConfigTarget`
    
.. class:: pyvisdk.do.config_target.ConfigTarget
    
    .. py:attribute:: autoVmotion
    
        Information whether a virtual machine with this ConfigTarget can auto vmotion. This field is only populated from an Environment browser obtained from a virtual machine.
        
    
    .. py:attribute:: cdRom
    
        List of CD-ROM devices available for use by virtual CD-ROMs. Used for VirtualCdromAtapiBackingInfo.
        
    
    .. py:attribute:: datastore
    
        List of datastores available for virtual disks and associated storage.
        
    
    .. py:attribute:: distributedVirtualPortgroup
    
        List of networks available from DistributedVirtualSwitch for virtual network adapters.
        
    
    .. py:attribute:: distributedVirtualSwitch
    
        List of distributed virtual switch available for virtual network adapters.
        
    
    .. py:attribute:: floppy
    
        List of floppy devices available for use by virtual floppies. Used for VirtualFloppyDeviceBackingInfo.
        
    
    .. py:attribute:: ideDisk
    
        List of physical IDE disks that can be used as targets for raw disk backings.
        
    
    .. py:attribute:: legacyNetworkInfo
    
        Legacy switch names when using the LegacyNetworkBacking types.
        
    
    .. py:attribute:: maxMemMBOptimalPerf
    
        Maximum recommended memory size, in MB, for creating a new virtual machine.
        
    
    .. py:attribute:: network
    
        List of networks available for virtual network adapters.
        
    
    .. py:attribute:: numCpuCores
    
        Number of physical CPU cores that are available to run virtual machines.
        
    
    .. py:attribute:: numCpus
    
        Number of logical CPUs that can be used to run virtual machines.
        
    
    .. py:attribute:: numNumaNodes
    
        Number of NUMA nodes.
        
    
    .. py:attribute:: parallel
    
        List of parallel devices available to support virtualization. Used for VirtualParallelPortDeviceBackingInfo.
        
    
    .. py:attribute:: pciPassthrough
    
        List of generic PCI devices.
        
    
    .. py:attribute:: resourcePool
    
        Information about the current available resources on the current resource pool for a virtual machine. This field is only populated from an Environment browser obtained from a virtual machine.
        
    
    .. py:attribute:: scsiDisk
    
        List of physical SCSI disks that can be used as targets for raw disk mapping backings.
        
    
    .. py:attribute:: scsiPassthrough
    
        List of generic SCSI devices.
        
    
    .. py:attribute:: serial
    
        List of serial devices available to support virtualization. Used for VirtualSerialPortDeviceBackingInfo.
        
    
    .. py:attribute:: sound
    
        List of sound devices available to support virtualization. Used for VirtualSoundCardDeviceBackingInfo.
        
    
    .. py:attribute:: usb
    
        List of USB devices on the host that are available to support virtualization. Used for VirtualUSBUSBBackingInfo.
        
    