
================================================================================
VirtualDevice
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.ovf_hardware_export.OvfHardwareExport`,
    :py:class:`~pyvisdk.do.ovf_unknown_device.OvfUnknownDevice`,
    :py:class:`~pyvisdk.do.virtual_device_config_spec.VirtualDeviceConfigSpec`,
    :py:class:`~pyvisdk.do.virtual_hardware.VirtualHardware`,
    :py:class:`~pyvisdk.do.virtual_machine_config_option.VirtualMachineConfigOption`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.description.Description`,
    :py:class:`~pyvisdk.do.virtual_device_backing_info.VirtualDeviceBackingInfo`,
    :py:class:`~pyvisdk.do.virtual_device_connect_info.VirtualDeviceConnectInfo`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Extended by
    
    :py:class:`~pyvisdk.do.virtual_cdrom.VirtualCdrom`,
    :py:class:`~pyvisdk.do.virtual_controller.VirtualController`,
    :py:class:`~pyvisdk.do.virtual_disk.VirtualDisk`,
    :py:class:`~pyvisdk.do.virtual_ethernet_card.VirtualEthernetCard`,
    :py:class:`~pyvisdk.do.virtual_floppy.VirtualFloppy`,
    :py:class:`~pyvisdk.do.virtual_keyboard.VirtualKeyboard`,
    :py:class:`~pyvisdk.do.virtual_machine_video_card.VirtualMachineVideoCard`,
    :py:class:`~pyvisdk.do.virtual_machine_vmci_device.VirtualMachineVMCIDevice`,
    :py:class:`~pyvisdk.do.virtual_machine_vmirom.VirtualMachineVMIROM`,
    :py:class:`~pyvisdk.do.virtual_parallel_port.VirtualParallelPort`,
    :py:class:`~pyvisdk.do.virtual_pci_passthrough.VirtualPCIPassthrough`,
    :py:class:`~pyvisdk.do.virtual_pointing_device.VirtualPointingDevice`,
    :py:class:`~pyvisdk.do.virtual_scsi_passthrough.VirtualSCSIPassthrough`,
    :py:class:`~pyvisdk.do.virtual_serial_port.VirtualSerialPort`,
    :py:class:`~pyvisdk.do.virtual_sound_card.VirtualSoundCard`,
    :py:class:`~pyvisdk.do.virtual_usb.VirtualUSB`
    
.. class:: pyvisdk.do.virtual_device.VirtualDevice
    
    .. py:attribute:: backing
    
        Information about the backing of this virtual device presented in the context of the virtual machine's environment. Not all devices are required to have backing information.
        
    
    .. py:attribute:: connectable
    
        Provides information about restrictions on removing this device while a virtual machine is running. If the device is not removable, then this property is null.
        
    
    .. py:attribute:: controllerKey
    
        Object key for the controller object for this device. This property contains the key property value of the controller device object.
        
    
    .. py:attribute:: deviceInfo
    
        Provides a label and summary information for the device.
        
    
    .. py:attribute:: key
    
        A unique key that distinguishes this device from other devices in the same virtual machine. Keys are immutable but may be recycled; that is, a key does not change as long as the device is associated with a particular virtual machine. However, once a device is removed, its key may be used when another device is added.
        
    
    .. py:attribute:: unitNumber
    
        The unit number of this device on its controller. This property is null if the controller property is null (for example, when the device is not attached to a specific controller object).
        
    