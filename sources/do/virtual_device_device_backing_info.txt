
================================================================================
VirtualDeviceDeviceBackingInfo
================================================================================


.. describe:: Extended by
    
    :py:class:`~pyvisdk.do.virtual_cdrom_atapi_backing_info.VirtualCdromAtapiBackingInfo`,
    :py:class:`~pyvisdk.do.virtual_cdrom_passthrough_backing_info.VirtualCdromPassthroughBackingInfo`,
    :py:class:`~pyvisdk.do.virtual_disk_raw_disk_ver2_backing_info.VirtualDiskRawDiskVer2BackingInfo`,
    :py:class:`~pyvisdk.do.virtual_ethernet_card_legacy_network_backing_info.VirtualEthernetCardLegacyNetworkBackingInfo`,
    :py:class:`~pyvisdk.do.virtual_ethernet_card_network_backing_info.VirtualEthernetCardNetworkBackingInfo`,
    :py:class:`~pyvisdk.do.virtual_floppy_device_backing_info.VirtualFloppyDeviceBackingInfo`,
    :py:class:`~pyvisdk.do.virtual_parallel_port_device_backing_info.VirtualParallelPortDeviceBackingInfo`,
    :py:class:`~pyvisdk.do.virtual_pci_passthrough_device_backing_info.VirtualPCIPassthroughDeviceBackingInfo`,
    :py:class:`~pyvisdk.do.virtual_pointing_device_device_backing_info.VirtualPointingDeviceDeviceBackingInfo`,
    :py:class:`~pyvisdk.do.virtual_scsi_passthrough_device_backing_info.VirtualSCSIPassthroughDeviceBackingInfo`,
    :py:class:`~pyvisdk.do.virtual_serial_port_device_backing_info.VirtualSerialPortDeviceBackingInfo`,
    :py:class:`~pyvisdk.do.virtual_sound_card_device_backing_info.VirtualSoundCardDeviceBackingInfo`,
    :py:class:`~pyvisdk.do.virtual_usb_remote_host_backing_info.VirtualUSBRemoteHostBackingInfo`,
    :py:class:`~pyvisdk.do.virtual_usbusb_backing_info.VirtualUSBUSBBackingInfo`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.virtual_device_backing_info.VirtualDeviceBackingInfo`
    
.. class:: pyvisdk.do.virtual_device_device_backing_info.VirtualDeviceDeviceBackingInfo
    
    .. py:attribute:: deviceName
    
        The name of the device on the host system.
        
    
    .. py:attribute:: useAutoDetect
    
        Indicates whether the device should be auto detected instead of directly specified. If this value is set to TRUE, deviceName is ignored.
        
    