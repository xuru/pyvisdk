
================================================================================
VirtualSerialPortOption
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.bool_option.BoolOption`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.virtual_device_option.VirtualDeviceOption`
    
.. class:: pyvisdk.do.virtual_serial_port_option.VirtualSerialPortOption
    
    .. py:attribute:: yieldOnPoll
    
        Indicates whether the virtual machine supports the CPU yield option during virtual serial port polling. When this feature is supported and enabled, the virtual machine will periodically relinquish the processor if its sole task is polling the virtual serial port.
        
    