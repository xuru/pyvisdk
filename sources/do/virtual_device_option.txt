
================================================================================
VirtualDeviceOption
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.virtual_hardware_option.VirtualHardwareOption`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.bool_option.BoolOption`,
    :py:class:`~pyvisdk.do.virtual_device_backing_option.VirtualDeviceBackingOption`,
    :py:class:`~pyvisdk.do.virtual_device_connect_option.VirtualDeviceConnectOption`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Extended by
    
    :py:class:`~pyvisdk.do.virtual_cdrom_option.VirtualCdromOption`,
    :py:class:`~pyvisdk.do.virtual_controller_option.VirtualControllerOption`,
    :py:class:`~pyvisdk.do.virtual_disk_option.VirtualDiskOption`,
    :py:class:`~pyvisdk.do.virtual_ethernet_card_option.VirtualEthernetCardOption`,
    :py:class:`~pyvisdk.do.virtual_floppy_option.VirtualFloppyOption`,
    :py:class:`~pyvisdk.do.virtual_keyboard_option.VirtualKeyboardOption`,
    :py:class:`~pyvisdk.do.virtual_machine_vmci_device_option.VirtualMachineVMCIDeviceOption`,
    :py:class:`~pyvisdk.do.virtual_parallel_port_option.VirtualParallelPortOption`,
    :py:class:`~pyvisdk.do.virtual_pci_passthrough_option.VirtualPCIPassthroughOption`,
    :py:class:`~pyvisdk.do.virtual_pointing_device_option.VirtualPointingDeviceOption`,
    :py:class:`~pyvisdk.do.virtual_scsi_passthrough_option.VirtualSCSIPassthroughOption`,
    :py:class:`~pyvisdk.do.virtual_serial_port_option.VirtualSerialPortOption`,
    :py:class:`~pyvisdk.do.virtual_sound_card_option.VirtualSoundCardOption`,
    :py:class:`~pyvisdk.do.virtual_usb_option.VirtualUSBOption`,
    :py:class:`~pyvisdk.do.virtual_video_card_option.VirtualVideoCardOption`,
    :py:class:`~pyvisdk.do.virtual_vmirom_option.VirtualVMIROMOption`
    
.. class:: pyvisdk.do.virtual_device_option.VirtualDeviceOption
    
    .. py:attribute:: autoAssignController
    
        Flag to indicate whether or not this device will be auto-assigned a controller if one is required. If this is true, then a client need not explicitly create the controller that this device will plug into.
        
    
    .. py:attribute:: backingOption
    
        A list of backing options that can be used to map the virtual device to the host. The list is optional, since some devices exist only within the virtual machine; for example, a VirtualController.
        
    
    .. py:attribute:: connectOption
    
        If the device is connectable, then the connectOption describes the connect options and defaults.
        
    
    .. py:attribute:: controllerType
    
        Data object type that denotes the controller option object that is valid for controlling this device.
        
    
    .. py:attribute:: defaultBackingOptionIndex
    
        Index into the backingOption list, indicating the default backing.
        
    
    .. py:attribute:: deprecated
    
        Indicates whether this device is deprecated. Hence, if set the device cannot be used when creating a new virtual machine or be added to an existing virtual machine. However, the device is still supported by the platform.
        
    
    .. py:attribute:: hotRemoveSupported
    
        Indicates if this type of device can be hot-removed from the virtual machine via a reconfigure operation when the virtual machine is powered on.
        
    
    .. py:attribute:: licensingLimit
    
        List of property names enforced by a licensing restriction of the underlying product. For example, a limit that is not derived based on the product or hardware features; the property name "numCPU".
        
    
    .. py:attribute:: plugAndPlay
    
        Indicates if this type of device can be hot-added to the virtual machine via a reconfigure operation when the virtual machine is powered on.
        
    
    .. py:attribute:: type
    
        The name of the run-time class the client should instantiate to create a run-time instance of this device.
        
    