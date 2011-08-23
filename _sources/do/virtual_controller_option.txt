
================================================================================
VirtualControllerOption
================================================================================


.. describe:: Extended by
    
    :py:class:`~pyvisdk.do.virtual_ide_controller_option.VirtualIDEControllerOption`,
    :py:class:`~pyvisdk.do.virtual_pci_controller_option.VirtualPCIControllerOption`,
    :py:class:`~pyvisdk.do.virtual_ps2_controller_option.VirtualPS2ControllerOption`,
    :py:class:`~pyvisdk.do.virtual_scsi_controller_option.VirtualSCSIControllerOption`,
    :py:class:`~pyvisdk.do.virtual_sio_controller_option.VirtualSIOControllerOption`,
    :py:class:`~pyvisdk.do.virtual_usb_controller_option.VirtualUSBControllerOption`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.int_option.IntOption`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.virtual_device_option.VirtualDeviceOption`
    
.. class:: pyvisdk.do.virtual_controller_option.VirtualControllerOption
    
    .. py:attribute:: devices
    
        The minimum and maximum number of devices this controller can control at run time.
        
    
    .. py:attribute:: supportedDevice
    
        Array of supported device options for this controller.
        
    