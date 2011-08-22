
================================================================================
VirtualUSB
================================================================================


.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.virtual_device.VirtualDevice`
    
.. class:: pyvisdk.do.virtual_usb.VirtualUSB
    
    .. py:attribute:: connected
    
        Flag indicating whether the device is currently connected. The virtual machine is not connected to the device if the autoconnect pattern specified in the USB device backing (VirtualDeviceDeviceBackingInfo.deviceName) can not be satisfied, either because there is no such device, or the matching device is not available. Valid only while the virtual machine is running.
        
    
    .. py:attribute:: family
    
        Device class families. For possible values see VirtualMachineUsbInfoFamily.
        
    
    .. py:attribute:: product
    
        Product ID of the USB device.
        
    
    .. py:attribute:: speed
    
        Device speeds detected by server. For possible values see VirtualMachineUsbInfoSpeed.
        
    
    .. py:attribute:: vendor
    
        Vendor ID of the USB device.
        
    