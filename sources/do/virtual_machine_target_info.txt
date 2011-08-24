
================================================================================
VirtualMachineTargetInfo
================================================================================


.. describe:: Extended by
    
    :py:class:`~pyvisdk.do.virtual_machine_cdrom_info.VirtualMachineCdromInfo`,
    :py:class:`~pyvisdk.do.virtual_machine_datastore_info.VirtualMachineDatastoreInfo`,
    :py:class:`~pyvisdk.do.virtual_machine_disk_device_info.VirtualMachineDiskDeviceInfo`,
    :py:class:`~pyvisdk.do.virtual_machine_floppy_info.VirtualMachineFloppyInfo`,
    :py:class:`~pyvisdk.do.virtual_machine_network_info.VirtualMachineNetworkInfo`,
    :py:class:`~pyvisdk.do.virtual_machine_parallel_info.VirtualMachineParallelInfo`,
    :py:class:`~pyvisdk.do.virtual_machine_pci_passthrough_info.VirtualMachinePciPassthroughInfo`,
    :py:class:`~pyvisdk.do.virtual_machine_scsi_passthrough_info.VirtualMachineScsiPassthroughInfo`,
    :py:class:`~pyvisdk.do.virtual_machine_serial_info.VirtualMachineSerialInfo`,
    :py:class:`~pyvisdk.do.virtual_machine_sound_info.VirtualMachineSoundInfo`,
    :py:class:`~pyvisdk.do.virtual_machine_usb_info.VirtualMachineUsbInfo`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.virtual_machine_target_info.VirtualMachineTargetInfo
    
    .. py:attribute:: configurationTag
    
        List of configurations that this device is available for. This is only filled out if more than one configuration is requested.
        
    
    .. py:attribute:: name
    
        The identification of the endpoint on the host. The format of this depends on the kind of virtual device this endpoints is used for. For example, for a VirtualEthernetCard this would be a networkname, and for a VirtualCDROM it would be a device name.
        
    