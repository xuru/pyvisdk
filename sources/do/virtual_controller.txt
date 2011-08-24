
================================================================================
VirtualController
================================================================================


.. describe:: Extended by
    
    :py:class:`~pyvisdk.do.virtual_ide_controller.VirtualIDEController`,
    :py:class:`~pyvisdk.do.virtual_pci_controller.VirtualPCIController`,
    :py:class:`~pyvisdk.do.virtual_ps2_controller.VirtualPS2Controller`,
    :py:class:`~pyvisdk.do.virtual_scsi_controller.VirtualSCSIController`,
    :py:class:`~pyvisdk.do.virtual_sio_controller.VirtualSIOController`,
    :py:class:`~pyvisdk.do.virtual_usb_controller.VirtualUSBController`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.virtual_device.VirtualDevice`
    
.. class:: pyvisdk.do.virtual_controller.VirtualController
    
    .. py:attribute:: busNumber
    
        Bus number associated with this controller.
        
    
    .. py:attribute:: device
    
        List of devices currently controlled by this controller. Each entry contains the key property of the corresponding device object.
        
    